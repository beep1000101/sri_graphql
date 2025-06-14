from pathlib import Path
from flask import Flask, request, jsonify
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    QueryType,
    MutationType,
    ObjectType,
)
from ariadne.explorer import ExplorerGraphiQL

explorer_html = ExplorerGraphiQL().html(None)

root_path = Path(__file__).parent
schema_path = root_path / "schemas"
type_defs = load_schema_from_path(schema_path)

query = QueryType()
mutation = MutationType()
ninja = ObjectType("Ninja")
village = ObjectType("Village")


@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"


schema = make_executable_schema(type_defs, [query, mutation, ninja, village])

app = Flask(__name__)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=True
    )
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
