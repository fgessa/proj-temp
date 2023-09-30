import os
from argparse import ArgumentParser, Namespace

from dotenv import load_dotenv

from cli.subcommands import classify, register_user, request_token


load_dotenv()

base_url=os.environ.get("BASE_URL")

def parse_args()->Namespace:

    parser = ArgumentParser()
    subparsers = parser.add_subparsers(help='mladversary api operations')

    classify_parser = subparsers.add_parser("classify", help="Classify provide image")
    classify_parser.add_argument("-i", "--image", required=True, help="Path to image")
    classify_parser.add_argument(
        "-u",
        "--url",
        default=f"{base_url}/classify",
        help="API to classify image"
    )
    classify_parser.set_defaults(func=classify)

    register_parser = subparsers.add_parser("register", help="Register")
    register_parser.add_argument(
        "-u",
        "--url",
        default=f"{base_url}/register",
        help="API to register user"
    )
    register_parser.set_defaults(func=register_user)

    token_parser = subparsers.add_parser(
        "request_token", help="Token to use in subsequent requests"
    )
    token_parser.add_argument(
        "-u",
        "--url",
        default=f"{base_url}/request_token",
        help="API to request token"
    )
    token_parser.set_defaults(func=request_token)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    args.func(args)



