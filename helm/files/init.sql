-- Schema for the notifications service.
--
-- Each microservice owns its own database. This file runs automatically from
-- /docker-entrypoint-initdb.d on the in-cluster Postgres' first start, against
-- the database named by POSTGRES_DB. For a managed database (prod) run it once
-- against this service's database:
--     psql "<notifications connection string>" -f init.sql

CREATE TABLE notifications (
    id       SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    message  TEXT NOT NULL,
    sent_at  TEXT NOT NULL
);
