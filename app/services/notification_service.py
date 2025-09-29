from app.models.models import Notification
from app.utils.security import get_current_user, get_user

class NotificationService:
    @staticmethod   
    def get_notifications(user: str, db):
        user = get_user(email=user, db=db)
        query = db.query(Notification).filter(Notification.reciever == user.id).all()

        if not query:
            return []
        
        return query