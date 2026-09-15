import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables from .env if present
load_dotenv()

# Fetch DATABASE_URL from environment or fallback to SQLite for easy local inspection
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./smartcart.db")

# Render and older Heroku PostgreSQL instances provide URLs starting with postgres://
# SQLAlchemy 1.4+ and 2.0+ require postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configure connection args based on dialect
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    # PostgreSQL production settings
    connect_args = {
        "sslmode": os.getenv("DB_SSLMODE", "prefer")
    }

# Create SQLAlchemy engine with pool pre-ping to handle stale hosted connections
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args if DATABASE_URL.startswith("sqlite") else {},
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    FastAPI dependency that provides a database session per request
    and ensures proper teardown.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
