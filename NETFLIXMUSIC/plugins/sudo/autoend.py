from pyrogram import filters
from pyrogram.types import Message

from NETFLIXMUSIC import app
from NETFLIXMUSIC.misc import SUDOERS
from NETFLIXMUSIC.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» Auto End Stream Enabled.\n\nThe assistant will automatically leave the video chat after a few minutes when no one is listening."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("🚫 **Auto End Stream Disabled.**")
    else:
        await message.reply_text(usage)
