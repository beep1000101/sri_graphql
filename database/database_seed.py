from pathlib import Path
from typing import Final

import pandas as pd

from database.models.base import Base
from database.models.ninja import Ninja
from database.models.village import Village
from database.models.enums import KekkeiGenkai, NinjaRank

from database.database_init import get_engine_and_session

DATA_PATH: Final[Path] = (
    Path(__file__).parents[1] / 'database' / 'data' / 'seed_data'
)


def create_tables(bind):
    """
    Create all tables defined on Base.metadata.

    Parameters
    ----------
    bind : Engine or Connection
        The database bind to use.
    """
    Base.metadata.create_all(bind)


def seed_data_from_csvs(session=None):
    """
    Seed the database with data from CSV files.
    """
    ninjas_df = pd.read_csv(DATA_PATH / 'ninjas.csv', index_col=0)
    # cast kekkei_genkai to KekkeiGenkai enum
    ninjas_df['kekkei_genkai'] = (
        ninjas_df['kekkei_genkai']
        .fillna(KekkeiGenkai.NONE)
        .map(KekkeiGenkai)
    )
    # cast rank to NinjaRank enum
    ninjas_df['rank'] = (
        ninjas_df['rank']
        .fillna(NinjaRank.GENIN)
        .map(NinjaRank)
    )
    ninjas_df = ninjas_df.fillna('')

    villages_df = pd.read_csv(DATA_PATH / 'villages.csv', index_col=0)
    ninjas = [Ninja(**row.to_dict()) for _, row in ninjas_df.iterrows()]
    villages = [Village(**row.to_dict()) for _, row in villages_df.iterrows()]
    session.bulk_save_objects(ninjas)
    session.bulk_save_objects(villages)
    session.commit()


if __name__ == "__main__":
    engine, SessionLocal = get_engine_and_session()
    create_tables(engine)
    session = SessionLocal()
    seed_data_from_csvs(session=session)
