# Autonomous Code Review Agent System

## Overview

This project is an **Autonomous Code Review Agent System** designed to analyze GitHub pull requests (PRs) using AI. The system employs a goal-oriented AI agent to independently plan and execute code reviews, process them asynchronously using Celery, and interact with developers via a structured API.

## Features

- **Automated Code Reviews**: The system identifies code style issues, potential bugs, performance optimizations, and adherence to best practices.
- **Asynchronous Task Processing**: Tasks are handled asynchronously with Celery, ensuring scalability and responsiveness.
- **Developer Interaction**: Provides a FastAPI-based interface for submitting PRs, checking task statuses, and retrieving results.

---

## Core Functionality

### 1. Basic API Endpoints

The system includes the following FastAPI endpoints:

- **POST `/analyze-pr`**:  
  Accepts GitHub PR details (repository and PR number) to initiate an analysis task.

- **GET `/status/<task_id>`**:  
  Checks the status of an analysis task by its unique `task_id`.

- **GET `/results/<task_id>`**:  
  Retrieves the results of the analysis for the specified `task_id`.

---

### 2. Asynchronous Processing with Celery

- **Task Management**: Uses Celery for asynchronous task execution.
- **Task Tracking**: Tracks task statuses (e.g., pending, running, completed, failed) and handles errors gracefully.
- **Data Storage**: Stores task results in a **PostgreSQL** database for retrieval.
## Bonus Features

- **Dockerized Deployment**: Includes Docker configuration for easy setup and deployment.
- **Caching**: Implements basic caching for frequently accessed API results.


## Technical Stack

- **Programming Language**: Python 3.8+
- **Frameworks**: FastAPI, Celery
- **Database**: PostgreSQL (for task result storage)
- **Caching**: Redis
- **AI Model Integration**:  
  - OPENAi
- **Testing**: Pytest for unit and integration testing.


## Installation and Setup

### Prerequisites

- Python 3.8+ installed
- Docker and Docker Compose (if using Docker)
- PostgreSQL and Redis instances

### Steps

1. **Clone the Repository**:  
   ```bash
   https://github.com/ajayak5235/backend_auto_AI
  

2. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:  
   Create a `.env` file with the following:
   ```env
   DATABASE_URL=postgresql://user:password@localhost/dbname
   REDIS_URL=redis://localhost:6379/0
   ```

4. **Run Migrations**:  
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**:  
   - Without Docker:
     ```bash
     uvicorn app.main:app --reload
     ```
   - With Docker:
     ```bash
     docker-compose up --build
     ```

6. **Start Celery Worker**:  
   ```bash
   celery -A app.tasks worker --loglevel=info
   ```

---

## Usage

1. **Submit a Pull Request for Analysis**:  
   Send a POST request to `/analyze-pr` with the following payload:  
   ```json
   {
       "repo": "https://github.com/user/repo",
       "pr_number": 123
   }
   ```

2. **Check Task Status**:  
   Send a GET request to `/status/<task_id>` to check the progress.

3. **Retrieve Results**:  
   Once the task is completed, send a GET request to `/results/<task_id>` to get the analysis.

---

## Testing

Run the test suite with:
```bash
pytest


## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Celery](https://docs.celeryproject.org/)
- [OPENAI]

