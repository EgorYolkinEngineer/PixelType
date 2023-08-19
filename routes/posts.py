from fastapi import APIRouter
from core.database import session
from models.db_models import Post
import utils
import time
from models import pydantic_models

posts_router = APIRouter()


@posts_router.post('/api/v1/post/create')
async def create_post(post: pydantic_models.Post):
    post = Post(
        author=post.author,
        title=post.title,
        key=utils.transform_title(post.title),
        text=post.text,
        created=time.time()
    )
    session.add(post)
    session.commit()

    return {'key': post.key}


@posts_router.get('/api/v1/posts/')
async def create_post(limit: int = 10, offset: int = 0):
    if limit >= 50:
        limit = 50
    queryset = session.query(Post).limit(limit).offset(offset)

    return [_.to_dict() for _ in queryset]
