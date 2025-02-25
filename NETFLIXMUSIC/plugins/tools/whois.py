from datetime import datetime

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User

from NETFLIXMUSIC import app


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


infotext = (
    "╭━─━─━─〔 👤 𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎 〕─━─━─━╮\n"
    " ➜ 𝗡𝗮𝗺𝗲: [{full_name}](tg://user?id={user_id})\n"
    " ➜ 🆔 𝐔𝐬𝐞𝐫 𝐈𝐃: `{user_id}`\n"
    " ➜ 🏷 𝐅𝐢𝐫𝐬𝐭 𝐍𝐚𝐦𝐞: `{first_name}`\n"
    " ➜ 🏷 𝐋𝐚𝐬𝐭 𝐍𝐚𝐦𝐞: `{last_name}`\n"
    " ➜ 🔗 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: `@{username}`\n"
    " ➜ 🕰 𝐋𝐚𝐬𝐭 𝐒𝐞𝐞𝐧: `{last_online}`\n"
    "╰━─━─━─〔 🔍 𝐍𝐄𝐓𝐅𝐋𝐈𝐗 𝐌𝐔𝐒𝐈𝐂 〕─━─━─━╯"
)



def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "Recently"
    elif user.status == "within_week":
        return "Within the last week"
    elif user.status == "within_month":
        return "Within the last month"
    elif user.status == "long_time_ago":
        return "A long time ago :("
    elif user.status == "online":
        return "Currently Online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.status.date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


@app.on_message(filters.command("whois"))
async def whois(client, message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.reply("I don't know that user.")
        return
    desc = await client.get_chat(get_user)
    desc = desc.description
    await message.reply_text(
        infotext.format(
            full_name=FullName(user),
            user_id=user.id,
            user_dc=user.dc_id,
            first_name=user.first_name,
            last_name=user.last_name if user.last_name else "",
            username=user.username if user.username else "",
            last_online=LastOnline(user),
            bio=desc if desc else "`ᴇᴍᴩᴛʏ.`",
        ),
        disable_web_page_preview=True,
    )
