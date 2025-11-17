from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.settings.settings import settings
from app.models import schemas
from fastapi.security import  OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.models import models

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password:str):
    return pwd_context.verify(password, hashed_password)


def get_access_token(data: dict):
    data_to_encode = data.copy()

    if not settings.token_expire_minutes:
        expire_minute = datetime.utcnow() + timedelta(minutes=30)
    else:
        expire_minute = datetime.utcnow() + timedelta(minutes=int(settings.token_expire_minutes))

    data_to_encode.update({"exp": expire_minute})
    encoded_jwt = jwt.encode(data_to_encode, settings.secrect_key, settings.algorithm)

    return encoded_jwt

def verify_access_token(token: str, exceptions: str):
    try: 
        payload = jwt.decode(token, settings.secrect_key, [settings.algorithm])
        user_email = payload.get("user_email")
        if not user_email:
            raise exceptions

        user = schemas.TokenData(email=user_email)

    except Exception:
        raise exceptions
    
    return user.email

def get_current_user(token: str = Depends(oauth2_schema)):
    exceptions = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not athorized, provide correct credentails", headers={"WWW-Authenticate": "Bearer"})

    return verify_access_token(token, exceptions)


def get_user(email: str, db):
    """ Helper function to retrieve a user for easy lookups"""
    user = db.query(models.User).filter(models.User.email == email).first()
    return user