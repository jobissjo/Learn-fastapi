from fastapi import FastAPI, status,Response
from enum import Enum
from typing import Optional
from routers import blog_get, blog_post, users
from db import models, database

app = FastAPI()
app.include_router(users.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def index():
    return 'Hello world'


@app.get('/products/{id}', tags=['products'])
def get_products(id: int, response:Response)-> dict[str,str]:
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    response.status_code = status.HTTP_200_OK
    return {'message': f'Blog with id {id}'}

models.Base.metadata.create_all(database.engine)