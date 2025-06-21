from sqlalchemy import Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

from database.models.enums import NinjaRank, KekkeiGenkai
from database.models.village import Village

from database.models.base import Base


class Ninja(Base):
    __tablename__ = 'ninjas'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    nickname: Mapped[str | None] = mapped_column(String(50), nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    rank: Mapped[NinjaRank] = mapped_column(
        Enum(NinjaRank),
        nullable=False,
        default=NinjaRank.GENIN
    )
    kekkei_genkai: Mapped[KekkeiGenkai] = mapped_column(
        Enum(KekkeiGenkai),
        nullable=False,
        default=KekkeiGenkai.NONE
    )
    is_cool: Mapped[bool] = mapped_column(Boolean, default=False)
    village_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("villages.id"),
        nullable=False
    )

    village: Mapped[Village] = relationship('Village', backref='ninjas')

    def __repr__(self):
        return f'<Ninja {self.name}>'
