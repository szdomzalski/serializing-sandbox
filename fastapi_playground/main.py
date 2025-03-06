from datetime import datetime
from uuid import UUID, uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# Input model for creating a user
class UserIn(BaseModel):
    name: str

# Output model for getting a user
class UserOut(UserIn):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.now)

users = [
    UserOut(name="Alice"),
    UserOut(name="Bob"),
]

# Async is preferred for FastAPI framework (running in asynchronous event loop)
@app.get("/users")
async def get_users() -> list[UserOut]:
    return users

@app.post("/users", status_code=201)  # Status code is in decorator instead of return tuple
async def create_user(user_in: UserIn) -> UserOut:
    user_out = UserOut(name=user_in.name)
    users.append(user_out)
    return user_out
