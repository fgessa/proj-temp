import functools
from typing import Any, Callable, Union, Dict, Tuple

import jwt
from flask import current_app, request

from api.model import User


def token_required(func: Callable) -> Callable:
     @functools.wraps(func)
     def wrapper() -> Union[Tuple[Dict[str, str], int], Callable]:
        if not (token := request.headers.get("x-access-token", None)):
            return {"message": "Token missing!"}, 401
        
        try:
            data = jwt.decode(
                token, current_app.config.get("SECRET_KEY"), algorithms=['HS256']
            )

            if not User.find_by_public_id(data["public_id"]):
                return {"error": "Bad Token"}, 401

        except (jwt.exceptions.DecodeError, jwt.exceptions.InvalidSignatureError) as e:
            return {"error": f"Token is invalid: {e}"}, 401
        
        except (jwt.ExpiredSignatureError) as e:
            return {"message": str(e)}, 401
        
        return func()
     
     return wrapper