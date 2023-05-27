from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    user_id: str
    username: str
    email: str

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    created_at: datetime

class UserInDB(UserBase):
    hashed_password: str
    created_at: Optional[datetime]
