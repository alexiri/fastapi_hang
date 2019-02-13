from fastapi import FastAPI, Depends
from models import db_session, User
from acls.user import num_users

first_user = db_session.query(User).first()
if not first_user:
    u = User(email="johndoe@example.com", hashed_password="notreallyhashed")
    db_session.add(u)
    db_session.commit()


# Utility
def get_user(db_session, user_id: int):
    return db_session.query(User).filter(User.id == user_id).first()


# FastAPI specific code
app = FastAPI()


@app.get("/users/{user_id}")
def read_user(user_id: int, count: int = Depends(num_users)):
    user = get_user(db_session, user_id=user_id)
    return {'user': user, 'count': count}
