from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

from flask import Flask, Response, jsonify, request

app = Flask(__name__)

@dataclass
class User:
    id: UUID
    name: str
    created_at: datetime

    @classmethod
    def create(cls, name: str) -> "User":
        return cls(uuid4(), name, datetime.now())

users = [
    User.create("Alice"),
    User.create("Bob"),
]

@app.route("/users", methods=["GET", "POST"])
def view_users() -> list[str] | tuple[Response, int]:
    if request.method == "GET":
        return users  # Flask will automatically serialize this list
    elif request.method == "POST":
        if request.is_json:  # Check if the request has a JSON body via mimetype
            # Create user from JSON payload
            payload = request.get_json()
            user = User.create(payload["name"])
            users.append(user)
            # Return the user as JSON with status code 201; jsonify helps with serialization of dataclass
            return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)