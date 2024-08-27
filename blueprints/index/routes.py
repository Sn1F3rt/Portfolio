from quart import render_template

from . import index_bp


@index_bp.route("/")
async def _index():
    return await render_template("index.html")
