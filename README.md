# stuff-counter

A Discord bot that counts everything for you, when you don't feel like it!

## Hosting Locally

Setting up the bot is really easy, you firstly need to fill in the .env file with a bot token. You _can_ also add a list of guilds to test commands on, but it's not required.

```
BOT_TOKEN=...

# optional
DEFAULT_GUILD=... # used for posting commands to a guild. Usually for testing
```

Then you can run `poetry run task start` to start the bot.
