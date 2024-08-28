from quart import send_from_directory

from . import documents_bp


@documents_bp.route("/documents/<path:path>")
async def _index(path: str):
    return await send_from_directory("documents", path)
