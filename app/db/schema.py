from app.db.connection import get_database
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def init_db() -> None:
    db = get_database()

    db.run(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT CHECK(status IN ('pending', 'in_progress', 'completed')) DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    )

    logger.info("Database initialized successfully.")