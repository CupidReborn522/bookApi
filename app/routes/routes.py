from flask import Blueprint

routesBlueprint = Blueprint('routes',__name__)


@routesBlueprint.route('/')
def index():
    pass