"""In-memory and PostgreSQL adapters for the NotificationRepository port.

`psycopg` is imported lazily, only when the PostgreSQL adapter is constructed,
so the in-memory path needs no database driver installed.
"""
from domain.entities import Notification
from domain.ports import NotificationRepository


class InMemoryNotificationRepository(NotificationRepository):
    def __init__(self):
        self._notifications: list[Notification] = []

    def add(self, order_id: int, message: str, sent_at: str) -> Notification:
        notification = Notification(
            id=len(self._notifications) + 1,
            order_id=order_id,
            message=message,
            sent_at=sent_at,
        )
        self._notifications.append(notification)
        return notification

    def list(self) -> list[Notification]:
        return list(self._notifications)


class PostgresNotificationRepository(NotificationRepository):
    def __init__(self, dsn: str):
        import psycopg

        self._psycopg = psycopg
        self._dsn = dsn

    def add(self, order_id: int, message: str, sent_at: str) -> Notification:
        with self._psycopg.connect(self._dsn) as conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO notifications (order_id, message, sent_at) "
                "VALUES (%s, %s, %s) RETURNING id",
                (order_id, message, sent_at),
            )
            new_id = cur.fetchone()[0]
        return Notification(new_id, order_id, message, sent_at)

    def list(self) -> list[Notification]:
        with self._psycopg.connect(self._dsn) as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT id, order_id, message, sent_at FROM notifications ORDER BY id"
            )
            return [Notification(i, o, m, s) for i, o, m, s in cur.fetchall()]
