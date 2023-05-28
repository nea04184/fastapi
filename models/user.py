from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    user_id: str
    username: str
    email: str

class UserIn(UserBase):
    password: str

class UserOut(BaseModel):
    user_id: str
    username: str
    email: str
    created_at: Optional[datetime] = Field(...)

class UserInDB(UserBase):
    hashed_password: str
    created_at: Optional[datetime]
