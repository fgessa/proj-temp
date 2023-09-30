from datetime import datetime, timedelta
from typing import Dict, Any, Tuple

import jwt
from flask import Blueprint, request, current_app
from werkzeug.security import  check_password_hash

from api.model import User


access_token_api = Blueprint("access_token_api", __name__)


@access_token_api.route("/request_token")
def request_token() -> Tuple[Dict[str, Any], int]:
    """
    Request a token for a user based on authentication.
    """
    auth = request.authorization

    if not any([auth, auth.username, auth.password]):
        return {"error": "Couldn't verify user"}, 400
    
    if not (user := User.find_by_name(name=auth.username)):
        return {"error": "User not found"}, 404
    
    if not check_password_hash(user.password, auth.password):
        return {"error": "Invalid password"}, 401
    
    token = jwt.encode(
        {
            "public_id": user.public_id,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        },
        key=current_app.config.get("SECRET_KEY")
    )

    return {"token": token}, 200
    




