from quart import Blueprint

index_bp = Blueprint("index", __name__)

from . import routes
