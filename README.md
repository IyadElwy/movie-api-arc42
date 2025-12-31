# Movie Browsing API

A REST API for browsing movie data built with FastAPI, following Richardson Maturity Model Level 2 and layered architecture principles.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Common Workflows](#common-workflows)
- [Development](#development)

## Overview

This project provides a REST API for managing and browsing movie data, including information about actors and ratings. The API follows REST best practices, implementing Richardson Maturity Model Level 2 with proper HTTP methods and status codes.

### Key Features

- CRUD operations for Movies, Actors, and Ratings
- Embedded relationships (movies include full actor and rating objects)
- Proper HTTP status codes (200, 201, 204, 404, 409, etc.)
- SQLite database for data persistence
- In-memory caching through SQLAlchemy
- Layered architecture for separation of concerns

## Architecture

The application follows a three-layer architecture:

1. **Database Layer**: SQLAlchemy ORM models and database connection
2. **Persistence Layer**: Repository pattern for data access
3. **Business Layer**: Service classes containing business logic
4. **API Layer**: FastAPI route handlers and Pydantic schemas

```
┌─────────────────┐
│   API Layer     │  (FastAPI routes, Pydantic schemas)
├─────────────────┤
│ Business Layer  │  (Services with business logic)
├─────────────────┤
│Persistence Layer│  (Repositories)
├─────────────────┤
│ Database Layer  │  (SQLAlchemy models)
└─────────────────┘
```

## Tech Stack

- **Python**: 3.12
- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Dependency Management**: Poetry
- **Container**: Docker

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py              # SQLAlchemy models
│   │   └── connection.py          # Database connection and session
│   ├── persistence/
│   │   ├── __init__.py
│   │   └── repositories.py        # Repository pattern implementations
│   ├── business/
│   │   ├── __init__.py
│   │   └── services.py            # Business logic services
│   └── api/
│       ├── __init__.py
│       ├── schemas.py             # Pydantic models
│       └── routes/
│           ├── __init__.py
│           ├── movies.py          # Movie endpoints
│           ├── actors.py          # Actor endpoints
│           └── ratings.py         # Rating endpoints
├── scripts/
│   └── populate_data.py           # Database seeding script
├── .devcontainer/
│   └── devcontainer.json          # VS Code dev container config
├── Dockerfile
├── pyproject.toml                 # Poetry dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.12
- Poetry (or Docker)

### Installation

#### Option 1: Local Setup with Poetry

1. Install dependencies:
```bash
poetry install
```

2. Activate the virtual environment:
```bash
poetry shell
```

3. Populate the database with sample data:
```bash
python scripts/populate_data.py
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

#### Option 2: Docker

1. Build the Docker image:
```bash
docker build -t movie-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 movie-api
```

3. Populate the database (in a separate terminal):
```bash
docker exec -it <container-id> python scripts/populate_data.py
```

#### Option 3: Dev Container (VS Code)

1. Open the project in VS Code
2. Install the "Dev Containers" extension
3. Press F1 and select "Dev Containers: Reopen in Container"
4. The container will automatically install dependencies and populate the database

### API Documentation

Once running, access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Movies

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/movies` | Get all movies | 200 OK |
| GET | `/movies/{id}` | Get a specific movie | 200 OK, 404 Not Found |
| POST | `/movies` | Create a new movie | 201 Created |
| PUT | `/movies/{id}` | Update a movie | 200 OK, 404 Not Found |
| DELETE | `/movies/{id}` | Delete a movie | 204 No Content, 404 Not Found |

#### Movie Response Schema

```json
{
  "id": 1,
  "title": "The Shawshank Redemption",
  "releaseDate": "1994-09-23",
  "runtime": 142,
  "synopsis": "Two imprisoned men bond over a number of years...",
  "posterUrl": "https://example.com/posters/shawshank.jpg",
  "language": "English",
  "genres": ["Drama", "Crime"],
  "budget": 25000000,
  "revenue": 28341469,
  "actors": [
    {
      "id": 1,
      "firstName": "Tim",
      "lastName": "Robbins",
      "fullName": "Tim Robbins",
      "birthDate": "1958-10-16",
      "nationality": "American"
    }
  ],
  "ratings": [
    {
      "id": 1,
      "score": 9.3,
      "reviewText": "An absolute masterpiece...",
      "reviewerEmail": "john.doe@example.com"
    }
  ],
  "averageRating": 9.3
}
```

### Actors

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/actors` | Get all actors | 200 OK |
| GET | `/actors/{id}` | Get a specific actor | 200 OK, 404 Not Found |
| POST | `/actors` | Create a new actor | 201 Created |
| PUT | `/actors/{id}` | Update an actor | 200 OK, 404 Not Found |
| DELETE | `/actors/{id}` | Delete an actor | 204 No Content, 404 Not Found |

#### Actor Response Schema

```json
{
  "id": 1,
  "firstName": "Morgan",
  "lastName": "Freeman",
  "fullName": "Morgan Freeman",
  "birthDate": "1937-06-01",
  "nationality": "American"
}
```

### Ratings

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/ratings` | Get all ratings | 200 OK |
| GET | `/ratings/{id}` | Get a specific rating | 200 OK, 404 Not Found |
| POST | `/ratings` | Create a new rating | 201 Created, 404 Not Found (if movie doesn't exist) |
| PUT | `/ratings/{id}` | Update a rating | 200 OK, 404 Not Found |
| DELETE | `/ratings/{id}` | Delete a rating | 204 No Content, 404 Not Found |

#### Rating Response Schema

```json
{
  "id": 1,
  "score": 9.5,
  "reviewText": "An absolute masterpiece of storytelling...",
  "reviewerEmail": "john.doe@example.com"
}
```

## Common Workflows

### Workflow 1: Creating a Complete Movie Entry

This workflow demonstrates creating a movie with actors and ratings from scratch.

#### Step 1: Create Actors

```bash
# Create first actor
curl -X POST http://localhost:8000/actors \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "Leonardo",
    "lastName": "DiCaprio",
    "birthDate": "1974-11-11",
    "nationality": "American"
  }'

# Response: {"id": 1, "firstName": "Leonardo", ...}

# Create second actor
curl -X POST http://localhost:8000/actors \
  -H "Content-Type: application/json" \
  -d '{
    "firstName": "Kate",
    "lastName": "Winslet",
    "birthDate": "1975-10-05",
    "nationality": "British"
  }'

# Response: {"id": 2, "firstName": "Kate", ...}
```

#### Step 2: Create Movie with Actor References

```bash
curl -X POST http://localhost:8000/movies \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Titanic",
    "releaseDate": "1997-12-19",
    "runtime": 195,
    "synopsis": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
    "posterUrl": "https://example.com/posters/titanic.jpg",
    "language": "English",
    "genres": ["Drama", "Romance"],
    "budget": 200000000,
    "revenue": 2187463944,
    "actorIds": [1, 2]
  }'

# Response: {"id": 1, "title": "Titanic", "actors": [...], "ratings": [], ...}
```

#### Step 3: Add Ratings to the Movie

```bash
# Add first rating
curl -X POST http://localhost:8000/ratings \
  -H "Content-Type: application/json" \
  -d '{
    "score": 9.2,
    "movieId": 1,
    "reviewText": "A timeless classic. Beautifully crafted.",
    "reviewerEmail": "critic1@example.com"
  }'

# Add second rating
curl -X POST http://localhost:8000/ratings \
  -H "Content-Type: application/json" \
  -d '{
    "score": 8.8,
    "movieId": 1,
    "reviewText": "Emotionally powerful and visually stunning.",
    "reviewerEmail": "critic2@example.com"
  }'
```

#### Step 4: Retrieve the Complete Movie

```bash
curl http://localhost:8000/movies/1

# Response includes embedded actors and ratings with calculated average
```

### Workflow 2: Browsing and Filtering Movies

#### Get All Movies

```bash
curl http://localhost:8000/movies
```

#### Get a Specific Movie

```bash
curl http://localhost:8000/movies/1
```

#### Get All Actors

```bash
curl http://localhost:8000/actors
```

### Workflow 3: Updating Movie Information

#### Update Movie Details

```bash
curl -X PUT http://localhost:8000/movies/1 \
  -H "Content-Type: application/json" \
  -d '{
    "revenue": 2200000000
  }'
```

#### Add More Actors to a Movie

```bash
curl -X PUT http://localhost:8000/movies/1 \
  -H "Content-Type: application/json" \
  -d '{
    "actorIds": [1, 2, 3]
  }'
```

### Workflow 4: Managing Ratings

#### Update a Rating

```bash
curl -X PUT http://localhost:8000/ratings/1 \
  -H "Content-Type: application/json" \
  -d '{
    "score": 9.5,
    "reviewText": "Updated review: Even better on second viewing!"
  }'
```

#### Delete a Rating

```bash
curl -X DELETE http://localhost:8000/ratings/1
```

### Workflow 5: Deleting Data

#### Delete a Movie (Cascade deletes ratings)

```bash
curl -X DELETE http://localhost:8000/movies/1
# Returns 204 No Content
```

#### Delete an Actor

```bash
curl -X DELETE http://localhost:8000/actors/1
# Returns 204 No Content
```

## Development

### Running Tests

```bash
poetry run pytest
```

### Code Style

The project uses standard Python conventions. Format code with:

```bash
poetry run black .
```

### Database

The SQLite database (`movies.db`) is stored in the project root. To reset the database:

1. Delete the `movies.db` file
2. Run the populate script: `python scripts/populate_data.py`

### Richardson Maturity Model Level 2

This API implements RMM Level 2:

- **HTTP Methods**: Uses proper HTTP verbs (GET, POST, PUT, DELETE)
- **HTTP Status Codes**: Returns appropriate status codes:
  - `200 OK`: Successful GET/PUT
  - `201 Created`: Successful POST
  - `204 No Content`: Successful DELETE
  - `404 Not Found`: Resource not found
  - `409 Conflict`: Constraint violations
- **Idempotency**: GET, PUT, and DELETE are idempotent
- **Safe Operations**: GET is safe (read-only)
- **Caching**: Enabled through HTTP semantics (SQLAlchemy session caching)

## License

This project is created as an educational MVP for learning REST API development.
