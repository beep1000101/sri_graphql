from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.models.base import Base


class Village(Base):
    __tablename__ = 'villages'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    leader_name: Mapped[str] = mapped_column(String(50), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self):
        return f'<Village {self.name}>'
