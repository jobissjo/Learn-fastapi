from fastapi import APIRouter, status,Response
from enum import Enum
from typing import Optional


router = APIRouter(
    prefix="/blog", tags=['blog']
)

class TypeEnum(str, Enum):
    story = 'story'
    whatever = 'whatever'
    education = 'education'



@router.get('/{id:int}', 
         summary='get the blog with id',
         description='This api will retrieve blog if matches the id')
def get_blog(id: int):
    return {'message': f'This is your blog num {id}'}

@router.get('/type/{type}')
def get_type_wise_blog(type: TypeEnum):
    return f'you selected {type.value}'


@router.get('/{id}/comment/{comment_id}', tags=['comments'])
def get_comments(id:int, comment_id:int, 
                 valid: bool, username:str | None = None):
    """
    This is a retrieve the blog with corresponding comments

    - **id** mandatory
    - **comment_id** mandatory
    """
    return {'message': f'blog {id} , of comment {id} is valid: {valid} of user : {username}'}

