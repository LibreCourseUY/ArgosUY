from dbwarden import database_config

database_config(
    database_name="primary",
    default=True,
    database_type="clickhouse",
    database_url="sqlite:///./app.db",
    migrations_dir="migrations/clickhouse",
)
