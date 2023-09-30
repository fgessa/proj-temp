import os
from argparse import Namespace

import cv2
import numpy as np
import requests


def is_file_image(image_extension: str) -> bool:
    return image_extension in [".png", ".jpg", ",jpeg"]


def get_file_extension(image_path: str) -> str:
    return os.path.splitext(image_path)[1]


def encode_image(image_path:str, image_extension:str) -> np.ndarray:
    image = cv2.imread(image_path)
    _, encoded_image = cv2.imencode(image_extension, image)
    return encoded_image


def classify(args: Namespace) -> None:
    """
    Classify an image by sending it to a remote server for analysis.
    """
    if not (token := os.environ.get("TOKEN")):
        raise ValueError("TOKEN environment variable is not set. Please set it.")

    ext = get_file_extension(args.image)

    if not is_file_image(ext):
        print("Please provide a valid path to image file")
        return

    encoded_image = encode_image(args.image, image_extension=ext)

    headers = {
         "content-type": f"image/{ext[1:]}",
         "x-access-token": token,
    }
    r = requests.post(args.url, data=encoded_image.tobytes(), headers=headers)

    print(r.json())