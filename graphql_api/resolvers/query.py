from ariadne import QueryType, ObjectType
from database.models.ninja import Ninja
from database.models.village import Village
from app_factory import db
from graphql_api.errors.decorators import catch_db_errors, require_positive_id
from graphql_api.errors.api_errors import APIError

query = QueryType()
village = ObjectType("Village")


@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"


@query.field("ninja")
@catch_db_errors
@require_positive_id(arg_name="id")
def resolve_ninja(_, info, id):
    ninja = db.session.query(Ninja).filter(Ninja.id == id).first()
    if not ninja:
        raise APIError("Ninja not found", code="NOT_FOUND", status_code=404)
    return ninja


@query.field("ninjas")
def resolve_ninjas(_, info):
    return db.session.query(Ninja).all()


@query.field("village")
@catch_db_errors
@require_positive_id(arg_name="id")
def resolve_village(_, info, id):
    village = db.session.query(Village).filter(Village.id == id).first()
    if not village:
        raise APIError("Village not found", code="NOT_FOUND", status_code=404)
    return village


@query.field("villages")
@catch_db_errors
def resolve_villages(_, info):
    return db.session.query(Village).all()


@village.field("ninjas")
@catch_db_errors
def resolve_village_ninjas(obj, info):
    return obj.ninjas
