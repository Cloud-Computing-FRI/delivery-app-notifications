"""Use case: record a notification and log that it was sent.

The timestamp is a business fact decided here; id generation is left to the
repository (a storage concern).
"""
from datetime import datetime, timezone

from domain.entities import Notification
from domain.ports import NotificationRepository


class CreateNotification:
    def __init__(self, repository: NotificationRepository):
        self._repository = repository

    def __call__(self, order_id: int, message: str) -> Notification:
        sent_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        notification = self._repository.add(order_id, message, sent_at)
        print(f"Notification sent: {message}", flush=True)
        return notification
