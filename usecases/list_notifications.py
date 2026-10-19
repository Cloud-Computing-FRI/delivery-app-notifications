"""Use case: list recorded notifications."""
from domain.entities import Notification
from domain.ports import NotificationRepository


class ListNotifications:
    def __init__(self, repository: NotificationRepository):
        self._repository = repository

    def __call__(self) -> list[Notification]:
        return self._repository.list()
