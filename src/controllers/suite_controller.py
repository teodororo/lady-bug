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


class SuiteController(BaseController):
    # GET ALL
    @classmethod
    async def index(cls, request:Request, project_id: str):
        project_id = Identifier(project_id).format()
        project = await cls.database.find_one_by_id('projects',project_id)
        print(project)
        suites = project['suites']
        return json(suites, dumps=dumps, cls=Serialize, status=200)

    # GET BY ID 
    @classmethod
    async def show(cls, request:Request, Suite_id: str):
        try:
            Suite_specific_id = Identifier(Suite_id).format()
            Suite = await cls.database.find_one('Suites',{'_id':Suite_specific_id})
            return json(Suite, dumps=dumps, cls=Serialize, status=200)           
        except HTTPClientError as e:
            return json(status=e.status)

    # POST
    @classmethod
    async def store(cls, request: Request, project_id:str):
        suite = deepcopy(request.json)
        project_id = Identifier(project_id).format()
        project = await cls.database.find_one_by_id('projects',project_id)
        if not 'suites' in project:
            print("ta caindo")
            project['suites'] = []
        if 'suites' in project:
            project['suites'].append(suite)
        inserted =  await cls.database.insert_one('projects',project)
        return json(inserted, dumps=dumps, cls=Serialize, status=200)

    # PUT
    @classmethod
    async def edit(cls, request: Request, Suite_id: str):
        Suite = deepcopy(request.json)
        try:
            Suite_specific_id = Identifier(Suite_id).format()
            _Suite = await cls.database.find_one('Suites',{'_id':Suite_specific_id})
            updated = await cls.database.replace_one('Suites',{'_id':Suite_specific_id},_Suite)
            return json(updated, dumps=dumps, cls=Serialize, status=200)
        except HTTPClientError as e:
            return json(status=e.status)
            
    # DELETE
    @classmethod
    async def destroy(cls, request: Request, Suite_id: str):
        try:
            Suite_specific_id = Identifier(Suite_id).format()
            await cls.database.delete_one('Suites',Suite_specific_id)
            return json(None, status=204)
        except HTTPClientError as e:
            return json(status=e.status)

    
