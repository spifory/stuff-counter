from disnake import User, UserCommandInteraction
from disnake.ext.plugins import Plugin

from src.impl.bot import Bot

plugin = Plugin[Bot]()

@plugin.user_command(name="Username Letter Count")
async def user_username_count(inter: UserCommandInteraction, user: User):
    username_count = len(user.name)
    noun = "letter" if username_count == 1 else "letters"

    return await inter.response.send_message(
        f"{user.mention} has {username_count} {noun} in their username",
    )

setup, teardown = plugin.create_extension_handlers()
