from src.database.database import LadybugMongo
#from src.database import ShellMongo, MinioStorageFile

class BaseController:
    database: LadybugMongo = None
    #storage: MinioStorageFile

    #def __new__(cls, database, storage, *args, **kwargs):
    def __new__(cls, database, *args, **kwargs):
        print(database)
        cls.database = database
        #cls.storage = storage
