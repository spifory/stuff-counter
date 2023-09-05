"""A file controlling all commands applicable to guilds."""
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from crescent import Context, Group, Plugin, command, option
from hikari import GuildTextChannel, RESTBot, Role

if TYPE_CHECKING:
    from hikari import Message

plugin = Plugin[RESTBot, None]()
log = getLogger(__name__)

letter_count = Group("letter-count", dm_enabled=False)


@plugin.include
@letter_count.child
@command(name="role", description="See how many letters are a role's name.")
class LetterCountRoleCount:
    """See how many letters are a role's name."""

    role = option(description="The role to count the letters of", option_type=Role)

    async def callback(self, ctx: Context) -> Message | None:
        """Control the callback for the `/letter-count role` command."""
        role_name_count = sum(not c.isspace() for c in self.role.name)
        noun = "letter" if role_name_count == 1 else "letters"

        return await ctx.respond(
            f"The role {self.role.mention} has {role_name_count} {noun} in its name",
            role_mentions=False,
            mentions_everyone=False,  # in case the role name is @everyone for some reason
        )


@plugin.include
@letter_count.child
@command(
    name="server-name",
    description="See how many letters are in the server's name.",
)
class LetterCountGuildName:
    """See how many letters are in the server's name."""

    async def callback(self, ctx: Context) -> Message | None:
        """Control the callback for the `/letter-count server-name` command."""
        guild = await plugin.app.rest.fetch_guild(
            ctx.guild_id,  # type: ignore[reportGeneralTypeIssues]
        )
        server_name_count = sum(not c.isspace() for c in guild.name)
        noun = "letter" if server_name_count == 1 else "letters"

        return await ctx.respond(
            f"This server has {server_name_count} {noun} in its name",
            role_mentions=False,  # in case the server name is a role mention for whatever reason
            mentions_everyone=False,  # in case the server name is @everyone for some reason
        )


@plugin.include
@letter_count.child
@command(
    name="channel-name",
    description="See how many letters are in the channel's name.",
)
class LetterCountChannelName:
    """See how many letters are in the channel's name."""

    channel = option(
        description="The channel to count the letters of",
        option_type=GuildTextChannel,
        default=None,
    )

    async def callback(self, ctx: Context) -> Message | None:
        """Control the callback for the `/letter-count channel-name` command."""
        if self.channel is None:
            channel = await plugin.app.rest.fetch_channel(ctx.channel_id)
        else:
            channel = await plugin.app.rest.fetch_channel(self.channel.id)

        # this command is not dm enabled, so this should never be None
        channel_name_count = sum(
            not c.isspace() for c in channel.name  # type: ignore[reportGeneralTypeIssues]
        )
        noun = "letter" if channel_name_count == 1 else "letters"

        return await ctx.respond(
            f"{channel.mention} has {channel_name_count} {noun} in its name",
        )


@plugin.include
@command(
    name="pin-count",
    description="See how many pins are in the channel.",
    dm_enabled=False,
)
class PinCount:
    """See how many pins are in the channel."""

    channel = option(
        description="The channel to count the pins of",
        option_type=GuildTextChannel,
        default=None,
    )

    async def callback(self, ctx: Context) -> Message | None:
        """Control the callback for the `/pin-count` command."""
        channel = ctx.channel_id if self.channel is None else self.channel.id

        pin_count = len(await plugin.app.rest.fetch_pins(channel))

        return await ctx.respond(
            f"<#{channel}> has {pin_count} pinned message{'' if pin_count == 1 else 's'}",
        )


@plugin.load_hook
def load() -> None:
    """Logic for loading the plugin."""
    log.info("Loaded {__name__}")


@plugin.unload_hook
def unload() -> None:
    """Logic for unloading the plugin."""
    log.info("Unloaded {__name__}")
