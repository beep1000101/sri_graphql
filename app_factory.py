from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_name):
    """
    Create and configure the Flask application.

    This function initializes the Flask app, sets up the database and
    Marshmallow, and registers the API routes.

    Parameters
    ----------
    config_name : str
        The configuration object to use for the Flask app.

    Returns
    -------
    Flask
        The configured Flask application instance.
    """
    # import routes
    # import error handlers
    # from flask_app.routes.errors import register_error_handlers
    from graphql_api.base import graphql_base_blueprint
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)

    # register the routes
    app.register_blueprint(graphql_base_blueprint)
    # register the error handlers
    # register_error_handlers(app=app)

    return app
