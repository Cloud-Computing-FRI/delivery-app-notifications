"""Port for storing and listing notifications; implemented in the outer ring."""
from abc import ABC, abstractmethod

from .entities import Notification


class NotificationRepository(ABC):
    @abstractmethod
    def add(self, order_id: int, message: str, sent_at: str) -> Notification:
        ...

    @abstractmethod
    def list(self) -> list[Notification]:
        ...
