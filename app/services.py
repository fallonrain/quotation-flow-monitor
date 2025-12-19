from datetime import datetime, timedelta
from app.database import get_connection


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quotations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL,
            opened_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_quotation(status: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO quotations (status, opened_at) VALUES (?, ?)",
        (status, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()


def get_quotations(status: str | None = None):
    conn = get_connection()
    cursor = conn.cursor()

    if status:
        cursor.execute(
            "SELECT id, status, opened_at FROM quotations WHERE status = ?",
            (status,)
        )
    else:
        cursor.execute(
            "SELECT id, status, opened_at FROM quotations"
        )

    rows = cursor.fetchall()
    conn.close()
    return rows


def get_stale_quotations(sla_hours: int = 24):
    conn = get_connection()
    cursor = conn.cursor()

    limit_time = datetime.now() - timedelta(hours=sla_hours)

    cursor.execute("""
        SELECT id, status, opened_at
        FROM quotations
        WHERE status = 'WAITING_SUPPLIER'
    """)

    rows = cursor.fetchall()
    conn.close()

    stale = []

    for row in rows:
        opened_at = datetime.fromisoformat(row[2])
        if opened_at < limit_time:
            stale.append({
                "id": row[0],
                "status": row[1],
                "opened_at": row[2]
            })

    return stale
