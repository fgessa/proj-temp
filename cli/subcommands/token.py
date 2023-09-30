import os
from argparse import Namespace

import requests


def request_token(args: Namespace) -> None:
    """
    Request an authentication token from a remote server using HTTP Basic Authentication.
    """
    if (
        not (name := os.environ.get("NAME")) or 
        not (password := os.environ.get("PASSWORD"))
    ):
        raise ValueError("Environment variables NAME and PASSWORD must be set.")
    
    basic_auth = requests.auth.HTTPBasicAuth(name, password)
    r = requests.get(args.url, auth=basic_auth)

    print(r.json())