import logging

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from enum import StrEnum


db = SQLAlchemy()


class AnsiColor(StrEnum):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


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
    from graphql_api.base import graphql_base_blueprint
    from graphql_api.examples import examples_blueprint
    app = Flask(__name__)

    # Set the logging level to INFO
    app.logger.setLevel(logging.INFO)

    app.config.from_object(config_name)
    db.init_app(app)

    # register the routes
    app.register_blueprint(graphql_base_blueprint)
    app.register_blueprint(examples_blueprint)
    graphql_playground_location = f'http://{config_name.HOST}:{config_name.PORT}/{graphql_base_blueprint.url_prefix}'
    app.logger.info(
        f"{AnsiColor.BOLD}{AnsiColor.CYAN} GraphQL playground:{AnsiColor.RESET} {AnsiColor.YELLOW}{graphql_playground_location}{AnsiColor.RESET}"
    )
    graphql_queries_location = f'http://{config_name.HOST}:{config_name.PORT}/{examples_blueprint.url_prefix}'
    app.logger.info(
        f"{AnsiColor.BOLD}{AnsiColor.CYAN} GraphQL examples:{AnsiColor.RESET}   {AnsiColor.YELLOW}{graphql_queries_location}{AnsiColor.RESET}"
    )

    @app.route('/')
    def hello_world():
        """
        Return a welcome page with full links to GraphQL playground and examples.
        """
        base_url = request.host_url.rstrip('/')
        graphql_url = f"{base_url}/{graphql_base_blueprint.url_prefix}"
        examples_url = f"{base_url}/{examples_blueprint.url_prefix}"

        return f"""
        <html>
            <head><title>Welcome</title></head>
            <body>
                <h1>Hello to the GraphQL Ninja world!</h1>
                <p><a href="{graphql_url}"> Playground</a></p>
                <p><a href="{examples_url}"> Examples</a></p>
            </body>
        </html>
        """, 200

    return app
