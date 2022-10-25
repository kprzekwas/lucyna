from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_settings import settings


def get_db_url():
    database = (
        f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}"
        f"@{settings.DATABASE_HOST}:5432/{settings.DATABASE_NAME}"
    )
    return database


engine = create_engine(get_db_url(), echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
