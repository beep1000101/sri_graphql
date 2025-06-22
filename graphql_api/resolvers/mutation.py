from typing import Optional

from ariadne import MutationType
from database.models.ninja import Ninja
from database.models.village import Village
from database.models.enums import NinjaRank, KekkeiGenkai
from graphql_api.errors.api_errors import APIError
from graphql_api.errors.decorators import catch_db_errors, require_positive_id
from app_factory import db

mutation = MutationType()


@mutation.field("createNinja")
@catch_db_errors
@require_positive_id(arg_name="village_id")
def resolve_create_ninja(
    _,
    info,
    name: str,
    age: int,
    village_id: int,
    rank: NinjaRank = NinjaRank.GENIN,
    kekkei_genkai: KekkeiGenkai = KekkeiGenkai.NONE,
    is_cool: bool = False,
    nickname: str = ""
):
    village = db.session.query(Village).get(village_id)
    if not village:
        raise APIError("Village not found", code="NOT_FOUND", status_code=404)

    ninja = Ninja(
        name=name,
        nickname=nickname,
        age=age,
        rank=rank,
        kekkei_genkai=kekkei_genkai,
        is_cool=is_cool,
        village_id=village_id
    )

    db.session.add(ninja)
    db.session.commit()
    return ninja


@mutation.field("updateNinja")
@catch_db_errors
@require_positive_id(arg_name="id")
def resolve_update_ninja(_, info, id: int, **kwargs):
    ninja = db.session.query(Ninja).get(id)
    if ninja is None:
        raise APIError("Ninja not found", code="NOT_FOUND", status_code=404)

    for field in ["name", "age", "village_id", "rank", "kekkei_genkai", "is_cool", "nickname"]:
        if field in kwargs and kwargs[field] is not None:
            setattr(ninja, field, kwargs[field])

    db.session.commit()
    return ninja


@mutation.field("assignNinjaToVillage")
@catch_db_errors
@require_positive_id(arg_name="ninja_id")
def resolve_assign_ninja_to_village(_, info, ninja_id: int, village_id: int):
    ninja = db.session.query(Ninja).get(ninja_id)
    if not ninja:
        raise APIError("Ninja not found", code="NOT_FOUND", status_code=404)

    village = Village.query.get(village_id)
    if not village:
        raise APIError("Village not found", code="NOT_FOUND", status_code=404)

    ninja.village_id = village.id
    db.session.commit()
    return ninja


@mutation.field("deleteNinja")
@catch_db_errors
@require_positive_id(arg_name="id")
def resolve_delete_ninja(_, info, id: int):
    ninja = db.session.query(Ninja).get(id)
    db.session.delete(ninja)
    db.session.commit()
    return True


@mutation.field("createVillage")
@catch_db_errors
def resolve_create_village(_, info, name: str):
    village = Village(name=name)
    db.session.add(village)
    db.session.commit()
    return village


@mutation.field("updateVillage")
@catch_db_errors
@require_positive_id(arg_name="id")
def resolve_update_village(_, info, id: int, name: Optional[str] = None):
    village = db.session.query(Village).get(id)
    if not village:
        raise APIError("Village not found", code="NOT_FOUND", status_code=404)
    if name is not None:
        village.name = name
    db.session.commit()
    return village


@mutation.field("deleteVillage")
@catch_db_errors
@require_positive_id(arg_name="id")
def resolve_delete_village(_, info, id: int):
    village = Village.query.get(id)
    if not village:
        raise APIError("Village not found", code="NOT_FOUND", status_code=404)
    db.session.delete(village)
    db.session.commit()
    return True
