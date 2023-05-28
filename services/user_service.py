from motor.motor_asyncio import AsyncIOMotorClient
from models.user import UserInDB, UserIn
from utils.hashing import Hasher
from utils.config import get_settings

settings = get_settings()


class UserService:
    def __init__(self, db: AsyncIOMotorClient = None):
        self.db = db or AsyncIOMotorClient(settings.mongo_db_url)
        self.collection = self.db.get_database(
            settings.mongo_db_name).get_collection("users")

    async def create_user(self, user: UserIn):
        user_in_db = UserInDB(
            **user.dict(), hashed_password=Hasher.get_hashed_password(user.password)
        )
        result = await self.collection.insert_one(user_in_db.dict())
        return str(result.inserted_id)
