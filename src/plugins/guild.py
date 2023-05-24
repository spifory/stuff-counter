import re

from disnake import AllowedMentions, GuildCommandInteraction, Role, TextChannel, Thread
from disnake.abc import GuildChannel
from disnake.ext.plugins import Plugin

from src.impl.bot import Bot

plugin = Plugin[Bot](
    name=__name__, # no sense in allowing this in DMs
    slash_command_attrs={"dm_permission": False}
)

@plugin.slash_command(name="letter-count")
async def letter_count(_: GuildCommandInteraction):
    pass

@letter_count.sub_command(name="role")
async def count_role(inter: GuildCommandInteraction, role: Role):
    """See how many letters are a role name.

    Parameters
    ----------
    role: The role to count the letters of.
    """
    role_name_count = len(re.sub(r"\s+", "", role.name))
    noun = "letter" if role_name_count == 1 else "letters"

    return await inter.response.send_message(
        f"The role {role.mention} has {role_name_count} {noun} in its name",
        allowed_mentions=AllowedMentions.none()
    )

@letter_count.sub_command(name="server-name")
async def count_guild_name(inter: GuildCommandInteraction):
    """See how many letters are in the server name."""
    guild_name_count = len(re.sub(r"\s+", "", inter.guild.name))
    noun = "letter" if guild_name_count == 1 else "letters"

    return await inter.response.send_message(
        f"This server has {guild_name_count} {noun} in its name",
    )

@letter_count.sub_command(name="channel-name")
async def count_channel_name(inter: GuildCommandInteraction, channel: GuildChannel):
    """See how many letters are in a channel name.

    Parameters
    ----------
    channel: The channel to count the letters of.
    """
    channel_name_count = len(re.sub(r"\s+", "", channel.name))
    noun = "letter" if channel_name_count == 1 else "letters"

    return await inter.response.send_message(
        f"The channel {channel.mention} has {channel_name_count} {noun} in its name",
    )


setup, teardown = plugin.create_extension_handlers()
