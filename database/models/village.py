from sqlalchemy import Integer, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, validates

from database.models.base import Base


class Village(Base):
    __tablename__ = 'villages'
    __table_args__ = (
        CheckConstraint('population >= 0',
                        name='ck_village_population_non_negative'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    leader_name: Mapped[str] = mapped_column(String(50), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f'<Village {self.name}>'

    @validates('name')
    def validate_name(self, key, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Name must be a non-empty string.')
        return value.strip()

    @validates('leader_name')
    def validate_leader_name(self, key, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Leader name must be a non-empty string.')
        return value.strip()

    @validates('population')
    def validate_population(self, key, value):
        if not isinstance(value, int):
            raise TypeError('Population must be an integer.')
        if value < 0:
            raise ValueError('Population must be non-negative.')
        return value
