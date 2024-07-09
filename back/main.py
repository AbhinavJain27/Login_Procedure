from fastapi import FastAPI , HTTPException , status , Depends
from typing import Annotated
from database import SessionLocal , engine
import models
from pydantic import BaseModel
from sqlalchemy.orm import Session

app=FastAPI()
models.User_Base.metadata.create_all(bind=engine)

class User_In(BaseModel):
    username : str
    password:str

class User_Up(User_In):
      Name:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated [Session , Depends(get_db)]

@app.post("/create_user" , status_code=status.HTTP_201_CREATED)
async def sign_up(user:User_Up , db:db_dependency):
    our_user = models.User_Base(**user.dict())
    db_user=db.query(models.User_Base).filter(models.User_Base.username==our_user.username).first()
    if db_user is None or db_user.username!=user.username:
        db.add(our_user)
        db.commit()
        return "user was created" 
    else:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE ,
                            detail=f'Username {db_user.username} is already taken')
    
@app.post("/get_user" ,  status_code=status.HTTP_200_OK)
async def sign_in(user:User_In , db:db_dependency):
    db_user=db.query(models.User_Base).filter(models.User_Base.username==user.username).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail="User was not found")
    if not user.password == db_user.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='username or password is incorrect')
    else:
        return "Successful Authentication"