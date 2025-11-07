from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from app.database.database import engine
from app.models import models 
from app.api.endpoints import auth, todos, notifications

app = FastAPI(
    title= "API for a todo application"
)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return JSONResponse({"message": "Welcome to our Todo API PRoject"}, status_code=status.HTTP_200_OK)


# Register Routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(todos.router, prefix="/api/v1")
app.include_router(notifications.router, prefix="/api/v1")
