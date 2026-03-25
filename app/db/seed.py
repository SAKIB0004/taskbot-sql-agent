import sqlite3
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


def seed_tasks() -> None:
    conn = sqlite3.connect("data/my_tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks;")
    count = cursor.fetchone()[0]

    if count > 0:
        logger.info("Seed skipped. Tasks already exist.")
        conn.close()
        return

    cursor.executemany(
        """
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
        """,
        [
            ("Prepare project report", "Complete the final report for TaskBot project", "pending"),
            ("Revise SQL concepts", "Practice joins, group by, and subqueries", "in_progress"),
            ("Submit internship application", "Apply before deadline", "completed"),
        ]
    )

    conn.commit()
    conn.close()

    logger.info("Seed data inserted successfully.")