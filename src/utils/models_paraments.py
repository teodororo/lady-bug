
from bson.objectid import ObjectId

class Identifier:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.validate()

    def validate(self):
        if not ObjectId.is_valid(self.identifier):
            raise AssertionError(message='Invalid id')

    def format(self):
        return ObjectId(self.identifier)