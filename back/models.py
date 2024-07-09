from database import base
from sqlalchemy import Column , String , Integer 

class User_Base(base):
    __tablename__='login_user'

    id = Column(Integer , primary_key = True , index = True)
    Name = Column(String(50))
    username = Column(String(50) , unique =True)
    password = Column(String(50))