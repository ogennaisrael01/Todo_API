from sqlalchemy.orm import Session
from app.models import models
from fastapi import HTTPException, status
from app.utils.security import hash_password, verify_password, get_access_token
from fastapi.responses import JSONResponse

class AuthService:
    @staticmethod
    def register_user(user_credentials, db):
        user = db.query(models.User).filter(models.User.email ==  user_credentials.email).first()
        if user:
            raise  HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already  exists, try logging in")
        
        credentials = user_credentials.model_dump()
        credentials["password"] = hash_password(user_credentials.password)

        save_user = models.User(**credentials)
        db.add(save_user)
        db.commit()
        db.refresh(save_user)
        return save_user
    
    @staticmethod
    def login_user(user_credentials, db):
        email = user_credentials.username
        user = db.query(models.User).filter(models.User.email == email).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentails inputed, try again")
        # Check for password match with the hashed password
        if not verify_password(user_credentials.password, user.password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentails inputed, try again")

        # If credentails match, get access token
        access_token = get_access_token({"user_email": email})
        return JSONResponse({
            "access_token": access_token,
            "token_type": "Bearer",
        })
