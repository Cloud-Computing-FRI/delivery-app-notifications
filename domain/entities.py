"""Domain entity: a notification sent to a customer. No framework imports."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Notification:
    id: int
    order_id: int
    message: str
    sent_at: str
