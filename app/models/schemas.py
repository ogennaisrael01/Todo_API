from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class RegistrationIn(BaseModel):
    email : EmailStr
    password: str

class ResgistrationOut(BaseModel):
    id : int
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr


class TodoCreate(BaseModel):
    task: str
    description: str | None = None
    due_date: datetime | None = None
    priority: str | None = None

class TodoOut(TodoCreate):
    completed: bool
    user_id : int
    created_at: datetime
    id: int
    
    class Config:
        orm_mode = True

class UpdateTodo(TodoCreate):
    ...


