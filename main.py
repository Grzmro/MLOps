import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:

    if environment not in ["dev", "test", "prod"]:
        raise ValueError("Environment must be one of: dev, test, prod")

    env_file = f"config/.env.{environment}"

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"{env_file} does not exist.")

    load_dotenv(dotenv_path=env_file)


def load_secrets(path: str = "secrets.yaml") -> None:
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} does not exist.")

    with open(path, "r") as file:
        secrets = yaml.safe_load(file)

    for key, value in secrets.items():
        os.environ[key] = str(value)


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
    load_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API_KEY: ", settings.API_KEY)
