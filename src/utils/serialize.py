import json
from datetime import datetime

from bson.objectid import ObjectId


class Serialize(json.JSONEncoder):
    def default(self, field):
        if isinstance(field, datetime):
            return field.isoformat() + 'Z'

        if isinstance(field, ObjectId):
            return field.__str__()

        else:
            return super(Serialize, self).default(field)
