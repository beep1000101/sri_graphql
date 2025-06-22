from sqlalchemy import Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import validates

from database.models.enums import NinjaRank, KekkeiGenkai
from database.models.village import Village

from database.models.base import Base


class Ninja(Base):
    __tablename__ = 'ninjas'
    __STRING_LENGTH: int = 50

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(__STRING_LENGTH), nullable=False)
    nickname: Mapped[str | None] = mapped_column(
        String(__STRING_LENGTH), nullable=True)
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

    village_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey("villages.id", ondelete="SET NULL"),
        nullable=True,
    )

    village: Mapped["Village"] = relationship(
        "Village",
        back_populates="ninjas",
        passive_deletes=True,
    )

    def __repr__(self):
        return f'<Ninja {self.name}>'

    @validates('id')
    def validate_id(self, key, value):
        try:
            value = int(value)
            if value < 0:
                raise ValueError("ID must be a non-negative integer.")
            return value
        except TypeError:
            raise ValueError("ID must be an integer.")
        except ValueError as e:
            raise e

    @validates('age')
    def validate_age(self, key, value):
        try:
            if value < 0:
                raise ValueError("Age must be a non-negative integer.")
            if value > 1.3e10:
                raise ValueError(
                    "Age is too large."
                    " In the world of Ninjas we don't allow anyone to be older than the assumed age of the Universe."
                )
            return value
        except TypeError:
            raise TypeError("Age must be an integer.")
        except ValueError as e:
            raise e

    @validates('rank')
    def validate_rank(self, key, value):
        if not isinstance(value, NinjaRank):
            raise ValueError(
                "Rank must be an instance of NinjaRank Enum."
            )
        return value

    @validates('kekkei_genkai')
    def validate_kekkei_genkai(self, key, value):
        if not isinstance(value, KekkeiGenkai):
            raise ValueError(
                "Kekkei Genkai must be an instance of KekkeiGenkai Enum."
            )
        return value

    @validates('is_cool')
    def validate_is_cool(self, key, value):
        if not isinstance(value, bool):
            raise ValueError("is_cool must be a boolean value.")
        return value

    @validates('village_id')
    def validate_village_id(self, key, value):
        if value is None:
            return None
        try:
            if value < 0:
                raise ValueError("Village ID must be a non-negative integer.")
            return value
        except TypeError:
            raise ValueError("Village ID must be an integer.")
        except ValueError as e:
            raise e

    @validates('name')
    def validate_name_fields(self, key, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key} must be a non-empty string.")
        if len(value) > self.__STRING_LENGTH:
            raise ValueError(f"{key} cannot exceed 50 characters.")
        return value.strip() if value else value

    @validates('nickname')
    def validate_nickname_fields(self, key, value):
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string.")
        if len(value) > self.__STRING_LENGTH:
            raise ValueError(f"{key} cannot exceed 50 characters.")
        return value.strip() if value else value
