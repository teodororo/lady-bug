from src.database.database import LadybugMongo
from src.utils.errors import HTTPClientError
from sanic.request import Request
from sanic.response import json
from sanic import response

from copy import deepcopy
from json import dumps
from src.utils.serialize import Serialize
from src.utils.models_paraments import Identifier
from src.controllers.base_controller import BaseController


class BugController(BaseController):
    # GET ALL
    @classmethod
    async def index(cls, request:Request):
        bugs = await cls.database.find('bugs')
        payload = {"items": bugs}
        return json(payload, dumps=dumps, cls=Serialize, status=200)

    # GET BY ID 
    @classmethod
    async def show(cls, request:Request, bug_id: str):
        try:
            bug_specific_id = Identifier(bug_id).format()
            bug = await cls.database.find_one_by_id('bugs',bug_specific_id)
            return json(bug, dumps=dumps, cls=Serialize, status=200)           
        except HTTPClientError as e:
            return json(status=e.status)

    # POST
    @classmethod
    async def store(cls, request: Request):
        bug = deepcopy(request.json)
        try: 
            inserted =  await cls.database.insert_one('bugs',bug)
            return response.json(inserted, dumps=dumps, cls=Serialize, status=201)
        except HTTPClientError as e:
            return json(status=e.status)

    # PUT
    @classmethod
    async def edit(cls, request: Request, bug_id: str):
        bug = deepcopy(request.json)
        try:
            bug_specific_id = Identifier(bug_id).format()
            _bug = await cls.database.find_one_by_id('bugs',bug_specific_id)
            updated = await cls.database.replace_one('bugs',bug_specific_id,_bug)
            return json(updated, dumps=dumps, cls=Serialize, status=200)
        except HTTPClientError as e:
            return json(status=e.status)
            
    # DELETE
    @classmethod
    async def destroy(cls, request: Request, bug_id: str):
        try:
            bug_specific_id = Identifier(bug_id).format()
            await cls.database.delete_one('bugs',bug_specific_id)
            return json(None, status=204)
        except HTTPClientError as e:
            return json(status=e.status)

    
