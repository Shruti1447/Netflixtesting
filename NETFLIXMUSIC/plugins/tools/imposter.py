from pyrogram import filters
from pyrogram.types import Message
from NETFLIXMUSIC.plugins.tools.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from NETFLIXMUSIC import app




@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**🔓 ᴘʀᴇᴛᴇɴᴅᴇʀ ᴅᴇᴛᴇᴄᴛᴇᴅ 🔓**
➖➖➖➖➖➖➖➖➖➖➖➖
**🍊 Name** : {message.from_user.mention}
**🍅 User ID** : {message.from_user.id}
➖➖➖➖➖➖➖➖➖➖➖➖\n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**🐻‍❄️ Changed UserName 🐻‍❄️**
➖➖➖➖➖➖➖➖➖➖➖➖
**🎭 Froom** : {bef}
**🍜 To** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**🪧 ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ 🪧**
➖➖➖➖➖➖➖➖➖➖➖➖
**🔐 ғʀᴏᴍ** : {bef}
**🍓 ᴛᴏ** : {aft}
➖➖➖➖➖➖➖➖➖➖➖➖\n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**🪧 𝙲𝙷𝙰𝙽𝙶𝙴𝚂 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴 🪧**  
➖➖➖➖➖➖➖➖➖➖➖➖  
**🚏𝙵𝚁𝙾𝙼** : {bef}  
**🍕 𝚃𝙾** : {aft}  
➖➖➖➖➖➖➖➖➖➖➖➖  
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo("https://telegra.ph/file/58afe55fee5ae99d6901b.jpg", caption=msg)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**𝙳𝙴𝚃𝙴𝙲𝚃 𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝚄𝚂𝙴𝚁𝚂 𝚄𝚂𝙰𝙶𝙴 : 𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝙾𝙽|𝙾𝙵𝙵**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝙼𝙾𝙳𝙴 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙴𝙽𝙰𝙱𝙻𝙴𝙳.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙴𝙽𝙰𝙱𝙻𝙴𝙳 𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝙼𝙾𝙳𝙴 𝙵𝙾𝚁 {message.chat.title}**")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝙼𝙾𝙳𝙴 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝙼𝙾𝙳𝙴 𝙵𝙾𝚁 {message.chat.title}**")
    else:
        await message.reply("**𝙳𝙴𝚃𝙴𝙲𝚃 𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝚄𝚂𝙴𝚁𝚂 𝚄𝚂𝙰𝙶𝙴 : 𝙿𝚁𝙴𝚃𝙴𝙽𝙳𝙴𝚁 𝙾𝙽|𝙾𝙵𝙵**")
