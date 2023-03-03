import asyncio
import argparse

from scripts.path import setup_path

setup_path()

from lanjun.actions.users import create_user
from lanjun.domain.user import UserType
from lanjun.http_models.requests import CreateUser


async def main(args: argparse.Namespace):
    user_info = CreateUser(
        email=args.email,
        name=args.name,
        password=args.password,
        phone=args.phone
    )

    token = await create_user(user_info, UserType.ADMIN)
    print(f"Created user with token: `{token}`")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="create_admin")
    parser.add_argument("--name", required=True)
    parser.add_argument("--email", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--phone", required=True)

    arguments = parser.parse_args()
    asyncio.run(main(arguments))
