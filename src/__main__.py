from logging import INFO, basicConfig
from os import environ

from crescent import Client
from dotenv import load_dotenv
from hikari import RESTBot


def main():
    load_dotenv()
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )

    bot = RESTBot(environ["BOT_TOKEN"])
    client = Client(
        bot,
        default_guild=environ.get("DEFAULT_GUILD", None),  # type: ignore
    )

    client.plugins.load_folder("src.plugins")

    bot.run()


if __name__ == "__main__":
    main()
