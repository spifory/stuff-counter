from logging import getLogger

from disnake import Activity, ActivityType, Intents
from disnake.ext.commands import InteractionBot

log = getLogger(__name__)
__all__ = ("Bot",)


class Bot(InteractionBot):
    def __init__(self):
        super().__init__(
            intents=Intents(guilds=True, guild_messages=True, message_content=True),
            activity=Activity(name="counting game", type=ActivityType.playing),
            test_guilds=(906815360492253205,)
        )

    async def on_ready(self):
        log.info("logged in as %s", self.user)

