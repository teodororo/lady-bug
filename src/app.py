from asyncio import AbstractEventLoop
from sanic import Sanic
from sanic_amqp import BaseExtension
from sanic.request import Request
from secure import SecureHeaders
from src.database.database import LadybugMongo

from src.routes import routes
from src.utils.environments import env
from sanic_cors import CORS
from src.controllers.base_controller import BaseController


app: BaseExtension = Sanic(__name__)
app.blueprint(routes)
CORS(app)


@app.middleware('request')
async def set_headers_request(request: Request):
    request.headers["User-ID"] = request.ip

@app.middleware('response')
async def set_headers_response(request: Request, response):
    SecureHeaders().sanic(response)

@app.listener('before_server_start')
async def start_mongo(server: Sanic, loop: AbstractEventLoop):
    if env('APP_MODE') == 'development':
        LadybugMongo(loop)
        LadybugMongo.connect()

@app.listener('before_server_start')
async def inject_dependency(server: Sanic, loop: AbstractEventLoop):
    if env('APP_MODE') == 'development':
        BaseController(LadybugMongo)
