# HD Tech — Portfolio SaaS

Plataforma de portfólio profissional com formulário de contato, solicitação de orçamento e agendamento de chamadas.

---

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.11 · FastAPI 0.111 · Pydantic v2 |
| Frontend | Vue 3 · Vue Router 4 · Vite 5 |
| Banco de dados | PostgreSQL 16 (provisionado, integração em breve) |
| Infraestrutura | Docker · Docker Compose |

---

## Funcionalidades

- **Formulário de contato** — nome, e-mail e mensagem com validação completa
- **Solicitação de orçamento** — tipo de projeto, descrição, valor e prazo
- **Agendamento de chamada** — link direto para o Calendly configurável via variável de ambiente

---

## Arquitetura

```
portfolio/
├── backend/                  # API FastAPI
│   └── app/
│       ├── core/             # Config, logging, tratamento de erros
│       ├── repositories/     # Camada de acesso a dados (pronta para PostgreSQL)
│       ├── routes/           # Endpoints HTTP
│       ├── schemas/          # Modelos Pydantic (request/response)
│       ├── services/         # Regras de negócio
│       └── models/           # Modelos SQLAlchemy (a implementar)
├── frontend/                 # SPA Vue 3
│   └── src/
│       ├── api/              # Funções de chamada HTTP (fetch wrapper)
│       ├── composables/      # useForm — estado de loading/erro/sucesso
│       ├── router/           # Rotas da aplicação
│       └── views/            # Páginas: Contact, Budget, Schedule
├── docker-compose.yml
└── Makefile
```

### Padrões aplicados no backend

- **Repository pattern** — `BaseRepository[T]` genérico desacopla serviços do armazenamento. Trocar in-memory por PostgreSQL exige mudança apenas na camada de repositório, sem alterar rotas nem serviços.
- **Dependency injection** — repositórios injetados nas rotas via `Depends()` do FastAPI.
- **Schemas separados** — `Request` e `Response` distintos em cada feature.
- **Logging estruturado** — timestamps e contexto em todos os logs, sem `print()`.
- **Tratamento de erros customizado** — respostas de erro padronizadas em `{"error": ..., "details": [...]}`.

---

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e Docker Compose v2
- Git

> **Não é necessário ter Python ou Node instalados localmente.** Tudo roda dentro dos containers.

---

## Como rodar

### 1. Clone o repositório

```bash
git clone https://github.com/henriquediasjr/hd-tech.git
cd hd-tech
```

### 2. Configure as variáveis de ambiente

```bash
# Portas do Docker Compose (ajuste se houver conflito na sua máquina)
cp .env.example .env

# Configurações da API
cp backend/.env.example backend/.env
```

Edite `backend/.env` com seus valores:

```env
CALENDLY_URL=https://calendly.com/seu-usuario   # seu link real do Calendly
```

### 3. Suba o projeto

```bash
make dev
```

Isso inicia três containers:

| Container | Endereço local |
|---|---|
| API (FastAPI) | http://localhost:8100 |
| Frontend (Vue) | http://localhost:5173 |
| PostgreSQL | localhost:5433 |

> As portas padrão podem ser alteradas no arquivo `.env` da raiz.

### 4. Acesse

| URL | Descrição |
|---|---|
| http://localhost:5173 | Aplicação frontend |
| http://localhost:8100/docs | Documentação interativa da API (Swagger) |
| http://localhost:8100/health | Health check da API |

---

## Variáveis de ambiente

### Raiz (`.env`) — portas do Docker Compose

| Variável | Padrão | Descrição |
|---|---|---|
| `API_PORT` | `8100` | Porta do host para a API |
| `FRONTEND_PORT` | `5173` | Porta do host para o frontend |
| `DB_PORT` | `5433` | Porta do host para o PostgreSQL |

### Backend (`backend/.env`)

| Variável | Padrão | Descrição |
|---|---|---|
| `APP_ENV` | `development` | Ambiente da aplicação |
| `APP_TITLE` | `Portfolio API` | Nome exibido no Swagger |
| `APP_VERSION` | `0.1.0` | Versão da API |
| `CORS_ORIGINS` | `["http://localhost:5173"]` | Origens permitidas pelo CORS |
| `CALENDLY_URL` | — | URL do seu Calendly |
| `DATABASE_URL` | — | URL do PostgreSQL (comentada até a integração) |

---

## Endpoints da API

### Contato
```
POST /api/contact/    Envia mensagem de contato
GET  /api/contact/    Lista todas as mensagens recebidas
```

### Orçamento
```
POST /api/budget/     Solicita orçamento de projeto
GET  /api/budget/     Lista todas as solicitações
```

### Agendamento
```
GET  /api/schedule/   Retorna URL do Calendly e instrução
```

### Sistema
```
GET  /health          Status da API e ambiente atual
```

---

## Comandos úteis

```bash
make dev            # Inicia todos os serviços com hot reload
make build          # Rebuilda as imagens Docker do zero
make down           # Para e remove os containers
make logs           # Acompanha os logs em tempo real
make ps             # Lista containers em execução
make shell-api      # Abre shell dentro do container da API
make shell-frontend # Abre shell dentro do container do frontend
make shell-db       # Abre psql dentro do container do banco
```

---

## Rodando sem Docker (desenvolvimento local)

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

> Requer Node.js 18+

```bash
cd frontend
npm install
npm run dev
```

> Em desenvolvimento local, ajuste o proxy no `frontend/vite.config.js` para apontar para `http://localhost:8000` em vez de `http://api:8000`.

---

## Próximos passos

- [ ] Integração com PostgreSQL via SQLAlchemy (async)
- [ ] Notificações por e-mail ao receber contato ou orçamento
- [ ] Build de produção do frontend servido pelo Nginx
- [ ] Autenticação de admin para visualizar submissões
- [ ] Deploy (Railway, Render ou VPS próprio)

---

## Licença

Projeto pessoal — todos os direitos reservados.
