import uuid

from flask import Blueprint, request, make_response
from werkzeug.security import generate_password_hash

from api.db import db
from api.model import User


user_api = Blueprint("user", __name__)

@user_api.route("/register", methods=["POST"])
def register_user() -> None:
    """
    Register a new user based on JSON data received in the request.
    """
    data = request.get_json()

    if user := User.find_by_name(data["name"]):
        return {"message": f"User already exists"}, 400

    user = User(
        public_id=str(uuid.uuid4()),
        name=data["name"], 
        password=generate_password_hash(data["password"])
    )
    db.session.add(user)
    db.session.commit()

    return {"message": "User created!"}, 401





