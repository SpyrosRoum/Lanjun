from os import getenv

from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = getenv("JWT_SECRET", "pass")

DATABASE_URL = getenv("DATABASE_URL", "")

LOGGING_LEVEL = getenv("LOGGING_LEVEL", "INFO")
