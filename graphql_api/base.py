from flask import request, jsonify, Blueprint

from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL

from graphql_api.graphql_schema import schema
from graphql_api.errors.utils import determine_http_status

explorer_html = ExplorerGraphiQL().html(None)

graphql_base_blueprint = Blueprint(
    'graphql_base', __name__, url_prefix='/graphql')


@graphql_base_blueprint.get("")
def graphql_playground():
    return explorer_html, 200


@graphql_base_blueprint.post("")
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=True
    )

    if result.get('errors'):
        status_code = determine_http_status(result)
        return jsonify(result), status_code

    return jsonify(result)
