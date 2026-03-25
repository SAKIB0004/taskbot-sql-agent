import sqlite3
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def reset_tasks_table() -> None:
    conn = sqlite3.connect("data/my_tasks.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks;")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='tasks';")

    conn.commit()
    conn.close()

    logger.info("Tasks table cleared and ID sequence reset.")