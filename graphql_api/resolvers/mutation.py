from typing import Optional

from ariadne import MutationType
from database.models.ninja import Ninja
from database.models.ninja import Ninja
from app_factory import db

from database.models.enums import NinjaRank, KekkeiGenkai

mutation = MutationType()


@mutation.field("createNinja")
def resolve_create_ninja(
        _,
        info,
        name: str,
        age: int,
        village_id: int,
        rank: NinjaRank = NinjaRank.GENIN,
        kekkei_genkai: KekkeiGenkai = KekkeiGenkai.NONE,
        is_cool: bool = False,
        nickname: str = ''
):
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
def resolve_update_ninja(
        _,
        info,
        id: int,
        name: Optional[str] = None,
        age: Optional[int] = None,
        village_id: Optional[int] = None,
        rank: Optional[NinjaRank] = None,
        kekkei_genkai: Optional[KekkeiGenkai] = None,
        is_cool: Optional[bool] = None,
        nickname: Optional[str] = None
):
    ninja = (
        db.session
        .query(Ninja)
        .filter(Ninja.id == id)
        .first()
    )

    if not ninja:
        return None

    if name is not None:
        ninja.name = name
    if age is not None:
        ninja.age = age
    if village_id is not None:
        ninja.village_id = village_id
    if rank is not None:
        ninja.rank = rank
    if kekkei_genkai is not None:
        ninja.kekkei_genkai = kekkei_genkai
    if is_cool is not None:
        ninja.is_cool = is_cool
    if nickname is not None:
        ninja.nickname = nickname

    db.session.commit()
    return ninja
