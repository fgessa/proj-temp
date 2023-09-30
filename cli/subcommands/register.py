from argparse import Namespace
import os
import requests


def register_user(args: Namespace) -> None:
    """
    Register a user by sending registration data to a remote server.
    """
    if (
        not (name := os.environ.get("NAME")) or 
        not (password := os.environ.get("PASSWORD"))
    ):
        raise ValueError("Environment variables NAME and PASSWORD must be set.")

    data = {
        "name": name,
        "password": password,
    }
    r = requests.post(args.url, json=data)
    
    print(r.json())