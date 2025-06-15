import os
import sys
from logging.config import fileConfig
from os.path import dirname, abspath

from dotenv import load_dotenv

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Load environment variables from .env.local first, then .env
load_dotenv('.env.local')
load_dotenv()  # Fallback to .env if variable not in .env.local

# 1. Add your PROJECT ROOT to Python path
project_root = dirname(dirname(abspath(__file__)))
sys.path.insert(0, project_root)

# 2. Now try importing - use absolute import path
try:
    # First try absolute import (if your project is a package)
    from fastapi_learning_series.config import Base
except ImportError:
    try:
        # Fallback to direct config import
        from config import Base
    except ImportError as e:
        raise ImportError(
            f"Cannot import Base. sys.path: {sys.path}\n"
            f"Current dir: {os.getcwd()}\n"
            f"Project root: {project_root}"
        ) from e

# This is the Alembic Config object
config = context.config

# Set up Python loggers
fileConfig(config.config_file_name)

# Import your SQLAlchemy Base and models here
# This should match where your Base is defined in your project
# Example: from app.db.base import Base
# Or if using the config.py we discussed earlier:
target_metadata = Base.metadata

# Set the database URL from environment variables
def get_database_url():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL not found in environment variables")
    return db_url

config.set_main_option('sqlalchemy.url', get_database_url())

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Good for detecting column type changes
            compare_server_default=True,  # Detect default value changes
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
