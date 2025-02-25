import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from NETFLIXMUSIC import app
from config import SUPPORT_CHAT

BUTTON = [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Beats_Support")]]
HOT = "https://imgflip.com/gif/9lehqr"
HORNY = "https://envs.sh/trt.mp4"
SEMXY = "https://envs.sh/tre.mp4"
LESBIAN = "https://envs.sh/trt.mp4"
GAY = "https://envs.sh/tre.mp4"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANGD = "hhttps://envs.sh/tre.mp4"
CUTIE = "https://envs.sh/tre.mp4"

####### masti
########  CUTE
@app.on_message(filters.command("cutie"))
async def cutie(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"🍑 {mention} {mm}% ᴄᴜᴛᴇ ʙᴀʙʏ🥀"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
###### horny

@app.on_message(filters.command("horny"))
async def horny(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HORNE = f"🔥 {mention} ɪꜱ {mm} % ʜᴏʀɴʏ!"

    await app.send_document(
        chat_id=message.chat.id,
        document=HORNY,
        caption=HORNE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

###### HOT 

@app.on_message(filters.command("hot"))
async def hot(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HOTIE = f"🔥{mention} ɪꜱ {mm}% ʜᴏᴛ!"

    await app.send_document(
        chat_id=message.chat.id,
        document=HOT,
        caption=HOTIE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

########## SEXY 

@app.on_message(filters.command("sexy"))
async def sexy(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    SEXO = f" 🔥 {mention} ɪꜱ {mm}% sexy!"
    await app.send_document (
        chat_id=message.chat.id,
        document=SEMXY,
        caption=SEXO,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

#########gay
@app.on_message(filters.command("gay"))
async def gay(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAYE = f" 🍷 {mention} ɪꜱ {mm}% ɢᴀʏ!"
    await app.send_document (
        chat_id=message.chat.id,
        document=GAY,
        caption=GAYE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

########### LESBIAN
@app.on_message(filters.command("lesbian"))
async def lesbian(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    LEZBIAN = f" 💜 {mention} ɪꜱ {mm}% ʟᴇꜱʙɪᴀɴ!"
    await app.send_document (
        chat_id=message.chat.id,
        document=LESBIAN,
        caption=LEZBIAN,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

########### BOOBS

@app.on_message(filters.command("boob"))
async def boob(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BALL = f" 🍒 {mention}ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ {mm} ! "
    await app.send_document (
        chat_id=message.chat.id,
        document=BIGBALL,
        caption=BALL,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)

######### COCK

@app.on_message(filters.command("cock"))
async def cock(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BAT = f" 🍆 {mention}  ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ {mm}ᴄᴍ"
    await app.send_document (
        chat_id=message.chat.id,
        document=LANGD,
        caption=BAT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
)
