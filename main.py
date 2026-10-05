import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:

    if environment not in ["dev", "test", "prod"]:
        raise ValueError("Environment must be one of: dev, test, prod")

    env_file = f"config/.env.{environment}"

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"{env_file} does not exist.")

    load_dotenv(dotenv_path=env_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
