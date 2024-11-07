from fastapi import Path, FastAPI
from typing import Annotated

app = FastAPI()

@app.get('/user/{user_id}')
async def user_welcome(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> dict:
    return {'message': f'Welcome, user №{user_id}'}


@app.get('user/{username}/{age}')
async def user_age(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
                   age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> dict:
    return {'message': f"Hello, {username}:{age}"}