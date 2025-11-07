from ..database.database import Base
from pydantic import EmailStr
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, nullable=False, primary_key=True)
    email: EmailStr = Column(String, nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    created_at : str = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, nullable=False, primary_key= True)
    task = Column(String, nullable=False)
    description = Column(String, nullable=True)     
    completed = Column(Boolean, default=False)
    due_date = Column(TIMESTAMP(timezone=True), nullable=True)
    priority = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"), onupdate=text("now()"))

    user = relationship("User")


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, nullable=False,primary_key=True)
    reciever = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")) 

    