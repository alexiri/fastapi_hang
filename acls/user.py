from models import db_session, User

def num_users():
    return db_session.query(User).count()
