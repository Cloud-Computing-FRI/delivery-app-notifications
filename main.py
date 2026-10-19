"""Composition root for the notifications service.

Reads configuration, picks the persistence adapter (PostgreSQL when
DATABASE_URL is set, otherwise in-memory), injects it into the use cases and
exposes `app` for `uvicorn main:app`.
"""
import os

from fastapi import FastAPI

from adapters.repositories import (
    InMemoryNotificationRepository,
    PostgresNotificationRepository,
)
from domain.ports import NotificationRepository
from usecases.create_notification import CreateNotification
from usecases.list_notifications import ListNotifications
from web.api import create_router


def build_repository() -> NotificationRepository:
    dsn = os.getenv("DATABASE_URL")
    if dsn:
        return PostgresNotificationRepository(dsn)
    return InMemoryNotificationRepository()


def create_app() -> FastAPI:
    repository = build_repository()
    app = FastAPI(title="Notifications service")
    app.include_router(
        create_router(CreateNotification(repository), ListNotifications(repository))
    )
    return app


app = create_app()
