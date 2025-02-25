import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from NETFLIXMUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@app.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git None")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']

                caption = f"""ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}
                
👤 **Username:**:{username}
📜 **Bio:**: {bio}
🔗 **Profile Link:** [Here]({url})
🏢 **Company:**:{company}
📆 **Joined On:** {created_at}
📂 **Repositories:** {repositories}
📝 **Blog:** {blog}
📍 **Location:** {location}
👥 **Followers:** {followers}
🔄 **Following:** {following}"""

            except Exception as e:
                print(str(e))
                pass

    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("Close", callback_data="close")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

    # Send the message with the inline keyboard
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=inline_keyboard)
