from ariadne import QueryType, ObjectType
from database.models.ninja import Ninja
from database.models.village import Village
from app_factory import db

query = QueryType()
village = ObjectType("Village")


@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"


@query.field("ninja")
def resolve_ninja(_, info, id):
    return db.session.query(Ninja).filter(Ninja.id == id).first()


@query.field("ninjas")
def resolve_ninjas(_, info):
    return db.session.query(Ninja).all()


@query.field("village")
def resolve_village(_, info, id):
    return db.session.query(Village).filter(Village.id == id).first()


@query.field("villages")
def resolve_villages(_, info):
    return db.session.query(Village).all()


@village.field("ninjas")
def resolve_village_ninjas(obj: Village, info):
    return obj.ninjas
