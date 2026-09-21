from dotenv import load_dotenv
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
dotenv_path = os.path.join(PROJECT_ROOT, ".env")
load_dotenv(dotenv_path)

CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER", "argosuy")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "argosuy")
CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT", "8123")
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "localhost")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "ghp_...")

LOG_LEVEL = os.getenv("LOG_LEVEL", "info")