from fastapi import APIRouter, Path
from config.db import conn
from models.categories import categories
from schemas.category import Category

category = APIRouter(
    prefix="/category",
    tags=["Category"],
)


@category.get("/")
def read_category():
    return conn.execute(categories.select()).fetchall()


@category.post("/{category_id}", response_model=Category, description="Create a new category")
def read_category(category: Category, category_id: int = Path(..., title="The ID of the category")):
    return f"category {category_id}"
