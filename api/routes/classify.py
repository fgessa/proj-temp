from typing import Any, Dict, Tuple, ByteString

import cv2
import numpy as np
from flask import request, Blueprint

from api.utils.auth import token_required
from api.utils.predict import predict

classify_api = Blueprint("classify_api", __name__)


def decode_image(encoded_image: ByteString, flag: int=cv2.IMREAD_COLOR) -> cv2.Mat:
    img = np.fromstring(encoded_image, dtype=np.uint8)
    img = cv2.imdecode(img, flag)
    return img


@classify_api.route("/classify", methods=["POST"])
@token_required
def classify_image() -> Tuple[Dict[str, Any], int]:
    """
    Classify an image received in the request data.
    """
    img = decode_image(request.data)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result, score = predict(img)

    return {"prediction": result, "score": score}, 201