from datetime import datetime
from uuid import UUID

import httpx
from pydantic import BaseModel, Field, RootModel, field_validator

# Pydantic models are used for data validation and serialization
class Metadata(BaseModel):
    uuid: UUID = Field(alias="id")  # Alias is used for JSON deserialization
    created_at: datetime

class User(Metadata):
    name: str

    # Dummy custom data validation
    # @field_validator auto-applies @classmethod to the decorated method; manually adding @classmethod is not needed
    #   and will even break the code if above @field_validator (validation will fail silently)
    @field_validator("name")
    @classmethod  # This is not needed but it doesn't break the code here; sometimes explicit is better than implicit
    def check_user_name(cls, name: str) -> str:
        if name[0].isupper():
            return name
        raise ValueError("name must start with an uppercase letter")

Users = RootModel[list[User]]

if __name__ == "__main__":
    # Usual approach
    response = httpx.get("http://localhost:8000/users")
    print(response.json())
    # Response body is basically list of JSON objects which can be treated as dictionaries
    for item in response.json():
        user = User(**item)
        print(repr(user))

    # RootModel approach
    response = httpx.get("http://localhost:8000/users")
    users = Users.model_validate_json(response.text)
    print(users)
    print(users.root)  # This is the list of User objects

    # Post request
    # Field name has to be valid with check_user_name method, "delta" will raise pydantic's ValidationError
    # Notice: created_at and id will be overwritten by the server but they are required for an object creation currently
    #   unless I specify them as Optional
    new_user = User(name="Delta", created_at=datetime.now(), id=UUID("12345678-1234-5678-1234-567812345678"))
    body = new_user.model_dump_json()
    print(body)  # This is the JSON string
    # Argument data is used for POST requests with JSON string instead of dictionary
    response = httpx.post("http://localhost:8000/users", data=body)
    print(response.json())
    print(response.status_code)

    response = httpx.get("http://localhost:8000/users")
    users = Users.model_validate_json(response.text)
    print(users)
    print(users.root)