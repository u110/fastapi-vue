from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NEW
register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "hello, world!"
