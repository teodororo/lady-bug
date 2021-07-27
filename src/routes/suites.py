from src.controllers.base_controller import BaseController
from sanic import Blueprint
from sanic.request import Request
from sanic.response import json 

from src.controllers.suite_controller import SuiteController
from src.database.database import LadybugMongo

suite = Blueprint(name='content_suites',url_prefix='/projects/<project_id>/suites')

@suite.middleware('request')
async def middleware(request: Request):
    pass

# GET ALL
@suite.get('/')
async def index(request: Request, project_id:str):
    return await SuiteController.index(request,project_id)

# GET BY ID 
@suite.get('/<suite_id>')
async def show(request: Request, Suite_id):
    return await SuiteController.show(request, Suite_id)

# PUT 
@suite.put('/<suite_id>')
async def edit(request: Request, Suite_id):
    return await SuiteController.edit(request, Suite_id)

# POST
@suite.post('/')
async def store(request: Request,project_id:str):
    print("entrou na rota de post do Suite")
    return await SuiteController.store(request,project_id)

# DELETE 
@suite.delete('/<suite_id>')
async def destroy(request: Request, Suite_id):
    return await SuiteController.destroy(request, Suite_id)

# OPTIONS
@suite.options('/')
async def options(request: Request):
    return json(None)