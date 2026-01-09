from sqlmodel import SQLModel, Session, create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get DATABASE_URL from environment or default to SQLite
# Note: On Vercel, the filesystem is read-only. We use /tmp for SQLite if no external DB is provided.
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    if os.getenv("VERCEL"):
        DATABASE_URL = "sqlite:////tmp/database.db"
    else:
        DATABASE_URL = "sqlite:///./database.db"

# Create engine with appropriate settings
if DATABASE_URL.startswith("sqlite"):
    # SQLite settings
    engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
else:
    # PostgreSQL/Neon DB settings
    engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
