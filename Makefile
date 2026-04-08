.DEFAULT_GOAL := help

.PHONY: help dev build down logs ps shell-api shell-db shell-frontend

help:
	@echo ""
	@echo "  make dev              Start all services with hot reload"
	@echo "  make build            Rebuild all images"
	@echo "  make down             Stop and remove containers"
	@echo "  make logs             Tail logs from all services"
	@echo "  make ps               Show running containers"
	@echo "  make shell-api        Open shell inside the API container"
	@echo "  make shell-frontend   Open shell inside the frontend container"
	@echo "  make shell-db         Open psql inside the DB container"
	@echo ""
	@echo "  Ports configured in .env:"
	@echo "    API_PORT=8100  FRONTEND_PORT=5173  DB_PORT=5433"
	@echo ""

dev:
	docker compose up

build:
	docker compose build --no-cache

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps

shell-api:
	docker compose exec api sh

shell-frontend:
	docker compose exec frontend sh

shell-db:
	docker compose exec db psql -U portfolio -d portfolio
