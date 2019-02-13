from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

# SQLAlchemy specific code, as with any other app
#SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/srschool"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class CustomBase:
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)


Base.metadata.create_all(bind=engine)
