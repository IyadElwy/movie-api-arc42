from fastapi import FastAPI
from app.database.connection import init_db
from app.api.routes import movies, actors, ratings

app = FastAPI(
    title="Movie Browsing API",
    description="A REST API for browsing movie data with actors and ratings",
    version="1.0.0"
)

app.include_router(movies.router)
app.include_router(actors.router)
app.include_router(ratings.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def root():
    return {
        "message": "Welcome to the Movie Browsing API",
        "docs": "/docs",
        "openapi": "/openapi.json"
    }
