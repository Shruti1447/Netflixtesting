import asyncio
from datetime import datetime
from pyrogram import filters
from NETFLIXMUSIC import app
from NETFLIXMUSIC.core.userbot import Userbot
from config import OWNER_ID

userbot = Userbot()

BOT_LIST = [
    "Netflix_MusicBot"
]

@app.on_message(filters.command("botschk") & filters.group)
async def check_bots_command(client, message):
    global last_checked_time

    # Check if the user is the owner
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("🚫 You are not authorized to use this command.")

    if not userbot.one.is_connected:
        await userbot.one.start()

    # Send the photo with the caption
    processing_msg = await message.reply_photo(
        photo="https://envs.sh/tlM.jpg",
        caption="**Checking Bots Stats Alive Or Dead...**"
    )

    start_time = datetime.now()

    response = "**Bots Status Dead or alive checker**\n\n"

    for bot_username in BOT_LIST:
        try:
            bot = await userbot.one.get_users(bot_username)
            await asyncio.sleep(0.5)
            await userbot.one.send_message(bot.id, "/start")
            await asyncio.sleep(3)
            
            async for bot_message in userbot.one.get_chat_history(bot.id, limit=1):
                status = "Online ✨" if bot_message.from_user.id == bot.id else "Offline ❄"
                response += f"╭⎋ {bot.mention}\n╰⊚ **Status: {status}**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **Status: Error ❌**\n\n"
    
    last_checked_time = start_time.strftime("%Y-%m-%d")
    await processing_msg.edit_caption(f"{response}⏲️ Last Check: {last_checked_time}")

    if userbot.one.is_connected:
        await userbot.one.stop()