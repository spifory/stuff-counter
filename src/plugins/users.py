"""A file that contains all commands applicable to user (or more so usernames)."""
from logging import getLogger

from crescent import Context, Plugin, user_command
from hikari import RESTBot, User

plugin = Plugin[RESTBot, None]()
LOG = getLogger()


@plugin.include
@user_command(name="Username Letter Count")
async def user_letter_count(ctx: Context, user: User) -> None:
    """See how many letters a person's username has."""
    letter_count = sum(not i.isspace for i in user.username)
    noun = "letter" if letter_count == 1 else "letters"

    await ctx.respond(
        content=f"{user.mention} has {letter_count} {noun} in their name.",
        user_mentions=False,
    )


@plugin.load_hook
def load() -> None:
    """Logic for loading the plugin."""
    LOG.info("loaded %s", __name__)


@plugin.unload_hook
def unload() -> None:
    """Logic for unloading the plugin."""
    LOG.warning("unloaded %s", __name__)
