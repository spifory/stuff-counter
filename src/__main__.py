"""The main file for the stuff-counter bot that controls everything."""
from logging import INFO, basicConfig
from os import environ

from crescent import Client
from dotenv import load_dotenv
from hikari import RESTBot


def main() -> None:
    """Control the start-up process of the bot."""
    load_dotenv()
    basicConfig(
        format="[%(asctime)s] | %(name)s | %(levelname)s | %(message)s",
        level=INFO,
        datefmt="%Y-%m-%d - %H:%M:%S",
    )

    bot = RESTBot(environ["BOT_TOKEN"])

    default_guild = environ.get("DEFAULT_GUILD")

    client = Client(
        bot,
        default_guild=int(default_guild) if default_guild else None,
    )

    client.plugins.load_folder("src.plugins")

    bot.run(port=8594)


if __name__ == "__main__":
    main()
