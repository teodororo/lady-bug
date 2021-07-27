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


class ProjectController(BaseController):
    # GET ALL
    @classmethod
    async def index(cls, request:Request):
        projects = await cls.database.find('projects')
        payload = {"items": projects}
        return json(payload, dumps=dumps, cls=Serialize, status=200)

    # GET BY ID 
    @classmethod
    async def show(cls, request:Request, project_id: str):
        try:
            project_specific_id = Identifier(project_id).format()
            project = await cls.database.find_one_by_id('projects',project_specific_id)
            return json(project, dumps=dumps, cls=Serialize, status=200)           
        except HTTPClientError as e:
            return json(status=e.status)

    # POST
    @classmethod
    async def store(cls, request: Request):
        project = deepcopy(request.json)
        try: 
            inserted =  await cls.database.insert_one('projects',project)
            return response.json(inserted, dumps=dumps, cls=Serialize, status=201)
        except HTTPClientError as e:
            return json(status=e.status)

    # PUT
    @classmethod
    async def edit(cls, request: Request, project_id: str):
        project = deepcopy(request.json)
        try:
            project_specific_id = Identifier(project_id).format()
            _project = await cls.database.find_one_by_id('projects',project_specific_id)
            updated = await cls.database.replace_one('projects',project_specific_id,_project)
            return json(updated, dumps=dumps, cls=Serialize, status=200)
        except HTTPClientError as e:
            return json(status=e.status)
            
    # DELETE
    @classmethod
    async def destroy(cls, request: Request, project_id: str):
        try:
            project_specific_id = Identifier(project_id).format()
            #project = await cls.database.find_one('projects',{'_id':project_specific_id})
            await cls.database.delete_one('projects',project_specific_id)
            return json(None, status=204)
        except HTTPClientError as e:
            return json(status=e.status)

    
