from enum import StrEnum


class NinjaRank(StrEnum):
    GENIN = 'Genin'
    CHUNIN = 'Chunin'
    JONIN = 'Jonin'
    SANNIN = 'Sannin'
    KAGE = 'Kage'


class KekkeiGenkai(StrEnum):
    NONE = 'None'
    BYAKUGAN = 'Byakugan'
    SHARINGAN = 'Sharingan'
    RINNEGAN = 'Rinnegan'
