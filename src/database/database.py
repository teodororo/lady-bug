from pymongo import MongoClient

from asyncio import AbstractEventLoop
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from src.utils.environments import env

#client = MongoClient('mongodb://ladybug_root:123ladybug@localhost:27017/')

class Database:
    @classmethod
    def connect(cls):
        raise NotImplementedError

    @classmethod
    def connection(cls):
        raise NotImplementedError

class LadybugMongo(Database):
    client = None
    host = None
    port = None
    username = None
    password = None
    io_loop = None

    def __new__(cls, io_loop: AbstractEventLoop, *args, **kwargs):
        cls.host = env('DATABASE_HOST')
        cls.port = int(env('DATABASE_PORT'))
        cls.username = env('DATABASE_USER')
        cls.password = env('DATABASE_PASS')
        cls.io_loop = io_loop

    @classmethod
    def connect(cls):
        LadybugMongo.client = AsyncIOMotorClient(
            host=cls.host,
            port=cls.port,
            username=cls.username,
            password=cls.password,
            io_loop=cls.io_loop
            )

    @classmethod
    def connection(cls):
        return cls.client[env('DATABASE_NAME')]

    @classmethod
    def disconnect(cls):
        cls.client.close()

    @classmethod
    async def insert_one(cls, collection: str, data: dict):
        database = cls.connection()
        inserted = await database[collection].insert_one(data)
        return await database[collection].find_one(
            {'_id': inserted.inserted_id})

    @classmethod
    async def update_one(cls, collection: str,  match: dict, update: dict):
        database = cls.connection()
        await database[collection].update_many(match,{"$set": update })
        return await database[collection].find_one(match)

    @classmethod
    async def find(cls, collection: str,size=100):
        database = cls.connection()
        cursor = database[collection].find()
        documents = await cursor.to_list(size)
        return documents

    @classmethod
    async def find_one_by_id(cls, collection: str, _id):
        database = cls.connection()
        return await database[collection].find_one({'_id': ObjectId(_id)})

    @classmethod
    async def find_one(cls, collection: str):
        database = cls.connection()
        return await database[collection].find_one()


    @classmethod
    async def delete_one(cls, collection: str, _id):
        database = cls.connection()
        await database[collection].delete_one({'_id': ObjectId(_id)})
