from typing import Any, Dict, Tuple, ByteString

import cv2
import numpy as np
from flask import request, Blueprint
from api.utils.auth import token_required


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
    return {"image_height": img.shape[0], "image_width": img.shape[1]}, 201