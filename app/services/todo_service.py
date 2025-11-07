from fastapi import HTTPException, status, Depends
from app.utils.security import get_current_user, get_user
from datetime import datetime, timezone
from app.models import models
from typing import List

from fastapi.responses import JSONResponse

class TodoService:
    @staticmethod
    def create_todo(form_data: dict, db, user_email: str):
        if not form_data.task:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Please enter your task to do")
        # if form_data.due_date < datetime.now(timezone.utc):
        #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Due date can't be less than now ")

        if db.query(models.Todo).filter(models.Todo.task == form_data.task).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You already created this task. Complete it before creating another one")
        
        # Get uset id
        user = get_user(email=user_email, db=db)
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query does not match")
        
        user_id = user.id

        # Convert form data to dict

        data = form_data.model_dump()

        save_todo = models.Todo(**data, user_id=user_id)
        message = "Your Todo has been added, you can track each task seamlessly"
        notification = models.Notification(reciever=user_id, message=message)
        db.add(save_todo)
        db.add(notification)    
        
        db.commit()
        db.refresh(save_todo)
        return save_todo

    @staticmethod
    def all_todos(search: str, db, user_email: str):
        """ all todos that are own by the user """
        user = get_user(email=user_email, db=db)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        query = db.query(models.Todo).filter(models.Todo.user_id == user.id)
        todos = query.all()
        if not todos:
            return []
        if search:
            todos = query.filter(models.Todo.task.contains(search.lower()))
        
        return todos
    
    @staticmethod
    def retrieve_todo(todo_id: int, db, user_email:str):
        user = get_user(email=user_email, db=db)
        todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == user.id).first()  
        if not todo:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        
        return todo
    
    @staticmethod
    def toggle_to_complete(todo_id: int, db, user_email: str):
        user = get_user(email=user_email, db=db)
        todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == user.id).first()  
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        
        if todo.completed == True:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Already marked as completed")
        
        todo.completed = True
        db.commit()
        return JSONResponse({
            "message": f"Todo titled: {todo.task} is marked as completed. You can go ahead and delete the todo"
        })
    
    @staticmethod
    def update_todo_by_id(todo_id: int, todo_form: dict, db, user_email: str):
        user = get_user(email=user_email, db=db)
        get_todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == user.id).first()

        if not get_todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        
        if get_todo.completed == True:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Can't update already completed task!")
        
        to_dict = todo_form.model_dump()
        for key, value in to_dict.items():
            setattr(get_todo, key, value)
       
        db.commit()
        db.refresh(get_todo)

        return get_todo
    

    @staticmethod
    def delete_todo(todo_id: str, db, user_email:str):
        user = get_user(email=user_email, db=db)
        todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()

        if not todo.user_id == user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Can't perform this action")
        if not todo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detial="No item with this id")

        db.delete(todo)
        db.commit()

    @staticmethod
    def toggle_to_incomplete(todo_id:str, db, user_email: str):

        user = get_user(email=user_email, db=db)
        todo = db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.user_id == user.id).first()
        if not todo:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"There is todo with the given id")
        
        if todo.completed == False:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Todo already marked as incomplete")
        
        todo.completed = False
        db.commit()
        db.refresch(todo)
        return todo

        
  
        