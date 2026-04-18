# RojakAI CLI 🤖

**RojakAI CLI** is a powerful, local-first coding assistant designed to help developers build, debug, and understand codebases. It combines the flexibility of local LLMs with robust orchestration and data retrieval strategies.

The name "Rojak" (a traditional Southeast Asian salad) reflects the project's philosophy: a harmonious blend of diverse tools and technologies—Ollama, Temporal, LlamaIndex, Qdrant, and more—working together to provide a seamless developer experience.

## 🚀 Key Features

-   **Local LLM Integration:** Uses [Ollama](https://ollama.com/) for high-performance, private, and local inference.
-   **Advanced RAG (Retrieval-Augmented Generation):** Deep codebase understanding using [LlamaIndex](https://www.llamaindex.ai/) and [Qdrant](https://qdrant.tech/) vector storage.
-   **Reliable Workflows:** Uses [Temporal.io](https://temporal.io/) to manage long-running, resilient tasks like project indexing and automated code repair.
-   **Model Context Protocol (MCP):** A standardized way for the agent to interact with tools (Git, File System, Terminal, etc.).
-   **Persistent Memory:** State management across sessions using PostgreSQL (for history) and Redis (for caching).
-   **Object Storage:** Minio-powered storage for large artifacts and indexed chunks.
-   **Modern CLI UI:** A beautiful and responsive terminal interface built with [Rich](https://github.com/Textualize/rich) and [Typer](https://typer.tiangolo.com/).

## 🏗️ Architecture

RojakAI is built with a modular architecture:

-   **`app/core`**: The brain of the agent, including the planner, thinker, and reflector.
-   **`app/llm`**: Communication layer with Ollama and prompt building.
-   **`app/rag`**: Indexing and retrieval logic using LlamaIndex.
-   **`app/mcp`**: Implementation of various tools (Model Context Protocol).
-   **`app/temporal`**: Durable execution of complex workflows.
-   **`app/storage`**: Integration with Postgres, Redis, and Minio.

## 🛠️ Tech Stack

-   **Language:** Python 3.13+
-   **LLM:** Ollama
-   **Orchestration:** Temporal.io
-   **Database:** PostgreSQL, Redis
-   **Vector Search:** Qdrant
-   **RAG Framework:** LlamaIndex
-   **CLI Framework:** Typer, Rich

## 🏁 Getting Started

### Prerequisites

-   [Docker & Docker Compose](https://www.docker.com/products/docker-desktop/)
-   [Python 3.13+](https://www.python.org/downloads/)
-   [Poetry](https://python-poetry.org/docs/#installation)
-   [Ollama](https://ollama.com/) (running and accessible)

### 1. Clone and Install

```bash
git clone https://github.com/lqmnwido/RojakAICLI.git
cd RojakAICLI
poetry install
```

### 2. Infrastructure Setup

Spin up the required services (Postgres, Redis, Minio, Qdrant, Temporal):

```bash
docker-compose up -d
```

You can access the **Temporal UI** at `http://localhost:8088` to monitor your workflows.

### 3. Environment Configuration

Create a `.env` file in the root directory:

```env
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3
OLLAMA_EMBED_MODEL=nomic-embed-text

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=agent
POSTGRES_USER=agent_user
POSTGRES_PASSWORD=P@ssw0rd2026

REDIS_HOST=localhost
REDIS_PORT=6379

QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=rojak_code

MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET=rojak-assets

TEMPORAL_HOST=localhost:7233
TEMPORAL_NAMESPACE=default

PROJECT_ROOT=.
LOG_PATH=logs/agent.log
CACHE_PATH=cache/
```

### 4. Usage

The main entry point is the `agent` command:

-   **Index a project:**
    ```bash
    poetry run agent index ./path-to-your-project
    ```
-   **Ask a specific question:**
    ```bash
    poetry run agent ask "How does the indexing workflow work?"
    ```
-   **Start interactive chat:**
    ```bash
    poetry run agent chat
    ```

## 📜 License

This project is licensed under the terms provided in the repository.

---
Built with ❤️ by [lqmnwido](https://github.com/lqmnwido)
