import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NETFLIXMUSIC import LOGGER, app, userbot
from NETFLIXMUSIC.core.call import SHRUSHTHI
from NETFLIXMUSIC.misc import sudo
from NETFLIXMUSIC.plugins import ALL_MODULES
from NETFLIXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴀssɪsᴛᴀɴᴛ sᴇssɪᴏɴ ɴᴏᴛ ғɪʟʟᴇᴅ, ᴘʟᴇᴀsᴇ ғɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NETFLIXMUSIC.plugins" + all_module)
    LOGGER("NETFLIXMUSIC.plugins").info("NETFLIX's ᴍᴏᴅᴜʟᴇs ʟᴏᴀᴅᴇᴅ...")
    await userbot.start()
    await SHRUSHTHI.start()
    try:
        await SHRUSHTHI.stream_call("https://envs.sh/tlB.mp4")
    except NoActiveGroupCall:
        LOGGER("NETFLIXMUSIC").error(
            ""🔊Please turn on the voice chat** in your log group/channel.\n\nNetflix Bot has stopped..."
        )
        exit()
    except:
        pass
    await SHRUSHTHI.decorators()
    LOGGER("NETFLIXMUSIC").info(
        "\x41\x6e\x6e\x69\x65\x20\x4d\x75\x73\x69\x63\x20\x52\x6f\x62\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x2e\x2e"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NETFLIXMUSIC").info("🛑Stopping Netflix Music Bot...🚀")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())