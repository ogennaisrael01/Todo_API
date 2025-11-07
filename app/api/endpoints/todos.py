from app.models import schemas
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.database import database
from app.utils.security import get_current_user
from app.services.todo_service import TodoService
from typing import List


router = APIRouter(
    tags=["Todos"]
)

@router.post("/add-todo/", response_model=schemas.TodoOut, status_code=status.HTTP_201_CREATED)
def add_todo(form_data: schemas.TodoCreate, db: Session = Depends(database.get_db), user_email: str = Depends(get_current_user)):
    todo_service = TodoService.create_todo(form_data, db, user_email)
    return todo_service

@router.get("/todos/", status_code=status.HTTP_200_OK, response_model=List[schemas.TodoOut])
def list_todos(search: str | None = None, db: Session = Depends(database.get_db), user_email:str = Depends(get_current_user)):
    """ List a queryset of all the todos with search funtionality(task, status, date) """
    queryset =  TodoService.all_todos(search, db, user_email)
    return queryset

@router.get("/todos/{todo_id}/", status_code=status.HTTP_200_OK, response_model=schemas.TodoOut)
def get_todo(todo_id: int, db: Session = Depends(database.get_db), user_email:str = Depends(get_current_user)):
    queryset =  TodoService.retrieve_todo(todo_id, db, user_email)
    return queryset


@router.post("/toggle_complete/{todo_id}/", status_code=status.HTTP_200_OK)
def mart_as_complete(todo_id: int, db: Session = Depends(database.get_db), user_email: str = Depends(get_current_user)):
    marked_todo = TodoService.toggle_to_complete(todo_id, db, user_email)
    return marked_todo

@router.put("/todo/update/{todo_id}", response_model=schemas.TodoOut, status_code=status.HTTP_200_OK)
def update_todo(todo_id: int, todo_form: schemas.UpdateTodo, db: Session = Depends(database.get_db), user_email: str = Depends(get_current_user)):
    updated_todo = TodoService.update_todo_by_id(todo_id, todo_form, db, user_email)
    return updated_todo

@router.delete("/todo/delete/{todo_id}/", status_code=status.HTTP_404_NOT_FOUND)
def delete(todo_id: int, db: Session = Depends(database.get_db), user_email: str = Depends(get_current_user)):
    todo_to_delete = TodoService.delete_todo(todo_id, db, user_email)
    return todo_to_delete


@router.post("/toggle_incomplete/{todo_id}/", status_code=status.HTTP_200_OK)
def mart_as_incomplete(todo_id: int, db: Session = Depends(database.get_db), user_email: str = Depends(get_current_user)):
    marked_todo = TodoService.toggle_to_incomplete(todo_id, db, user_email)
    return marked_todo


