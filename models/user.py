from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    """
    User class to store user information
    
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    #first_name = Column(String(250), nullable=False)
    #last_name = Column(String(250), nullable=False)
    #age = Column(Integer, nullable=False)
    #img = Column(String(60))
    
    
    
    