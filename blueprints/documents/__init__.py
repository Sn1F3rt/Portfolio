from quart import Blueprint

documents_bp = Blueprint("documents", __name__)

from . import routes
