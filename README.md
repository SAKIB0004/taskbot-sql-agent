# TaskBot SQL Agent

> An AI-powered task management assistant that uses natural language to interact with a SQL database.

---

## Overview

**TaskBot SQL Agent** is a portfolio-ready AI application that enables users to manage tasks through natural language conversations. Instead of writing SQL manually, users can create, read, update, and delete tasks by chatting with an AI assistant backed by a SQLite database.

The project combines **LangChain**, **LangGraph memory**, **Groq-hosted LLMs**, **SQLite**, and **Streamlit** to deliver a lightweight but production-style intelligent task management system.

This repository is designed to demonstrate practical skills in:

* AI agent design
* LLM-tool integration
* SQL-backed conversational systems
* modular Python project architecture
* Streamlit-based application development

---

## Why This Project Matters

Traditional task management systems require fixed forms, rigid interfaces, or manual database operations. This project addresses that limitation by providing a conversational interface that makes database interaction more intuitive.

### Problem Statement

Users often need a simpler way to manage structured task data without directly writing SQL queries or using a complex UI. This project solves that by enabling a natural language workflow such as:

* “Show all tasks”
* “Add a task titled Complete report”
* “Mark task 3 as completed”
* “Delete the task named Learn SQL”

The assistant interprets the user’s request, interacts with the SQL database through tools, and returns structured results.

---

## Features

* Natural language task management
* SQL-powered CRUD operations
* SQLite-backed persistent storage
* AI agent with database tools
* Thread-based conversational memory
* Streamlit chat interface
* Modular project structure for maintainability
* Demo-ready and portfolio-friendly design
* Reset support for tasks table and ID sequence
* Clean separation of UI, services, agent, database, and utilities

---

## Tech Stack

### Core Technologies

* **Python**
* **Streamlit**
* **SQLite**
* **LangChain**
* **LangGraph**
* **Groq LLM API**
* **python-dotenv**
* **pytest**

### Main Libraries

* `streamlit`
* `langchain`
* `langchain-community`
* `langgraph`
* `langchain-groq`
* `sqlalchemy`
* `python-dotenv`
* `pytest`

---

## Architecture / Workflow

The application follows a clean layered architecture:

```text
User
  → Streamlit UI
    → Chat Service
      → AI Agent
        → SQL Toolkit / Tools
          → SQLite Database
```

### High-Level Flow

1. The user enters a task-related query in the Streamlit chat UI.
2. The request is forwarded to the service layer.
3. The service layer invokes the LangChain agent.
4. The agent uses SQL database tools to inspect schema and execute safe SQL operations.
5. The database returns results.
6. The agent formats the response for the user.

### Core Modules

* **UI Layer**: Handles chat interface and session interaction
* **Service Layer**: Orchestrates query processing
* **Agent Layer**: Creates the LLM-powered SQL agent
* **Database Layer**: Manages schema initialization, connection, seed, and reset logic
* **Utility Layer**: Logging and supporting helpers

---

## Project Structure

```text
taskbot-sql-agent/
├── app/
│   ├── main.py
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   ├── schema.py
│   │   └── seed.py
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── llm.py
│   │   ├── toolkit.py
│   │   ├── memory.py
│   │   ├── prompt.py
│   │   └── builder.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── chat_service.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── components.py
│   └── utils/
│       ├── __init__.py
│       └── logger.py
├── data/
├── .env
├── requirements.txt
├── README.md
└── check_db.py
```

---

## Module Breakdown

### `app/main.py`

Streamlit application entrypoint. Initializes the database, handles UI rendering, and connects user input with the chat service.

### `app/config/settings.py`

Loads environment variables and centralizes runtime configuration such as model name, database path, and app title.

### `app/db/`

Contains database-related logic:

* `connection.py`: database connection setup
* `schema.py`: creates the `tasks` table
* `seed.py`: optional demo task insertion

### `app/agent/`

Contains AI-agent-related components:

* `llm.py`: LLM initialization
* `toolkit.py`: SQL tool creation
* `memory.py`: conversational memory setup
* `prompt.py`: system prompt definition
* `builder.py`: agent construction

### `app/services/chat_service.py`

Acts as the bridge between the UI and the AI agent.

### `app/ui/components.py`

Reusable Streamlit UI helpers.

### `app/utils/logger.py`

Logging configuration for debugging and monitoring.

---

## Database Schema

The project uses a `tasks` table with the following schema:

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT CHECK(status IN ('pending', 'in_progress', 'completed')) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Supported Task Status Values

* `pending`
* `in_progress`
* `completed`

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/taskbot-sql-agent.git
cd taskbot-sql-agent
```

### 2. Create and activate a virtual environment

#### Windows (PowerShell)

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=qwen/qwen3-32b
DATABASE_URL=sqlite:///data/my_tasks.db
APP_TITLE=TaskBot - Task Management Agent
DEFAULT_THREAD_ID=taskbot-thread-1
```

---

## Run Instructions

Start the Streamlit app from the project root:

```bash
python -m streamlit run app/main.py
```

---

## Usage

Once the app is running, you can interact with the assistant using natural language.

### Example Prompts

```text
Show all tasks
Add a task titled "Complete report" with description "Finish before Sunday"
Mark task 1 as completed
Show all pending tasks
Delete the task titled "Complete report"
```

### Typical User Actions

* Create a new task
* View the latest tasks
* Update task status
* Delete tasks
* Reset task workflow during testing

---

## System Design Notes

This project is structured like a real-world AI-backed backend application, even though it uses Streamlit for the interface.

### Design Principles

* modular architecture
* separation of concerns
* configuration-driven setup
* reproducible local development
* clear service boundaries
* database-first task persistence

### Agent Design

The agent is built using:

* an LLM from Groq
* LangChain SQL tools
* a controlled system prompt
* memory through LangGraph checkpointer support

The agent does not directly hallucinate task data. It relies on tool access to the database to retrieve and modify information.

---

## Example Output / Results

### Example: listing tasks

| ID | Title                         | Description                                   | Status      | Created At          |
| -- | ----------------------------- | --------------------------------------------- | ----------- | ------------------- |
| 1  | Prepare project report        | Complete the final report for TaskBot project | pending     | 2026-03-25 15:48:23 |
| 2  | Revise SQL concepts           | Practice joins, group by, and subqueries      | in_progress | 2026-03-25 15:48:23 |
| 3  | Submit internship application | Apply before deadline                         | completed   | 2026-03-25 15:48:23 |

### Example: update action

```text
Task 2 has been updated successfully.
Current status: completed
```

### Example: delete action

```text
Task "Complete report" was deleted successfully.
```

---

## Screenshots / Demo

Add your screenshots here once available.

### Suggested screenshot slots

```text
assets/screenshots/home.png
assets/screenshots/task-list.png
assets/screenshots/create-task.png
assets/screenshots/update-task.png
```

### Example Markdown

```md
![Home Screen](assets/screenshots/home.png)
![Task Listing](assets/screenshots/task-list.png)
```

### Demo

* Live demo: `[Add deployment link here]`
* Video walkthrough: `[Add demo video link here]`

---

## Configuration

The application behavior can be customized through `.env`.

| Variable            | Description                 | Example                           |
| ------------------- | --------------------------- | --------------------------------- |
| `GROQ_API_KEY`      | Groq API key                | `gsk_...`                         |
| `MODEL_NAME`        | LLM model name              | `qwen/qwen3-32b`                  |
| `DATABASE_URL`      | SQLite database path        | `sqlite:///data/my_tasks.db`      |
| `APP_TITLE`         | UI title                    | `TaskBot - Task Management Agent` |
| `DEFAULT_THREAD_ID` | Default conversation thread | `taskbot-thread-1`                |

---

## Developer Notes

### Check Database Tables

You can inspect whether the `tasks` table exists using:

```bash
python check_db.py
```

### Run Tests

If you add tests in a `tests/` directory:

```bash
pytest
```

### Recommended Future Additions for Testing

* database connection tests
* schema creation tests
* service-level response tests
* agent initialization tests

---

## Deployment Notes

This project currently targets local development and demonstration.

### Suitable Next Deployment Options

* Streamlit Community Cloud
* Dockerized local deployment
* Render
* Railway
* FastAPI backend + React frontend migration

### Production Upgrade Suggestions

* persistent multi-user memory
* PostgreSQL instead of SQLite
* API-based architecture
* authentication and session isolation
* structured observability and logging
* containerization with Docker
* CI/CD pipeline integration

---

## Roadmap / Future Scope

* Add task filtering by status from the UI
* Add structured dataframe rendering for task results
* Add export to CSV
* Add edit task form controls in sidebar
* Add safer SQL guardrails and validation
* Replace local SQLite with PostgreSQL
* Introduce FastAPI backend APIs
* Add Docker support
* Add unit and integration tests
* Support multi-user task spaces
* Deploy a live public demo

---

## Contributing

Contributions, suggestions, and improvements are welcome.

### Recommended workflow

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes

```bash
git commit -m "Add your feature"
```

4. Push to your branch

```bash
git push origin feature/your-feature-name
```

5. Open a pull request

---

## License

This project is currently released under the **MIT License**.

```text
MIT License
```

Update this section if you choose a different license.

---

## Author

**Mahmudul Haque Sakib**
CSE Graduate | AI/ML Enthusiast | Data Science Focused

* GitHub: `[Add GitHub profile link]`
* LinkedIn: `[Add LinkedIn profile link]`

---

## Acknowledgments

This project builds on the capabilities of:

* LangChain
* LangGraph
* Groq
* Streamlit
* SQLite

---

## Final Note

This repository is intended to demonstrate how an LLM-powered assistant can be integrated with structured database tools in a clean, modular, and developer-friendly way. It is lightweight enough for local experimentation and strong enough in structure to serve as a solid portfolio project.
