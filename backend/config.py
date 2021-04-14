from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from books.models import ModelBook
from decouple import config


# Models
ALL_MODELS = [ModelBook]


# Middleware
def middlewareAPI(app: FastAPI, available=True):
    """
        the backend is in a different "origin" than the frontend.
    """
    if available:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=config('HOST'),
        )
