# Todo List API

A robust, extensible RESTful API for managing personal tasks, built with FastAPI and SQLAlchemy. This project supports user authentication, task CRUD operations, and advanced features for productivity and organization.

## Features

1. **User Authentication**
   - Register and log in users (JWT-based).
   - Each user manages their own tasks securely.

2. **Create Task**
   - Add new tasks with title and description.
   - Optional: due date and priority fields.

3. **View Tasks**
   - Fetch all tasks for the logged-in user.
   - Filter by completed/not completed status.

4. **Update Task**
   - Edit task details (title, description, due date, priority).

5. **Delete Task**
   - Remove a task permanently.

6. **Mark Task as Completed/Incomplete**
   - Toggle status between done and not done.

8. **Sorting and Filtering**
   - Sort by due task


9. **Reminders / Notifications**
   - Inapp notifications for upcoming tasks.

10. **Search**
    - Keyword search in tasks.

---

## 🏗️ Project Structure

- `app/main.py` — FastAPI entrypoint, includes routers and middleware.
- `app/api/endpoints/` — Route handlers for authentication and todos.
- `app/services/` — Business logic for authentication and todo management.
- `app/models/` — SQLAlchemy models and Pydantic schemas.
- `app/database/` — Database session and engine setup.
- `app/utils/` — Security utilities (JWT, password hashing).
- `migrations/` — Alembic migration scripts.

## 🛠️ Developer Workflow

- **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- **Run the API locally:**
  ```bash
  uvicorn app.main:app --reload
  ```
- **Run migrations:**
  ```bash
  alembic upgrade head
  ```
- **Run tests:**
  (Add your test command here if available)

## 🔑 Environment Variables

- Configure database URL, JWT secret, and other settings in `app/settings/settings.py` or via environment variables.

## 📦 Dependencies
- FastAPI
- SQLAlchemy
- Alembic
- Passlib (for password hashing)
- jose (for JWT handling)
- pydantic


## 📚 Example API Usage

- Register: `POST /auth/register`
- Login: `POST /auth/login`
- Create Task: `POST /todos/`
- List Tasks: `GET /todos/`
- Update Task: `PUT /todos/{id}`
- Delete Task: `DELETE /todos/{id}`

---

## 📝 Contributing
Pull requests are welcome! Please follow project structure and conventions.

---
