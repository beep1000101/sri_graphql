from flask import request, jsonify, Blueprint

from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL

from graphql_api.graphql_schema import schema

explorer_html = ExplorerGraphiQL().html(None)

graphql_base_blueprint = Blueprint('graphql_base', __name__)


@graphql_base_blueprint.get("/graphql")
def graphql_playground():
    return explorer_html, 200


@graphql_base_blueprint.post("/graphql")
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=True
    )
    return jsonify(result)
