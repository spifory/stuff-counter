from disnake import Message, MessageCommandInteraction
from disnake.ext.plugins import Plugin
from emoji import emoji_count

from src.impl.bot import Bot

plugin = Plugin[Bot](message_command_attrs={"dm_permission": False})

@plugin.message_command(name="Word Count")
async def message_word_count(inter: MessageCommandInteraction, message: Message):
    word_count = len(message.content.split(" "))
    noun = "words" if word_count > 1 or word_count == 0 else "word"

    return await inter.response.send_message(
        f"[This]({message.jump_url}) message has {word_count} {noun} in it.",
    )

@plugin.message_command(name="Emoji Count")
async def message_emoji_count(inter: MessageCommandInteraction, message: Message):
    count = emoji_count(message.content)
    noun = "emojis" if count > 1 or count == 0 else "emoji"

    return await inter.response.send_message(
        f"[This]({message.jump_url}) message has {count} {noun} in it \N{EYES}",
    )

@plugin.message_command(name="Letter Count")
async def message_character_count(inter: MessageCommandInteraction, message: Message):
    character_count = len(message.content.strip())
    noun = "letters" if character_count > 1 or character_count == 0 else "letter"

    return await inter.response.send_message(
        f"[This]({message.jump_url}) message has {character_count} {noun} in it",
    )

setup, teardown = plugin.create_extension_handlers()
