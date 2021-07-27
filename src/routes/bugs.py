from src.controllers.base_controller import BaseController
from sanic import Blueprint
from sanic.request import Request
from sanic.response import json 

from src.controllers.bug_controller import BugController

from src.database.database import LadybugMongo

bug = Blueprint(name='content_bugs',url_prefix='/bugs')

@bug.middleware('request')
async def middleware(request: Request):
    pass

# GET ALL
@bug.get('/')
async def index(request: Request):
    return await BugController.index(request)

# GET BY ID 
@bug.get('/<bug_id>')
async def show(request: Request, bug_id):
    return await BugController.show(request, bug_id)

# PUT 
@bug.put('/<bug_id>')
async def edit(request: Request, bug_id):
    return await BugController.edit(request, bug_id)

# POST
@bug.post('/')
async def store(request: Request):
    return await BugController.store(request)

# DELETE 
@bug.delete('/<bug_id>')
async def destroy(request: Request, bug_id):
    return await BugController.destroy(request, bug_id)

# OPTIONS
@bug.options('/')
async def options(request: Request):
    return json(None)