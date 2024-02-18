from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional


router = APIRouter(
    prefix='/blog', tags=['blog']
)

class BlogModel(BaseModel):
    title:str
    content:str
    nb_comments: int
    published: Optional[bool]

@router.post('/{id}')
def create_post(blog:BlogModel, id: int, version: int = 1):

    return {'message': f'your blog is created successfully, your blog title is {blog.title}'}


@router.post('/{id}/comments')
def create_comment(blog: BlogModel, id: int, 
                   comment_id:int = Query(
                       None,
                       title = "Id of the comment",
                       description="whatever description",
                       alias = "commentId",
                       deprecated=True
                   ),
                   content:str = Body(..., min_length=10)
                   ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id
    }