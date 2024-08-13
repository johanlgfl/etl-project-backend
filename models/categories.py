from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

categories = Table(
    "categories",
    meta,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("name", String(255), nullable=False),
    Column("description", String(255), nullable=False),
    Column("active", Boolean, default=True, nullable=False),
)

meta.create_all(engine)
