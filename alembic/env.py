import os
import sys
from logging.config import fileConfig
from os.path import dirname, abspath

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from alembic import context

# Load environment variables
load_dotenv('.env.local')
load_dotenv()

# 1. Add project root to Python path (critical fix)
project_root = dirname(dirname(abspath(__file__)))
sys.path.insert(0, project_root)

# 2. Import Base - simplified approach
try:
    # Direct import from config.py in project root
    from config import Base
except ImportError as e:
    raise ImportError(
        f"Failed to import Base from config.py. "
        f"Current directory: {os.getcwd()}\n"
        f"Python path: {sys.path}\n"
        f"Is config.py in {project_root}?"
    ) from e

# Alembic config setup
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata
target_metadata = Base.metadata

# Get DB URL from environment
def get_database_url():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("DATABASE_URL must be set in environment variables")
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
            compare_type=True,
            compare_server_default=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
