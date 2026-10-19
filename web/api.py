"""FastAPI delivery mechanism for the notifications service."""
from dataclasses import asdict

from fastapi import APIRouter
from pydantic import BaseModel

from usecases.create_notification import CreateNotification
from usecases.list_notifications import ListNotifications


class NewNotification(BaseModel):
    order_id: int
    message: str


def create_router(create_notification: CreateNotification, list_notifications: ListNotifications) -> APIRouter:
    router = APIRouter()

    @router.get("/health")
    def health():
        return {"status": "ok"}

    @router.get("/notifications")
    def list_all():
        return [asdict(n) for n in list_notifications()]

    @router.post("/notifications", status_code=201)
    def create(new: NewNotification):
        return asdict(create_notification(new.order_id, new.message))

    return router
