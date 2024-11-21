from sqlalchemy import create_engine
from src.config.settings import AZURE_DB_PW_DEV, AZURE_DB_UID
from .base import Base


from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError


# TODO: This seems a bit hard-coded, but couldn't get it to work otherwise
# with the dependent columns
def init_db(engine) -> None:
    """Initialize the database with schema and tables."""
    try:
        with engine.connect() as conn:
            with conn.begin():
                conn.execute(text("CREATE SCHEMA IF NOT EXISTS storm;"))
    except ProgrammingError:
        pass

    Base.metadata.create_all(engine)


def drop_all(engine) -> None:
    """Drop all tables and schema."""
    with engine.connect() as conn:
        with conn.begin():
            conn.execute(text("DROP SCHEMA IF EXISTS storm CASCADE;"))


def get_engine(mode="dev"):
    """Get a database engine instance."""
    return create_engine(
        f"postgresql+psycopg2://{AZURE_DB_UID}:{AZURE_DB_PW_DEV}@chd-rasterstats-dev.postgres.database.azure.com/postgres"  # noqa: E501
    )
