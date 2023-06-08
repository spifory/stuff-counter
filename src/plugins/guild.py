from logging import getLogger
from hikari import GuildTextChannel, RESTBot, Role
from crescent import Context, Group, Plugin, command, option


plugin = Plugin[RESTBot, None]()
log = getLogger(__name__)

letter_count = Group("letter-count", dm_enabled=False)


@plugin.include
@letter_count.child
@command(name="role", description="See how many letters are a role's name.")
class LetterCountRoleCount:
    role = option(description="The role to count the letters of", option_type=Role)

    async def callback(self, ctx: Context):
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
    name="server-name", description="See how many letters are in the server's name."
)
class LetterCountGuildName:
    async def callback(self, ctx: Context):
        assert ctx.guild_id is not None
        guild = await plugin.app.rest.fetch_guild(ctx.guild_id)
        server_name_count = sum(not c.isspace() for c in guild.name)
        noun = "letter" if server_name_count == 1 else "letters"

        return await ctx.respond(
            f"This server has {server_name_count} {noun} in its name",
            role_mentions=False,  # in case the server name is a bloody role mention for whatever reason
            mentions_everyone=False,  # in case the server name is @everyone for some reason
        )


@plugin.include
@letter_count.child
@command(
    name="channel-name", description="See how many letters are in the channel's name."
)
class LetterCountChannelName:
    channel = option(
        description="The channel to count the letters of",
        option_type=GuildTextChannel,
        default=None,
    )

    async def callback(self, ctx: Context):
        if self.channel is None:
            assert ctx.channel_id is not None
            channel = await plugin.app.rest.fetch_channel(ctx.channel_id)
        else:
            channel = await plugin.app.rest.fetch_channel(self.channel.id)

        assert (
            channel.name is not None
        )  # this command is not dm enabled, so this should never happen

        channel_name_count = sum(not c.isspace() for c in channel.name)
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
    channel = option(
        description="The channel to count the pins of",
        option_type=GuildTextChannel,
        default=None,
    )

    async def callback(self, ctx: Context):
        if self.channel is None:
            assert ctx.channel_id is not None
            channel = ctx.channel_id
        else:
            channel = self.channel.id

        pin_count = len(await plugin.app.rest.fetch_pins(channel))

        return await ctx.respond(
            f"<#{channel}> has {pin_count} pinned message{'' if pin_count == 1 else 's'}"
        )


@plugin.load_hook
def setup():
    log.info(f"Loaded {__name__}")


@plugin.unload_hook
def teardown():
    log.info(f"Unloaded {__name__}")
