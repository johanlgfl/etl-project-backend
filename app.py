from fastapi import FastAPI
from routes.category import category

app = FastAPI()

app.include_router(category)
