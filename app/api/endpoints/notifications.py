from app.database.database import get_db
from app.utils.security import get_current_user
from sqlalchemy.orm import Session
from app.services.notification_service import NotificationService
from app.models.schemas import NotificationOut
from fastapi import Depends, status, APIRouter


router = APIRouter(
    tags=["Notifications"]
)


@router.get("/notifications", status_code=status.HTTP_200_OK)
def notifications(user: str = Depends(get_current_user), db : Session = Depends(get_db)):
    """ Notifications"""
    notif = NotificationService.get_notifications(user, db)
    return notif