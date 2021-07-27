from sanic import Blueprint
from .projects import project
from .bugs import bug

#from .suites import suite 

# add more collections here 
#routes = Blueprint.group([projects,users,bugs],url_prefix='/')
routes = Blueprint.group([bug, project])