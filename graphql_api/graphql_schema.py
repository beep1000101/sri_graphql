from pathlib import Path

from ariadne import make_executable_schema
from ariadne import (
    load_schema_from_path,
    ObjectType
)

from graphql_api.resolvers.query import query
from graphql_api.resolvers.mutation import mutation

root_path = Path(__file__).parents[1]
schema_path = root_path / "graphql"
type_defs = load_schema_from_path(schema_path)

ninja = ObjectType("Ninja")
village = ObjectType("Village")


schema = make_executable_schema(
    type_defs, [query, mutation, ninja, village])
