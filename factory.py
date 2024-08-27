from quart import Quart


def create_app() -> Quart:
    app = Quart(__name__, static_url_path="/assets", static_folder="assets")
    app.config.from_pyfile("config.py")

    from blueprints.index import index_bp

    app.register_blueprint(index_bp)

    return app
