from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import Base, User

class db_storage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/hi_friend')
        
    def add(self, obj):
        self.__session.add(obj)
        self.__session.commit()
        
    def login(self, email):
        for user in self.all():
            if self.all()[user]['email'] == email:
                return self.all()[user]
        return None
    
    def all(self):
        dic_users = {}
        for user in self.__session.query(User).all():
            dic_users[str(user.id)] = {'username': user.username,
                                  'email': user.email,
                                     'password': user.password,
                                     }
        return dic_users
    
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session