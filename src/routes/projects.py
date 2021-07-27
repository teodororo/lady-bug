from src.controllers.base_controller import BaseController
from sanic import Blueprint
from sanic.request import Request
from sanic.response import json 

from src.controllers.project_controller import ProjectController
from src.database.database import LadybugMongo

project = Blueprint(name='content_projects',url_prefix='/projects')

@project.middleware('request')
async def middleware(request: Request):
    pass

# GET ALL
@project.get('/')
async def index(request: Request):
    return await ProjectController.index(request)

# GET BY ID 
@project.get('/<project_id>')
async def show(request: Request, project_id):
    return await ProjectController.show(request, project_id)

# PUT 
@project.put('/<project_id>')
async def edit(request: Request, project_id):
    return await ProjectController.edit(request, project_id)

# POST
@project.post('/')
async def store(request: Request):
    print("entrou na rota de post do project")
    return await ProjectController.store(request)

# DELETE 
@project.delete('/<project_id>')
async def destroy(request: Request, project_id):
    return await ProjectController.destroy(request, project_id)

# OPTIONS
@project.options('/')
async def options(request: Request):
    return json(None)