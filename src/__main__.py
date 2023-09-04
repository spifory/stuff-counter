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

    DEFAULT_GUILD = environ.get("DEFAULT_GUILD")

    client = Client(
        bot,
        default_guild=int(DEFAULT_GUILD) if DEFAULT_GUILD else None
    )

    client.plugins.load_folder("src.plugins")

    bot.run(port=8594)

if __name__ == "__main__":
    main()
