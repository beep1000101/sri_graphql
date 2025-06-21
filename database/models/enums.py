from enum import StrEnum


class NinjaRank(StrEnum):
    """
    Enumeration for the ranks of ninjas in the Naruto universe.

    The ranks are ordered from lowest to highest:
    - Genin: The lowest rank, typically a young ninja who has just graduated from the Ninja Academy.
    - Chunin: A mid-level ninja who has passed the Chunin Exams and is capable of leading teams.
    - Jonin: A high-ranking ninja who has significant experience and is often a leader of a team of Genin.
    - Sennin: A legendary ninja, often considered among the strongest in the world.
    - Kage: The highest rank, the leader of a ninja village, responsible for the safety and governance of their village.
    """
    GENIN = 'Genin'
    CHUNIN = 'Chunin'
    JONIN = 'Jonin'
    SENNIN = 'Sennin'
    KAGE = 'Kage'


class KekkeiGenkai(StrEnum):
    """
    Enumeration for the Kekkei Genkai abilities in the Naruto universe.
    """
    NONE = 'None'
    BYAKUGAN = 'Byakugan'
    SHARINGAN = 'Sharingan'
    RINNEGAN = 'Rinnegan'
