import logging

from flask import Flask, json
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import BadRequest
from werkzeug.wrappers import Response

import core.settings as config
from app.products.routes import init_product_routes
from app.users.routes import init_auth_routes
from core.commands import create_dummy_users_command
from core.error_handlers import AppError
from core.resources.database import db


def build_db(app):
    db.init_app(app)
    return db


def routes(app):
    api = Api(app)
    init_auth_routes(api)
    init_product_routes(api)


def build_application():
    app = Flask(__name__)
    # load flask config from settings
    for k in dir(config):
        v = getattr(config, k)
        if not k.startswith("_") and k.upper() == k and not callable(v):
            app.config[k] = v

    # set logging based on unicorn level
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    if __name__ != "main":
        app.logger.setLevel(gunicorn_logger.level)
    else:
        app.logger.setLevel(logging.DEBUG)
    app.logger.info("Logger Configured w/level {}".format(app.logger.level))

    app.db = build_db(app)
    CORS(app)
    JWTManager(app)

    Migrate(app, app.db)
    routes(app)
    return app


# =============================================================================

app = build_application()

# =============================================================================
@app.errorhandler(AppError)
def handle_exception(error):
    payload = {"success": error.success, "data": error.data}
    if getattr(error, "message", None):
        payload["message"] = error.message

    response = Response()

    response.data = json.dumps(payload)
    response.content_type = "application/json"
    response.status_code = error.code
    return response


@app.errorhandler(ValidationError)
def schema_validation_error(error):
    payload = {
        "success": False,
        "message": "Validation Error",
        "errors": error.messages,
    }
    response = Response()
    response.content_type = "application/json"
    response.data = json.dumps(payload)
    response.status_code = BadRequest.code
    app.logger.error(error)
    return response


# =============================================================================
@app.cli.command()
def create_dummy_users():
    """Run script to create dummy users"""
    create_dummy_users_command()
