import logging
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
    from graphql_api.examples import examples_blueprint
    app = Flask(__name__)

    # Set the logging level to INFO
    app.logger.setLevel(logging.INFO)

    app.logger.info(f"Creating Flask app with config: {config_name}")
    app.config.from_object(config_name)
    db.init_app(app)
    app.logger.info("Flask app created and configured")

    # register the routes
    app.register_blueprint(graphql_base_blueprint)
    app.logger.info(f"Registered blueprint: {graphql_base_blueprint.name}")
    app.register_blueprint(examples_blueprint)
    app.logger.info(f"Registered blueprint: {examples_blueprint.name}")
    graphql_playground_location = f'http://{config_name.host}:{config_name.port}/{graphql_base_blueprint.url_prefix}'
    app.logger.info(
        f"GraphQL playground available at: {graphql_playground_location}"
    )
    graphql_queries_location = f'http://{config_name.host}:{config_name.port}/{examples_blueprint.url_prefix}'
    app.logger.info(
        f"GraphQL examples available at: {graphql_queries_location}"
    )

    return app
