from app.models import schemas
from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.database import database
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import get_current_user


router = APIRouter(
    tags=["Authentications/Authorization"]
)


@router.post("/register/", response_model=schemas.ResgistrationOut)
def register(credentials: schemas.RegistrationIn, db: Session = Depends(database.get_db)):
    registration_service = AuthService.register_user(credentials, db=db)
    return registration_service

@router.post("/login/", response_model=schemas.Token)
def login(credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    login_service = AuthService.login_user(credentials, db)
    return login_service
 

