import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from NETFLIXMUSIC import app 

spam_chats = []


GM_MESSAGES = [ "➠ 𝙶𝚘𝚘𝚍 𝙼𝚘𝚛𝚗𝚒𝚗𝚐! ☀️ 𝙰𝚞𝚛 𝚔𝚢𝚊 𝚑𝚊𝚕 𝚑𝚊𝚒 𝚖𝚎𝚛𝚎 𝚍𝚘𝚜𝚝? 🤗",
           "➠ 𝙰𝚓 𝚋𝚑𝚒 𝚗𝚊𝚢𝚊 𝚍𝚒𝚗 𝚊𝚢𝚊 𝚑𝚊𝚒, 𝚜𝚘 𝚞𝚝𝚑𝚘 𝚘𝚛 𝚊𝚙𝚗𝚎 𝚜𝚙𝚗𝚘𝚗 𝚙𝚎 𝚕𝚊𝚐𝚘! ✨",
           "➠ 𝙲𝚑𝚊𝚒 𝚙𝚒 𝚕𝚘, 𝚘𝚛 𝚋𝚊𝚍𝚑𝚒𝚢𝚊 𝚍𝚒𝚗 𝚔𝚎 𝚕𝚒𝚢𝚎 𝚝𝚢𝚊𝚛 𝚑𝚘 𝚓𝚊𝚘! ☕😄",
           "➠ 𝙴𝚔 𝚗𝚊𝚢𝚊 𝚍𝚒𝚗, 𝚎𝚔 𝚗𝚊𝚢𝚒 𝚖𝚞𝚜𝚔𝚊𝚗! 😊 𝙶𝚘𝚘𝚍 𝙼𝚘𝚛𝚗𝚒𝚗𝚐! 🌸",
           "➠ 𝘊𝘩𝘢𝘯𝘥 𝘬𝘢 𝘳𝘢𝘫 𝘬𝘩𝘢𝘵𝘮, 𝘚𝘶𝘳𝘢𝘫 𝘬𝘪 𝘫𝘦𝘦𝘵! ☀️ 𝘈𝘢𝘫 𝘬𝘪 𝘴𝘶𝘣𝘩 𝘬𝘢 𝘢𝘢𝘨𝘢𝘢𝘻 𝘩𝘰 𝘨𝘢𝘺𝘢! 🌼",
           "➠ 𝙰𝚐𝚊𝚛 𝚣𝚒𝚗𝚍𝚊𝚐𝚒 𝚖𝚎 𝚋𝚑𝚎𝚝𝚎𝚛𝚒 𝚌𝚑𝚊𝚑𝚒𝚎, 𝚝𝚘 𝚞𝚝𝚑𝚘 𝚘𝚛 𝚊𝚊𝚙𝚗𝚒 𝚖𝚎𝚑𝚗𝚝 𝚔𝚊𝚛𝚘! 💪 𝙶𝚘𝚘𝚍 𝙼𝚘𝚛𝚗𝚒𝚗𝚐! 🌅",
           "➠ 𝙼𝚞𝚜𝚔𝚊𝚗 𝚝𝚑𝚘𝚍𝚒 𝚋𝚑𝚒 𝚗𝚊 𝚖𝚒𝚜𝚜 𝚔𝚊𝚛𝚗𝚊, 𝚘𝚛 𝚏𝚞𝚕𝚕 𝚓𝚘𝚜𝚑 𝚖𝚎 𝚍𝚒𝚗 𝚜𝚝𝚊𝚛𝚝 𝚔𝚊𝚛𝚘! 😎🔥",
           "➠ 𝘊𝘩𝘢𝘪 𝘬𝘦 𝘦𝘬 𝘴𝘪𝘱 𝘴𝘦 𝘩𝘪 𝘴𝘢𝘳𝘪 𝘵𝘩𝘢𝘬𝘢𝘯 𝘤𝘩𝘢𝘭𝘪 𝘫𝘢𝘢𝘺𝘦! ☕ 𝘎𝘰𝘰𝘥 𝘔𝘰𝘳𝘯𝘪𝘯𝘨! 🌞",
           "➠ 𝙰𝚓 𝚔𝚞𝚌𝚑 𝚗𝚊𝚢𝚊 𝚔𝚊𝚛𝚘, 𝚓𝚘 𝚝𝚞𝚖𝚑𝚎 𝚋𝚎𝚑𝚝𝚎𝚛 𝚋𝚗𝚊𝚢𝚎! 🚀✨",
           "➠ 𝘊𝘩𝘢𝘪 𝘱𝘪𝘵𝘦 𝘱𝘪𝘵𝘦 𝘬𝘢𝘮𝘪𝘢𝘣𝘪 𝘬𝘦 𝘴𝘢𝘢𝘳𝘦 𝘪𝘥𝘦𝘢 𝘢𝘢𝘵𝘦 𝘩𝘢𝘪𝘯! ☕😆 𝘎𝘰𝘰𝘥 𝘔𝘰𝘳𝘯𝘪𝘯𝘨!",
           "➠ 𝙰𝚋 𝚍𝚎𝚔𝚑𝚘, 𝚜𝚞𝚛𝚊𝚓 𝚗𝚒𝚌𝚑𝚎 𝚜𝚎 𝚜𝚞𝚛𝚊𝚓 𝚘𝚞𝚙𝚛 𝚊𝚊 𝚐𝚢𝚊, 𝚞𝚝𝚑𝚘 𝚘𝚛 𝚊𝚙𝚗𝚒 𝚓𝚒𝚗𝚍𝚊𝚐𝚒 𝚓𝚒𝚘! 🌞",
           "➠ 𝘕𝘢𝘺𝘢 𝘥𝘪𝘯, 𝘯𝘢𝘺𝘪 𝘶𝘮𝘦𝘦𝘥𝘦𝘪𝘯, 𝘰𝘳 𝘯𝘢𝘺𝘪 𝘫𝘪𝘮𝘮𝘦𝘥𝘢𝘳𝘪𝘺𝘢𝘯! 💪🔥",
           "➠ 𝘈𝘢𝘴𝘮𝘢𝘯 𝘬𝘪 𝘖𝘳 𝘥𝘦𝘬𝘩𝘰, 𝘤𝘩𝘢𝘯𝘥 𝘨𝘢𝘺𝘢, 𝘴𝘶𝘳𝘢𝘫 𝘢𝘺𝘢! 𝘉𝘴 𝘢𝘣 𝘵𝘶𝘮 𝘣𝘩𝘪 𝘶𝘵𝘩𝘰! 🌅",
           "➠ 𝙶𝚘𝚘𝚍 𝙼𝚘𝚛𝚗𝚒𝚗𝚐! 𝚂𝚞𝚋𝚑 𝚔𝚒 𝚜𝚑𝚞𝚛𝚞𝚊𝚝 𝚖𝚞𝚜𝚔𝚊𝚗 𝚜𝚎 𝚔𝚛𝚘! 😊✨",
           "➠ 𝘋𝘦𝘳 𝘮𝘢𝘵 𝘬𝘢𝘳𝘰, 𝘶𝘵𝘩𝘰 𝘰𝘳 𝘥𝘶𝘯𝘪𝘺𝘢 𝘬𝘰 𝘥𝘪𝘬𝘩𝘢 𝘥𝘰 𝘬𝘪 𝘵𝘶𝘮 𝘬𝘪𝘵𝘯𝘦 𝘣𝘩𝘦𝘵𝘦𝘳 𝘩𝘰! 🌟",
           "➠ 𝙽𝚊𝚖𝚊𝚣 𝚙𝚍𝚑𝚘, 𝚍𝚞𝚊 𝚔𝚛𝚘, 𝚘𝚛 𝚏𝚒𝚛 𝚏𝚞𝚕𝚕 𝚎𝚗𝚎𝚛𝚐𝚢 𝚜𝚎 𝚍𝚒𝚗 𝚜𝚝𝚊𝚛𝚝 𝚔𝚛𝚘! 🙏☀️",
           "➠ 𝘒𝘶𝘤𝘩 𝘢𝘤𝘩𝘢 𝘤𝘩𝘢𝘩𝘪𝘺𝘦 𝘵𝘰 𝘬𝘩𝘶𝘥 𝘬𝘰 𝘣𝘦𝘵𝘵𝘦𝘳 𝘣𝘢𝘯𝘢𝘯𝘢 𝘱𝘢𝘥𝘦𝘨𝘢! 🔥 𝘎𝘰𝘰𝘥 𝘔𝘰𝘳𝘯𝘪𝘯𝘨!",
        ]


GN_MESSAGES = [  "➠ 𝔾𝕠𝕠𝕕 ℕ𝕚𝕘𝕙𝕥 🌙 𝕊𝕝𝕖𝕖𝕡 𝕋𝕚𝕘𝕙𝕥, 𝔻𝕣𝕖𝕒𝕞 𝔹𝕚𝕘! 😴✨",
           "➠ 𝕊𝕙𝕙𝕙.. 𝕊𝕠 𝕛𝕒𝕠! 𝕍𝕒𝕣𝕟𝕒 𝕞𝕦𝕞𝕞𝕪 𝕒𝕒 𝕛𝕒𝕪𝕖𝕘𝕚! 🤫😂",
           "➠ 🅟🅗🅞🅝🅔 🅡🅐🅚🅗 🅚🅔 🅢🅞 🅙🅐, 🅝🅐🅗🅘 🅣🅞 🅑🅗🅞🅞🅣 🅐🅐 🅙🅐🅨🅔🅖🅐..👻",
           "➠ 𝒜𝒷 𝓈𝑜 𝒿𝒶𝑜, 𝓃𝒶𝒽𝒾𝓃 𝓉𝑜 𝓂𝒶𝓂𝓂𝒶 𝓅𝒾𝓉𝑒𝑔𝒾! 😜",
           "➠ 𝐑𝐚𝐚𝐭 𝐤𝐨 𝐦𝐚𝐭 𝐣𝐚𝐠𝐨, 𝐧𝐚𝐡𝐢 𝐭𝐨 𝐬𝐮𝐛𝐡 𝐮𝐭𝐡𝐧𝐞 𝐦𝐞 𝐦𝐚𝐦𝐦𝐲 𝐤𝐚 𝐛𝐞𝐥𝐭 𝐜𝐡𝐚𝐥𝐞𝐠𝐚! 😆",
           "➠ 𝕊𝕨𝕖𝕖𝕥 𝔻𝕣𝕖𝕒𝕞𝕤 ✨ 𝕄𝕦𝕟𝕟𝕒 𝕤𝕠 𝕛𝕒, 𝕨𝕒𝕣𝕟𝕒 𝕓𝕒𝕓𝕒 𝕒𝕛𝕒𝕪𝕖𝕘𝕒! 😨",
           "➠ 𝑮𝒐𝒐𝒅 𝑵𝒊𝒈𝒉𝒕, 𝒔𝒘𝒆𝒆𝒕 𝒅𝒓𝒆𝒂𝒎𝒔, 𝒅𝒐𝒏'𝒕 𝒍𝒆𝒕 𝒕𝒉𝒆 𝒎𝒐𝒔𝒒𝒖𝒊𝒕𝒐𝒆𝒔 𝒃𝒊𝒕𝒆! 🦟😂",
           "➠ 𝐆𝐨𝐨𝐝 𝐍𝐢𝐠𝐡𝐭! 💫 𝐁𝐚𝐬 𝐬𝐨 𝐣𝐚𝐨, 𝐚𝐠𝐚𝐫 𝐤𝐨𝐢 𝐩𝐡𝐨𝐧𝐞 𝐝𝐞𝐤𝐡 𝐫𝐚𝐡𝐚 𝐡𝐚𝐢 𝐭𝐨 𝐮𝐬𝐤𝐨 𝐛𝐡𝐢 𝐬𝐨𝐧𝐚 𝐡𝐚𝐢! 😴📵",
           "➠ 𝙶𝚘𝚘𝚍 𝙽𝚒𝚐𝚑𝚝 🌙 𝙳𝚘𝚗'𝚝 𝚠𝚘𝚛𝚛𝚢, 𝚝𝚘𝚖𝚘𝚛𝚛𝚘𝚠 𝚒𝚜 𝚊 𝚗𝚎𝚠 𝚍𝚊𝚢! ✨",
           "➠ 𝘈𝘤𝘩𝘩𝘢 𝘵𝘩𝘦𝘦𝘬 𝘩𝘢𝘪, 𝘴𝘰 𝘫𝘢𝘰! 𝘚𝘰𝘣𝘪 𝘬𝘪 𝘛𝘢𝘳𝘢𝘩 𝘤𝘩𝘢𝘯𝘥 𝘬𝘰 𝘯𝘩𝘪𝘯 𝘥𝘦𝘬𝘩𝘯𝘢 𝘩𝘢𝘪 😅",
           "➠ 𝙶𝚘𝚘𝚍 𝙽𝚒𝚐𝚑𝚝 🌙 𝙳𝚘𝚗'𝚝 𝚠𝚘𝚛𝚛𝚢, 𝚝𝚘𝚖𝚘𝚛𝚛𝚘𝚠 𝚒𝚜 𝚊 𝚗𝚎𝚠 𝚍𝚊𝚢! ✨",
           "➠ 𝘈𝘤𝘩𝘩𝘢 𝘵𝘩𝘦𝘦𝘬 𝘩𝘢𝘪, 𝘴𝘰 𝘫𝘢𝘰! 𝘚𝘰𝘣𝘪 𝘬𝘪 𝘛𝘢𝘳𝘢𝘩 𝘤𝘩𝘢𝘯𝘥 𝘬𝘰 𝘯𝘩𝘪𝘯 𝘥𝘦𝘬𝘩𝘯𝘢 𝘩𝘢𝘪 😅",
           "➠ 𝙶𝚘𝚘𝚍 𝙽𝚒𝚐𝚑𝚝 😴 𝚂𝚠𝚎𝚎𝚝 𝙳𝚛𝚎𝚊𝚖𝚜! 🌙✨",
           "➠ 𝙷𝚊𝚛 𝚍𝚒𝚗 𝚗𝚎𝚠 𝚑𝚘𝚝𝚊 𝚑𝚊𝚒, 𝚌𝚑𝚒𝚗𝚝𝚊 𝚖𝚊𝚝 𝚔𝚛𝚘 𝚊𝚞𝚛 𝚊𝚛𝚊𝚖 𝚜𝚎 𝚜𝚘 𝚓𝚊𝚘! 💫",
           "➠ 𝙱𝚎𝚜𝚝 𝚠𝚒𝚜𝚑𝚎𝚜 𝚏𝚘𝚛 𝚢𝚘𝚞𝚛 𝚍𝚛𝚎𝚊𝚖𝚜! 💤 𝙶𝚗 😴",
           "➠ 𝚂𝚝𝚊𝚛𝚜 𝚊𝚛𝚎 𝚠𝚊𝚝𝚌𝚑𝚒𝚗𝚐 𝚘𝚟𝚎𝚛 𝚢𝚘𝚞, 𝚛𝚎𝚜𝚝 𝚠𝚎𝚕𝚕! 🌠",
           "➠ 𝘔𝘢𝘵 𝘴𝘰𝘤𝘩𝘰 𝘬𝘪 𝘬𝘺𝘢 𝘩𝘶𝘢, 𝘴𝘪𝘳𝘧 𝘺𝘦 𝘴𝘰𝘤𝘩𝘰 𝘬𝘪 𝘬𝘢𝘭 𝘬𝘺𝘢 𝘩𝘰𝘨𝘢! 😉",
           "➠ 𝙲𝚕𝚘𝚜𝚎 𝚢𝚘𝚞𝚛 𝚎𝚢𝚎𝚜 𝚊𝚗𝚍 𝚕𝚎𝚝 𝚝𝚑𝚎 𝚍𝚛𝚎𝚊𝚖𝚜 𝚝𝚊𝚔𝚎 𝚘𝚟𝚎𝚛! 😇",
           "➠ 𝙰𝚜𝚖𝚊𝚗 𝚖𝚎 𝚝𝚊𝚛𝚎 𝚔𝚒 𝚝𝚊𝚛𝚊𝚑, 𝚜𝚞𝚔𝚘𝚗 𝚜𝚎 𝚜𝚘 𝚓𝚊𝚘! 🌌",
           "➠ 𝙲𝚑𝚊𝚗𝚍 𝚔𝚘 𝚍𝚎𝚔𝚑𝚘, 𝚊𝚛𝚊𝚖 𝚜𝚎 𝚜𝚘 𝚓𝚊𝚘! 🌙✨",
           "➠ 𝙳𝚘𝚗'𝚝 𝚠𝚘𝚛𝚛𝚢, 𝚋𝚎 𝚑𝚊𝚙𝚙𝚢! 😍 𝙶𝚘𝚘𝚍 𝙽𝚒𝚐𝚑𝚝!",
           "➠ 𝙷𝚊𝚗𝚜𝚘 𝚊𝚞𝚛 𝚔𝚑𝚞𝚜𝚑 𝚛𝚊𝚑𝚘, 𝚏𝚒𝚛 𝚊𝚛𝚊𝚖 𝚜𝚎 𝚜𝚘 𝚓𝚊𝚘! 😊",
           "➠ 𝙰𝚜𝚖𝚊𝚗 𝚔𝚎 𝚝𝚊𝚛𝚎 𝚋𝚜 𝚝𝚞𝚖𝚑𝚎 𝚍𝚎𝚔𝚑 𝚛𝚑𝚎 𝚑𝚊𝚒𝚗, 𝚊𝚛𝚊𝚖 𝚜𝚎 𝚜𝚘𝚓𝚊𝚘! 🌌",
           "➠ 𝙳𝚎𝚛 𝚜𝚎 𝚜𝚘𝚗𝚊 𝚖𝚊𝚝, 𝚊𝚊𝚖 𝚑𝚘 𝚓𝚊𝚘𝚐𝚎! 😂 𝙶𝚘𝚘𝚍 𝙽𝚒𝚐𝚑𝚝!",
           "➠ 𝙲𝚑𝚊𝚗𝚍 𝚜𝚎 𝚔𝚊𝚑𝚗𝚊, 𝚝𝚞 𝚋𝚑𝚒 𝚊𝚛𝚊𝚖 𝚜𝚎 𝚜𝚘𝚓𝚊, 𝚝𝚎𝚛𝚊 𝚖𝚒𝚝𝚛 𝚋𝚑𝚒 𝚜𝚘 𝚛𝚊𝚑𝚊 𝚑𝚊𝚒! 🌙✨",
           "➠ 𝚂𝚞𝚔𝚘𝚗 𝚜𝚎 𝚜𝚘𝚓𝚊𝚘, 𝚏𝚒𝚛 𝚋𝚑𝚒 𝚔𝚘𝚒 𝚖𝚊𝚜𝚕𝚊 𝚑𝚘, 𝚖𝚒𝚝𝚛𝚘𝚗 𝚜𝚎 𝚙𝚘𝚘𝚌𝚑 𝚕𝚎𝚗𝚊! 😆",
           "➠ 𝘒𝘢𝘩𝘪𝘯 𝘮𝘪𝘴𝘵𝘢𝘬𝘦 𝘩𝘶𝘪 𝘵𝘰𝘩 𝘧𝘪𝘭𝘦 𝘤𝘭𝘰𝘴𝘦 𝘬𝘢𝘳𝘬𝘦 𝘢𝘨𝘭𝘪 𝘴𝘶𝘣𝘩 𝘳𝘦𝘴𝘵𝘢𝘳𝘵 𝘬𝘢𝘳 𝘭𝘦𝘯𝘢! 💾😜",
           "➠ 𝙲𝚑𝚘𝚝𝚎-𝚌𝚑𝚘𝚝𝚎 𝚝𝚘𝚝𝚎 𝚍𝚘 𝚊𝚊𝚛𝚊𝚖 𝚜𝚎 𝚗𝚒𝚗𝚍 𝚕𝚎𝚗𝚊, 𝚏𝚒𝚛 𝚋𝚑𝚒 𝚐𝚊𝚋𝚑𝚛𝚊𝚘 𝚗𝚊𝚑𝚒𝚗, 𝚖𝚊𝚒𝚗 𝚑𝚞 𝚗𝚊! 😉",
           "➠ 𝘈𝘢𝘫 𝘬𝘪 𝘥𝘩𝘶𝘯 𝘣𝘩𝘶𝘭 𝘫𝘢𝘰, 𝘯𝘢𝘺𝘪 𝘴𝘶𝘣𝘩 𝘬𝘪 𝘵𝘺𝘢𝘳𝘪 𝘬𝘳𝘰! 😌",
           "➠ 𝙶𝚘𝚘𝚍 𝙽𝚒𝚐𝚑𝚝! 𝙰𝚐𝚊𝚛 𝚔𝚘𝚒 𝚜𝚊𝚙𝚗𝚊 𝚖𝚒𝚜𝚜 𝚑𝚘 𝚐𝚢𝚊, 𝚞𝚜𝚔𝚘 𝚏𝚒𝚛 𝚜𝚎 𝚕𝚘𝚊𝚍 𝚔𝚊𝚛 𝚕𝚎𝚗𝚊! 😆💾",
           "➠ 𝘔𝘦𝘳𝘢 𝘦𝘬 𝘢𝘤𝘩𝘢 𝘥𝘰𝘴𝘵 𝘩𝘢𝘪, 𝘫𝘰 𝘢𝘣 𝘴𝘰𝘯𝘦 𝘫𝘢 𝘳𝘢𝘩𝘢 𝘩𝘢𝘪, 𝘣𝘦𝘴𝘩𝘢𝘬 𝘶𝘴𝘦 𝘎𝘯 𝘬𝘩𝘦𝘩 𝘥𝘰! 😇",
           "➠ 𝙱𝚎𝚝𝚝𝚎𝚛 𝚍𝚊𝚢𝚜 𝚊𝚛𝚎 𝚌𝚘𝚖𝚒𝚗𝚐, 𝚊𝚋 𝚔𝚑𝚞𝚍 𝚙𝚎 𝚎𝚝𝚋𝚊𝚛 𝚔𝚊𝚛𝚘 𝚘𝚛 𝚜𝚘 𝚓𝚊𝚘! 💜✨",
           ]

HI_MESSAGES = [ " **❅ बेबी कहा हो। 🤗** ",
           " **❅ ओए सो गए क्या, ऑनलाइन आओ ।😊** ",
           " **❅ ओए वीसी आओ बात करते हैं । 😃** ",
           " **❅ खाना खाया कि नही। 🥲** ",
           " **❅ घर में सब कैसे हैं। 🥺** ",
           " **❅ पता है बहुत याद आ रही आपकी। 🤭** ",
           " **❅ और बताओ कैसे हो।..?? 🤨** ",
           " **❅ मेरी भी सैटिंग करवा दो प्लीज..?? 🙂** ",
           " **❅ आपका नाम क्या है।..?? 🥲** ",
           " **❅ नाश्ता हो गया..?? 😋** ",
           " **❅ मुझे अपने ग्रूप में ऐड कर लो। 😍** ",
           " **❅ आपका दोस्त आपको बुला रहा है। 😅** ",
           " **❅ मुझसे शादी करोगे ..?? 🤔** ",
           " **❅ सोने चले गए क्या 🙄** ",
           " **❅ अरे यार कोई AC चला दो 😕** ",
           " **❅ आप कहा से हो..?? 🙃** ",
           " **❅ हेलो जी नमस्ते 😛** ",
           " **❅ BABY क्या कर रही हो..? 🤔** ",
           " **❅ क्या आप मुझे जानते हो .? ☺️** ",
           " **❅ आओ baby Ludo खेलते है .🤗** ",
           " **❅ चलती है क्या 9 से 12... 😇** ",
           " **❅ आपके पापा क्या करते है 🤭** ",
           " **❅ आओ baby बाजार चलते है गोलगप्पे खाने। 🥺** ",
           " **❅ अकेली ना बाजार जाया करो, नज़र लग जायेगी। 😶** ",
           " **❅ और बताओ BF कैसा है ..?? 🤔** ",
           " **❅ गुड मॉर्निंग 😜** ",
           " **❅ मेरा एक काम करोगे। 🙂** ",
           " **❅ DJ वाले बाबू मेरा गाना चला दो। 😪** ",
           " **❅ आप से मिलकर अच्छा लगा।☺** ",
           " **❅ मेरे बाबू ने थाना थाया।..? 🙊** ",
           " **❅ पढ़ाई कैसी चल रही हैं ? 😺** ",
           " **❅ हम को प्यार हुआ। 🥲** ",
           " **❅ Nykaa कौन है...? 😅** ",
           " **❅ तू खींच मेरी फ़ोटो ..? 😅** ",
           " **❅ Phone काट मम्मी आ गई क्या। 😆** ",
           " **❅ और भाबी से कब मिल वा रहे हो । 😉** ",
           " **❅ क्या आप मुझसे प्यार करते हो 💚** ",
           " **❅ मैं तुम से बहुत प्यार करती हूं..? 👀** ",
           " **❅ बेबी एक kiss दो ना..?? 🙉** ",
           " **❅ एक जॉक सुनाऊं..? 😹** ",
           " **❅ vc पर आओ कुछ दिखाती हूं  😻** ",
           " **❅ क्या तुम instagram चलते हो..?? 🙃** ",
           " **❅ whatsapp नंबर दो ना अपना..? 😕** ",
           " **❅ आप की दोस्त से मेरी सेटिंग करा दो ..? 🙃** ",
           " **❅ सारा काम हो गया हो तो ऑनलाइन आ जाओ।..? 🙃** ",
           " **❅ कहा से हो आप 😊** ",
           " **❅ जा तुझे आज़ाद कर दिया मैंने मेरे दिल से। 🥺** ",
           " **❅ मेरा एक काम करोगे, ग्रूप मे कुछ मेंबर ऐड कर दो ..? ♥️** ",
           " **❅ मैं तुमसे नाराज़ हूं 😠** ",
           " **❅ आपकी फैमिली कैसी है..? ❤** ",
           " **❅ क्या हुआ..? 🤔** ",
           " **❅ बहुत याद आ रही है आपकी 😒** ",
           " **❅ भूल गए मुझे 😏** ",
           " **❅ झूठ क्यों बोला आपने मुझसे 🤐** ",
           " **❅ इतना भाव मत खाया करो, रोटी खाया करो कम से कम मोटी तो हो जाओगी 😒** ",
           " **❅ ये attitude किसे दिखा रहे हो 😮** ",
           " **❅ हेमलो कहा busy ho 👀** ",
           " **❅ आपके जैसा दोस्त पाकर मे बहुत खुश हूं। 🙈** ",
           " **❅ आज मन बहुत उदास है ☹️** ",
           " **❅ मुझसे भी बात कर लो ना 🥺** ",
           " **❅ आज खाने में क्या बनाया है 👀** ",
           " **❅ क्या चल रहा है 🙂** ",
           " **❅ message क्यों नहीं करती हो..🥺** ",
           " **❅ मैं मासूम हूं ना 🥺** ",
           " **❅ कल मज़ा आया था ना 😅** ",
           " **❅ कल कहा busy थे 😕** ",
           " **❅ आप relationship में हो क्या..? 👀** ",
           " **❅ कितने शांत रहते हो यार आप 😼** ",
           " **❅ आपको गाना, गाना आता है..? 😸** ",
           " **❅ घूमने चलोगे मेरे साथ..?? 🙈** ",
           " **❅ हमेशा हैप्पी रहा करो यार 🤞** ",
           " **❅ क्या हम दोस्त बन सकते है...? 🥰** ",
           " **❅ आप का विवाह हो गया क्या.. 🥺** ",
           " **❅ कहा busy the इतने दिनों से 🥲** ",
           " **❅ single हो या mingle 😉** ",
           " **❅ आओ पार्टी करते है 🥳** ",
           " **❅ Bio में link हैं join कर लो 🧐** ",
           " **❅ मैं तुमसे प्यार नहीं करती, 🥺** ",
           " **❅ यहां आ जाओ ना @Shrushthi_25 मस्ती करेंगे 🤭** ",
           " **❅ भूल जाओ मुझे,..? 😊** ",
           " **❅ अपना बना ले पिया, अपना बना ले 🥺** ",
           " **❅ मेरा ग्रुप भी join कर लो ना 🤗** ",
           " **❅ मैने तेरा नाम Dil rakh diya 😗** ",
           " **❅ तुमारे सारे दोस्त कहा गए 🥺** ",
           " **❅ 𝐈𝐬𝐦𝐞 𝐚𝐚 𝐣𝐚𝐨 𝐟𝐥𝐢𝐫𝐭 𝐤𝐫𝐞𝐧𝐠𝐞 @Beats_Support 🥰** ",
           " **❅ किसकी याद मे खोए हो जान 😜** ",
           " **❅ गुड नाईट जी बहुत रात हो गई 🥰** ",
           ]

QUOTES = [ "𝗜𝗳 𝘆𝗼𝘂 𝗱𝗼 𝗻𝗼𝘁 𝘀𝘁𝗲𝗽 𝗳𝗼𝗿𝘄𝗮𝗿𝗱, 𝘆𝗼𝘂 𝘄𝗶𝗹𝗹 𝗿𝗲𝗺𝗮𝗶𝗻 𝗶𝗻 𝘁𝗵𝗲 𝘀𝗮𝗺𝗲 𝗽𝗹𝗮𝗰𝗲.",
           "𝗟𝗶𝗳𝗲 𝗶𝘀 𝗵𝗮𝗿𝗱 𝗯𝘂𝘁 𝗻𝗼𝘁 𝗶𝗺𝗽𝗼𝘀𝘀𝗶𝗯𝗹𝗲.",
           "𝗟𝗶𝗳𝗲’𝘀 𝘁𝗼𝗼 𝘀𝗵𝗼𝗿𝘁 𝘁𝗼 𝗮𝗿𝗴𝘂𝗲 𝗮𝗻𝗱 𝗳𝗶𝗴𝗵𝘁.",
           "𝗗𝗼𝗻’𝘁 𝘄𝗮𝗶𝘁 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗽𝗲𝗿𝗳𝗲𝗰𝘁 𝗺𝗼𝗺𝗲𝗻𝘁. 𝗧𝗮𝗸𝗲 𝘁𝗵𝗲 𝗺𝗼𝗺𝗲𝗻𝘁 𝗮𝗻𝗱 𝗺𝗮𝗸𝗲 𝗶𝘁 𝗽𝗲𝗿𝗳𝗲𝗰𝘁.",
           "𝗦𝗶𝗹𝗲𝗻𝗰𝗲 𝗶𝘀 𝘁𝗵𝗲 𝗯𝗲𝘀𝘁 𝗮𝗻𝘀𝘄𝗲𝗿 𝘁𝗼 𝘀𝗼𝗺𝗲𝗼𝗻𝗲 𝘄𝗵𝗼 𝗱𝗼𝗲𝘀𝗻’𝘁 𝘃𝗮𝗹𝘂𝗲 𝘆𝗼𝘂𝗿 𝘄𝗼𝗿𝗱𝘀.",
           "𝗘𝘃𝗲𝗿𝘆 𝗻𝗲𝘄 𝗱𝗮𝘆 𝗶𝘀 𝗮 𝗰𝗵𝗮𝗻𝗰𝗲 𝘁𝗼 𝗰𝗵𝗮𝗻𝗴𝗲 𝘆𝗼𝘂𝗿 𝗹𝗶𝗳𝗲.",
           "𝗧𝗼 𝗰𝗵𝗮𝗻𝗴𝗲 𝘆𝗼𝘂𝗿 𝗹𝗶𝗳𝗲, 𝘆𝗼𝘂 𝗻𝗲𝗲𝗱 𝘁𝗼 𝗰𝗵𝗮𝗻𝗴𝗲 𝘆𝗼𝘂𝗿 𝗽𝗿𝗶𝗼𝗿𝗶𝘁𝗶𝗲𝘀.",
           "𝗟𝗶𝗳𝗲 𝗶𝘀 𝗮 𝗷𝗼𝘂𝗿𝗻𝗲𝘆, 𝗻𝗼𝘁 𝗮 𝗿𝗮𝗰𝗲.",
           "𝗧𝗵𝗲 𝗯𝗲𝘀𝘁 𝘄𝗮𝘆 𝘁𝗼 𝗽𝗿𝗲𝗱𝗶𝗰𝘁 𝘁𝗵𝗲 𝗳𝘂𝘁𝘂𝗿𝗲 𝗶𝘀 𝘁𝗼 𝗰𝗿𝗲𝗮𝘁𝗲 𝗶𝘁.",
           "𝗬𝗼𝘂 𝗼𝗻𝗹𝘆 𝗳𝗮𝗶𝗹 𝘄𝗵𝗲𝗻 𝘆𝗼𝘂 𝘀𝘁𝗼𝗽 𝘁𝗿𝘆𝗶𝗻𝗴.",
           "𝗪𝗼𝗿𝗸 𝗵𝗮𝗿𝗱 𝗶𝗻 𝘀𝗶𝗹𝗲𝗻𝗰𝗲, 𝗹𝗲𝘁 𝘀𝘂𝗰𝗰𝗲𝘀𝘀 𝗯𝗲 𝘆𝗼𝘂𝗿 𝗻𝗼𝗶𝘀𝗲.",
           "𝗧𝗵𝗲 𝗼𝗻𝗹𝘆 𝘄𝗮𝘆 𝘁𝗼 𝗱𝗼 𝗴𝗿𝗲𝗮𝘁 𝘄𝗼𝗿𝗸 𝗶𝘀 𝘁𝗼 𝗹𝗼𝘃𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝗱𝗼.",
           "𝗛𝗮𝗿𝗱 𝘁𝗶𝗺𝗲𝘀 𝗿𝗲𝘃𝗲𝗮𝗹 𝘁𝗿𝘂𝗲 𝗳𝗿𝗶𝗲𝗻𝗱𝘀.",
           "𝗗𝗼𝗻'𝘁 𝗹𝗲𝘁 𝘆𝗼𝘂𝗿 𝗳𝗲𝗮𝗿𝘀 𝗱𝗲𝗰𝗶𝗱𝗲 𝘆𝗼𝘂𝗿 𝗳𝘂𝘁𝘂𝗿𝗲.",
           "𝗧𝗵𝗲 𝗯𝗲𝘀𝘁 𝗶𝘀 𝘆𝗲𝘁 𝘁𝗼 𝗰𝗼𝗺𝗲.",
           "𝗧𝗵𝗲 𝗼𝗻𝗹𝘆 𝗹𝗶𝗺𝗶𝘁 𝘁𝗼 𝗼𝘂𝗿 𝗿𝗲𝗮𝗹𝗶𝘇𝗮𝘁𝗶𝗼𝗻 𝗼𝗳 𝘁𝗼𝗺𝗼𝗿𝗿𝗼𝘄 𝗶𝘀 𝗼𝘂𝗿 𝗱𝗼𝘂𝗯𝘁𝘀 𝗼𝗳 𝘁𝗼𝗱𝗮𝘆.",
           "𝗛𝗼𝗽𝗲 𝗶𝘀 𝘁𝗵𝗲 𝗼𝗻𝗹𝘆 𝘁𝗵𝗶𝗻𝗴 𝘀𝘁𝗿𝗼𝗻𝗴𝗲𝗿 𝘁𝗵𝗮𝗻 𝗳𝗲𝗮𝗿.",
           "𝗧𝗵𝗲 𝗷𝗼𝘆 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗵𝗲𝗮𝗿𝘁 𝗶𝘀 𝘁𝗵𝗲 𝗯𝗲𝘀𝘁 𝗳𝘂𝗲𝗹 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝗱𝗿𝗲𝗮𝗺𝘀."
           "𝗦𝗺𝗶𝗹𝗲, 𝗶𝘁'𝘀 𝘁𝗵𝗲 𝗸𝗲𝘆 𝘁𝗵𝗮𝘁 𝗳𝗶𝘁𝘀 𝘁𝗵𝗲 𝗹𝗼𝗰𝗸 𝗼𝗳 𝗲𝘃𝗲𝗿𝘆𝗼𝗻𝗲'𝘀 𝗵𝗲𝗮𝗿𝘁!",
           "𝗜𝗳 𝘆𝗼𝘂 𝘁𝗵𝗶𝗻𝗸 𝗻𝗼𝗯𝗼𝗱𝘆 𝗰𝗮𝗿𝗲𝘀 𝗮𝗯𝗼𝘂𝘁 𝘆𝗼𝘂, 𝘁𝗿𝘆 𝗺𝗶𝘀𝘀𝗶𝗻𝗴 𝗮 𝗰𝗼𝘂𝗽𝗹𝗲 𝗼𝗳 𝗯𝗶𝗹𝗹𝘀!",
           "𝗟𝗶𝗳𝗲 𝗶𝘀 𝗹𝗶𝗸𝗲 𝗮 𝗰𝗮𝗺𝗲𝗿𝗮, 𝗳𝗼𝗰𝘂𝘀 𝗼𝗻 𝘁𝗵𝗲 𝗴𝗼𝗼𝗱 𝘁𝗶𝗺𝗲𝘀, 𝗱𝗲𝘃𝗲𝗹𝗼𝗽 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗻𝗲𝗴𝗮𝘁𝗶𝘃𝗲𝘀, 𝗮𝗻𝗱 𝗶𝗳 𝘁𝗵𝗶𝗻𝗴𝘀 𝗱𝗼𝗻'𝘁 𝘄𝗼𝗿𝗸 𝗼𝘂𝘁, 𝘁𝗮𝗸𝗲 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝘀𝗵𝗼𝘁!",
           "𝗗𝗼𝗻'𝘁 𝘄𝗼𝗿𝗿𝘆 𝗶𝗳 𝗽𝗹𝗮𝗻 𝗔 𝗳𝗮𝗶𝗹𝘀, 𝘁𝗵𝗲𝗿𝗲 𝗮𝗿𝗲 𝟮𝟱 𝗺𝗼𝗿𝗲 𝗹𝗲𝘁𝘁𝗲𝗿𝘀 𝗶𝗻 𝘁𝗵𝗲 𝗮𝗹𝗽𝗵𝗮𝗯𝗲𝘁!",
           "𝗜 𝗮𝗺 𝗮𝗹𝘄𝗮𝘆𝘀 𝗿𝗲𝗮𝗱𝘆 𝘁𝗼 𝗹𝗲𝗮𝗿𝗻, 𝗮𝗹𝘁𝗵𝗼𝘂𝗴𝗵 𝗜 𝗱𝗼 𝗻𝗼𝘁 𝗮𝗹𝘄𝗮𝘆𝘀 𝗹𝗶𝗸𝗲 𝗯𝗲𝗶𝗻𝗴 𝘁𝗮𝘂𝗴𝗵𝘁!",
           "𝗗𝗿𝗲𝗮𝗺 𝗯𝗶𝗴, 𝘄𝗼𝗿𝗸 𝗵𝗮𝗿𝗱, 𝘀𝘁𝗮𝘆 𝗳𝗼𝗰𝘂𝘀𝗲𝗱, 𝗮𝗻𝗱 𝘀𝘂𝗿𝗿𝗼𝘂𝗻𝗱 𝘆𝗼𝘂𝗿𝘀𝗲𝗹𝗳 𝘄𝗶𝘁𝗵 𝗴𝗼𝗼𝗱 𝗽𝗲𝗼𝗽𝗹𝗲!",
           "𝗜 𝗹𝗶𝗸𝗲 𝗺𝘆 𝗯𝗲𝗱𝗿𝗼𝗼𝗺 𝗹𝗶𝗸𝗲 𝗜 𝗹𝗶𝗸𝗲 𝗺𝘆 𝗹𝗶𝗳𝗲: 𝗮 𝗰𝗼𝗺𝗳𝗼𝗿𝘁𝗮𝗯𝗹𝗲 𝗺𝗲𝘀𝘀!",
           "𝗡𝗼 𝗺𝗮𝘁𝘁𝗲𝗿 𝗵𝗼𝘄 𝗺𝗮𝗻𝘆 𝗺𝗶𝘀𝘁𝗮𝗸𝗲𝘀 𝘆𝗼𝘂 𝗺𝗮𝗸𝗲 𝗼𝗿 𝗵𝗼𝘄 𝘀𝗹𝗼𝘄 𝘆𝗼𝘂 𝗽𝗿𝗼𝗴𝗿𝗲𝘀𝘀, 𝘆𝗼𝘂 𝗮𝗿𝗲 𝘀𝘁𝗶𝗹𝗹 𝗮𝗵𝗲𝗮𝗱 𝗼𝗳 𝗲𝘃𝗲𝗿𝘆𝗼𝗻𝗲 𝘄𝗵𝗼 𝗶𝘀𝗻'𝘁 𝘁𝗿𝘆𝗶𝗻𝗴!",
           "𝗧𝗵𝗲 𝗯𝗲𝘀𝘁 𝘄𝗮𝘆 𝘁𝗼 𝗳𝗶𝗻𝗶𝘀𝗵 𝗮 𝗱𝗮𝘆 𝗶𝘀 𝘄𝗶𝘁𝗵 𝗮 𝗴𝗿𝗲𝗮𝘁 𝗷𝗼𝗸𝗲 𝗮𝗻𝗱 𝗮 𝗯𝗶𝗴 𝘀𝗺𝗶𝗹𝗲!",
           "𝗪𝗵𝗲𝗻 𝗶𝗻 𝗱𝗼𝘂𝗯𝘁, 𝗮𝗱𝗱 𝗺𝗼𝗿𝗲 𝗰𝗼𝗳𝗳𝗲𝗲!",
           "𝗜 𝗱𝗼𝗻'𝘁 𝗻𝗲𝗲𝗱 𝗮 𝗽𝗶𝗿𝗮𝘁𝗲 𝗺𝗮𝗽, 𝗺𝘆 𝗰𝗮𝗿 𝗸𝗲𝘆𝘀 𝗮𝗿𝗲 𝗮𝗹𝘄𝗮𝘆𝘀 𝘁𝗿𝗲𝗮𝘀𝘂𝗿𝗲 𝗲𝗻𝗼𝘂𝗴𝗵 𝘁𝗼 𝗳𝗶𝗻𝗱!",
           "𝗜𝗳 𝘄𝗲 𝗮𝗿𝗲 𝗺𝗲𝗮𝗻𝘁 𝘁𝗼 𝘀𝘁𝗮𝘆 𝗶𝗻 𝗼𝗻𝗲 𝗽𝗹𝗮𝗰𝗲, 𝘄𝗵𝘆 𝗱𝗼 𝘁𝗵𝗲𝘆 𝗽𝘂𝘁 𝗰𝗮𝗿𝘀 𝗶𝗻 𝗺𝗼𝘁𝗶𝗼𝗻?!",
           "𝗦𝗲𝗿𝗶𝗼𝘂𝘀𝗹𝘆, 𝗹𝗮𝘂𝗴𝗵𝘁𝗲𝗿 𝗶𝘀 𝗳𝗿𝗲𝗲 𝗯𝘂𝘁 𝗽𝗿𝗶𝗰𝗲𝗹𝗲𝘀𝘀!"
        ]

SHAYARI = [ " 🌺**बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।**🌺 \n\n**🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀** ",
           " 🌺**मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।**🌺 \n\n**🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀** ",
           " 🌺**तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।**🌺 \n\n**🥀**Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.🥀** ",
           " 🌺**काश वो दिन जल्दी आए,जब तू मेरे साथ सात फेरो में बन्ध जाए।**🌺 \n\n**🥀Kash woh din jldi aaye Jb tu mere sath 7 feron me bndh jaye.🥀** ",
           " 🌺**अपना हाथ मेरे दिल पर रख दो और अपना दिल मेरे नाम कर दो।**🌺 \n\n**🥀apna hath mere dil pr rakh do aur apna dil mere naam kar do.🥀** ",
           " 🌺**महादेव ना कोई गाड़ी ना कोई बंगला चाहिए सलामत रहे मेरा प्यार बस यही दुआ चाहिए।**🌺 \n\n**🥀Mahadev na koi gadi na koi bangla chahiye salamat rhe mera pyar bas yahi dua chahiye.🥀** ",
           " 🌺**फिक्र तो होगी ना तुम्हारी इकलौती मोहब्बत हो तुम मेरी।**🌺 \n\n**🥀Fikr to hogi na tumhari ikloti mohabbat ho tum meri.🥀** ",
           " 🌺**सुनो जानू आप सिर्फ किचन संभाल लेना आप को संभालने के लिए मैं हूं ना।**🌺 \n\n**🥀suno jaanu aap sirf kitchen sambhal lena ap ko sambhlne ke liye me hun naa.🥀** ",
           " 🌺**सौ बात की एक बात मुझे चाहिए बस तेरा साथ।**🌺 \n\n**🥀So bat ki ek bat mujhe chahiye bas tera sath.🥀** ",
           " 🌺**बहुत मुश्किलों से पाया हैं तुम्हें, अब खोना नहीं चाहते,कि तुम्हारे थे तुम्हारे हैं अब किसी और के होना नहीं चाहते।**🌺 \n\n**🥀Bahut muskilon se paya hai tumhe Ab khona ni chahte ki tumhare they tumhare hai ab kisi or k hona nhi chahte.🥀** ",
           " 🌺**बेबी बातें तो रोज करते है चलो आज रोमांस करते है।**🌺 \n\n**🥀Baby baten to roj karte haichalo aaj romance karte hai..🥀** ",
           " 🌺**सुबह शाम तुझे याद करते है हम और क्या बताएं की तुमसे कितना प्यार करते है हम।**🌺 \n\n**🥀subha sham tujhe yad karte hai hum aur kya batayen ki tumse kitna pyar karte hai hum.🥀** ",
           " 🌺**किसी से दिल लग जाने को मोहब्बत नहीं कहते जिसके बिना दिल न लगे उसे मोहब्बत कहते हैं।**🌺 \n\n**🥀Kisi se dil lag jane ko mohabbat nahi kehte jiske nina dil na lage use mohabbat kehte hai.🥀** ",
           " 🌺**मेरे दिल के लॉक की चाबी हो तुम क्या बताएं जान मेरे जीने की एकलौती वजह हो तुम।**🌺 \n\n**🥀mere dil ke lock ki chabi ho tum kya batayen jaan mere jeene ki eklauti wajah ho tum..🥀** ",
           " 🌺**हम आपकी हर चीज़ से प्यार कर लेंगे, आपकी हर बात पर ऐतबार कर लेंगे, बस एक बार कह दो कि तुम सिर्फ मेरे हो, हम ज़िन्दगी भर आपका इंतज़ार कर लेंगे।**🌺 \n\n**🥀Hum apki har cheez se pyar kar lenge apki har baat par etvar kar lenge bas ek bar keh do ki tum sirf mere ho hum zindagi bhar apka intzaar kar lenge..🥀** ",
           " 🌺**मोहब्बत कभी स्पेशल लोगो से नहीं होती जिससे होती है वही स्पेशल बन जाता है।**🌺 \n\n**🥀Mohabbat kabhi special logo se nahi hoti jisse bhi hoti hai wahi special ban jate hai,.🥀**",
           " 🌺**तू मेरी जान है इसमें कोई शक नहीं तेरे अलावा मुझ पर किसी और का हक़ नहीं।**🌺 \n\n**🥀Tu meri jaan hai isme koi shak nahi tere alawa mujhe par kisi aur ka hak nhi..🥀** ",
           " 🌺**पहली मोहब्बत मेरी हम जान न सके, प्यार क्या होता है हम पहचान न सके, हमने उन्हें दिल में बसा लिया इस कदर कि, जब चाहा उन्हें दिल से निकाल न सके।**🌺 \n\n**🥀Pehli mohabbat meri hum jaan na sake pyar kya hota hai hum pehchan na sake humne unhe dil me basa liya is kadar ki jab chaha unhe dil se nikal na sake.🥀** ",
           " 🌺**खुद नहीं जानती वो कितनी प्यारी हैं , जान है हमारी पर जान से प्यारी हैं, दूरियों के होने से कोई फर्क नहीं पड़ता वो कल भी हमारी थी और आज भी हमारी है.**🌺 \n\n**🥀khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.🥀** ",
           " 🌺**चुपके से आकर इस दिल में उतर जाते हो, सांसों में मेरी खुशबु बनके बिखर जाते हो, कुछ यूँ चला है तेरे इश्क का जादू, सोते-जागते तुम ही तुम नज़र आते हो।**🌺 \n\n**🥀Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..🥀** ",
           " 🌺**प्यार करना सिखा है नफरतो का कोई ठौर नही, बस तु ही तु है इस दिल मे दूसरा कोई और नही.**🌺 \n\n**🥀Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.🥀** ",
           " 🌺**रब से आपकी खुशीयां मांगते है, दुआओं में आपकी हंसी मांगते है, सोचते है आपसे क्या मांगे,चलो आपसे उम्र भर की मोहब्बत मांगते है।**🌺\n\n**🥀Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..🥀** ",
           " 🌺**काश मेरे होंठ तेरे होंठों को छू जाए देखूं जहा बस तेरा ही चेहरा नज़र आए हो जाए हमारा रिश्ता कुछ ऐसा होंठों के साथ हमारे दिल भी जुड़ जाए.**🌺\n\n**🥀kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.🥀** ",
           " 🌺**आज मुझे ये बताने की इजाज़त दे दो, आज मुझे ये शाम सजाने की इजाज़त दे दो, अपने इश्क़ मे मुझे क़ैद कर लो,आज जान तुम पर लूटाने की इजाज़त दे दो.**🌺\n\n**🥀Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..🥀** ",
           " 🌺**जाने लोग मोहब्बत को क्या क्या नाम देते है, हम तो तेरे नाम को ही मोहब्बत कहते है.**🌺\n\n**🥀Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..🥀** ",
           " 🌺**देख के हमें वो सिर झुकाते हैं। बुला के महफिल में नजर चुराते हैं। नफरत हैं हमसे तो भी कोई बात नहीं। पर गैरो से मिल के दिल क्यों जलाते हो।**🌺\n\n**🥀Dekh Ke Hame Wo Sir Jhukate Hai Bula Ke Mahfhil Me Najar Churate Hai Nafrat Hai Hamse To Bhi Koei Bat Nhi Par Gairo Se Mil Ke Dil Kyo Jalate Ho.🥀** ",
           " 🌺**तेरे बिना टूट कर बिखर जायेंगे,तुम मिल गए तो गुलशन की तरह खिल जायेंगे, तुम ना मिले तो जीते जी ही मर जायेंगे, तुम्हें जो पा लिया तो मर कर भी जी जायेंगे।**🌺\n\n**🥀Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..🥀** ",
           " 🌺**सनम तेरी कसम जेसे मै जरूरी हूँ तेरी ख़ुशी के लिये, तू जरूरी है मेरी जिंदगी के लिये.**🌺\n\n**🥀Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.🥀** ",
           " 🌺**तुम्हारे गुस्से पर मुझे बड़ा प्यार आया हैं इस बेदर्द दुनिया में कोई तो हैं जिसने मुझे पुरे हक्क से धमकाया हैं.**🌺\n\n**🥀Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.🥀** ",
           " 🌺**पलको से आँखो की हिफाजत होती है धडकन दिल की अमानत होती है ये रिश्ता भी बडा प्यारा होता है कभी चाहत तो कभी शिकायत होती है.**🌺\n\n**🥀Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.🥀** ",
           " 🌺**मुहब्बत को जब लोग खुदा मानते हैं प्यार करने वाले को क्यों बुरा मानते हैं। जब जमाना ही पत्थर दिल हैं। फिर पत्थर से लोग क्यों दुआ मांगते है।**🌺\n\n**🥀Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.🥀** ",
           " 🌺**हुआ जब इश्क़ का एहसास उन्हें आकर वो पास हमारे सारा दिन रोते रहे हम भी निकले खुदगर्ज़ इतने यारो कि ओढ़ कर कफ़न, आँखें बंद करके सोते रहे।**🌺\n\n**🥀Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.🥀** ",
           " 🌺**दिल के कोने से एक आवाज़ आती हैं। हमें हर पल उनकी याद आती हैं। दिल पुछता हैं बार -बार हमसे के जितना हम याद करते हैं उन्हें क्या उन्हें भी हमारी याद आती हैं।**🌺\n\n**🥀Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,🥀** ",
           " 🌺**कभी लफ्ज़ भूल जाऊं कभी बात भूल जाऊं, तूझे इस कदर चाहूँ कि अपनी जात भूल जाऊं, कभी उठ के तेरे पास से जो मैं चल दूँ, जाते हुए खुद को तेरे पास भूल जाऊं।**🌺\n\n**🥀Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..🥀** ",
           " 🌺**आईना देखोगे तो मेरी याद आएगी साथ गुज़री वो मुलाकात याद आएगी पल भर क लिए वक़्त ठहर जाएगा, जब आपको मेरी कोई बात याद आएगी.**🌺\n\n**🥀Aaina dekhoge to meri yad ayegi sath guzari wo mulakat yad ayegi pal bhar ke waqt thahar jayega jab apko meri koi bat yad ayegi.🥀** ",
           " 🌺**प्यार किया तो उनकी मोहब्बत नज़र आई दर्द हुआ तो पलके उनकी भर आई दो दिलों की धड़कन में एक बात नज़र आई दिल तो उनका धड़का पर आवाज़ इस दिल की आई.**🌺\n\n**🥀Pyar kiya to unki mohabbat nazar aai dard hua to palke unki bhar aai do dilon ki dhadkan me ek baat nazar aai dil to unka dhadka par awaz dil ki aai.🥀** ",
           " 🌺**कई चेहरे लेकर लोग यहाँ जिया करते हैं हम तो बस एक ही चेहरे से प्यार करते हैं ना छुपाया करो तुम इस चेहरे को,क्योंकि हम इसे देख के ही जिया करते हैं.**🌺\n\n**🥀Kai chehre lekar log yahn jiya karte hai hum to bas ek hi chehre se pyar karte hai na chupaya karo tum is chehre ko kyuki hum ise dekh ke hi jiya karte hai.🥀** ",
           " 🌺**सबके bf को अपनी gf से बात करके नींद आजाती है और मेरे वाले को मुझसे लड़े बिना नींद नहीं आती।**🌺\n\n**🥀Sabke bf ko apni gf se baat karke nind aajati hai aur mere wale ko mujhse lade bina nind nhi aati.🥀** ",
           " 🌺**सच्चा प्यार कहा किसी के नसीब में होता है. एसा प्यार कहा इस दुनिया में किसी को नसीब होता है.**🌺\n\n**🥀Sacha pyar kaha kisi ke nasib me hota hai esa pyar kahan is duniya me kisi ko nasib hota hai.🥀** " 
           ]

TAG_ALL = [ 
          "**𝐎𝐲𝐲! 𝐊𝐚𝐡𝐚 𝐠𝐮𝐦 𝐡𝐨? 𝐀𝐚𝐨 𝐦𝐚𝐬𝐭𝐢 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢𝐧!** 😏🔥",
          "**𝐕𝐂 𝐜𝐡𝐚𝐥𝐨, 𝐭𝐡𝐨𝐝𝐚 𝐦𝐚𝐳𝐚 𝐥𝐨!** 🎧💫",
          "**𝐀𝐫𝐞𝐞! 𝐌𝐚𝐝𝐡𝐮𝐫𝐢 𝐃𝐢𝐱𝐢𝐭 𝐣𝐢𝐭𝐧𝐢 𝐦𝐮𝐬𝐤𝐚𝐧 𝐝𝐞 𝐝𝐨 𝐧𝐚!** 😜✨",
          "**𝐄𝐤 𝐩𝐢𝐜 𝐛𝐡𝐞𝐣 𝐝𝐨, 𝐦𝐢𝐥𝐤𝐞 𝐝𝐞𝐤𝐡𝐧𝐚 𝐡𝐚𝐢!** 😉📸",
          "**𝐌𝐚𝐚𝐬𝐨𝐨𝐦 𝐝𝐢𝐤𝐡𝐧𝐞 𝐤𝐢 𝐚𝐜𝐭𝐢𝐧𝐠 𝐦𝐚𝐭 𝐤𝐚𝐫, 𝐬𝐚𝐛 𝐩𝐚𝐭𝐚 𝐡𝐚𝐢!** 😏😂",
          "**𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐝𝐞𝐤𝐡𝐨 𝐨𝐫 𝐦𝐮𝐬𝐤𝐚𝐧 𝐝𝐨, 𝐝𝐢𝐥 𝐣𝐢𝐭𝐧𝐞 𝐤𝐢 𝐤𝐨𝐬𝐢𝐬𝐡 𝐡𝐨 𝐫𝐡𝐢 𝐡𝐚𝐢!** 😍💖",
          "**𝐏𝐡𝐨𝐭𝐨 𝐦𝐢𝐥 𝐣𝐚𝐭𝐢 𝐭𝐨 𝐝𝐢𝐥 𝐤𝐡𝐮𝐬𝐡 𝐡𝐨 𝐣𝐚𝐭𝐚!** 😉📷",
          "**𝐀𝐣 𝐭𝐡𝐨𝐝𝐚 𝐣𝐨𝐤𝐞𝐬 𝐬𝐮𝐧𝐚𝐮? 𝐘𝐚 𝐟𝐢𝐫 𝐡𝐚𝐬𝐧𝐞 𝐤𝐢 𝐚𝐜𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐮?** 😂😜",
          "**𝐉𝐚𝐧𝐞𝐦𝐚𝐧! 𝐀𝐚𝐣 𝐦𝐞𝐫𝐚 𝐝𝐢𝐥 𝐛𝐡𝐚𝐭𝐚𝐤 𝐫𝐡𝐚 𝐡𝐚𝐢, 𝐭𝐮𝐦𝐡𝐚𝐫𝐚 𝐡𝐢 𝐬𝐚𝐡𝐚𝐫𝐚 𝐜𝐡𝐚𝐡𝐢𝐲𝐞!** 😘❤️",
          "**𝐒𝐨𝐧𝐞 𝐬𝐞 𝐩𝐡𝐞𝐥𝐞 𝐞𝐤 𝐬𝐰𝐞𝐞𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐤𝐚 𝐢𝐧𝐭𝐳𝐚𝐫 𝐫𝐡𝐚!** 😍✨",
          "**𝐄𝐤 𝐜𝐡𝐨𝐭𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞, 𝐥𝐞𝐤𝐢𝐧 𝐛𝐨𝐡𝐨𝐭 𝐬𝐚𝐫𝐚 𝐩𝐲𝐚𝐫!** 💖🌸",
          "**𝐌𝐞𝐫𝐢 𝐦𝐚𝐬𝐮𝐦𝐢𝐭 𝐤𝐢 𝐪𝐚𝐬𝐚𝐦, 𝐣𝐨𝐨𝐭𝐡 𝐦𝐚𝐭 𝐛𝐨𝐥𝐧𝐚, 𝐦𝐚𝐢𝐧 𝐤𝐚𝐢𝐬𝐢 𝐥𝐚𝐠𝐭𝐢 𝐡𝐮𝐧?** 😉💫",
          "**𝐊𝐚𝐛𝐡𝐢 𝐤𝐚𝐛𝐡𝐢 𝐭𝐨 𝐬𝐨𝐜𝐡𝐨, 𝐦𝐞𝐫𝐚 𝐛𝐡𝐢 𝐝𝐢𝐥 𝐡𝐚𝐢, 𝐭𝐮𝐦𝐡𝐚𝐫𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐤𝐚 𝐢𝐧𝐭𝐳𝐚𝐫 𝐤𝐚𝐫𝐭𝐚 𝐡𝐨𝐠𝐚!** 🥺💙",
          "**𝐏𝐡𝐨𝐧𝐞 𝐮𝐭𝐡𝐚𝐨 𝐧𝐚! 𝐌𝐚𝐢 𝐲𝐡𝐚𝐚𝐧 𝐞𝐤 𝐡𝐢𝐧𝐭 𝐝𝐞 𝐫𝐡𝐚 𝐡𝐮!** 😏☎️",
          "**𝐄𝐤 𝐬𝐦𝐢𝐥𝐞 𝐝𝐨, 𝐝𝐢𝐧 𝐛𝐚𝐧 𝐣𝐚𝐲𝐞𝐠𝐚!** 😊💖",
          "**𝐀𝐛 𝐦𝐢𝐬𝐬 𝐛𝐡𝐢 𝐤𝐚𝐫𝐨 𝐤𝐚𝐛𝐡𝐢! 𝐊𝐚𝐦 𝐬𝐞 𝐤𝐚𝐦 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐤𝐚𝐫 𝐬𝐚𝐤𝐭𝐞 𝐡𝐨!** 😜📩",
          "**𝐀𝐣 𝐦𝐨𝐨𝐝 𝐛𝐨𝐡𝐨𝐭 𝐚𝐜𝐡𝐚 𝐡𝐚𝐢, 𝐜𝐡𝐚𝐥𝐨 𝐤𝐨𝐢 𝐝𝐡𝐚𝐦𝐚𝐥 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢𝐧!** 🎉🤩",
          "**𝐒𝐮𝐧𝐨! 𝐁𝐡𝐚𝐯 𝐦𝐞 𝐫𝐚𝐡𝐨, 𝐦𝐚𝐢 𝐦𝐚𝐬𝐭𝐢 𝐤𝐞 𝐦𝐨𝐨𝐝 𝐦𝐞 𝐡𝐮!** 😉🔥",
          "**𝐊𝐢𝐭𝐧𝐚 𝐜𝐡𝐮𝐩 𝐫𝐡𝐨𝐠𝐞? 𝐄𝐤 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐛𝐡𝐞𝐣 𝐝𝐨 𝐧𝐚!** 🥺💌",
          "**𝐀𝐚𝐣 𝐫𝐚𝐚𝐭 𝐤𝐨 𝐝𝐞𝐞𝐩 𝐜𝐨𝐧𝐯𝐨 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢𝐧! 𝐊𝐲𝐚 𝐤𝐡𝐚𝐲𝐚𝐥 𝐡𝐚𝐢?** 🤔💬",
          "**𝐘𝐚𝐫𝐞! 𝐌𝐚𝐢 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐝𝐞𝐤𝐡 𝐫𝐡𝐚 𝐡𝐨𝐨𝐧, 𝐫𝐞𝐩𝐥𝐲 𝐦𝐚𝐭 𝐝𝐨 𝐦𝐚𝐭𝐥𝐚𝐛!** 😏😂",
          "**𝐎𝐲𝐲! 𝐊𝐚𝐡𝐚 𝐠𝐮𝐦 𝐡𝐨? 𝐀𝐚𝐨 𝐦𝐚𝐬𝐭𝐢 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢𝐧!** 😏🔥",
          "**𝐕𝐂 𝐜𝐡𝐚𝐥𝐨, 𝐭𝐡𝐨𝐝𝐚 𝐦𝐚𝐳𝐚 𝐥𝐨!** 🎧💫",
          "**𝐀𝐫𝐞𝐞! 𝐌𝐚𝐝𝐡𝐮𝐫𝐢 𝐃𝐢𝐱𝐢𝐭 𝐣𝐢𝐭𝐧𝐢 𝐦𝐮𝐬𝐤𝐚𝐧 𝐝𝐞 𝐝𝐨 𝐧𝐚!** 😜✨",
          "**𝐄𝐤 𝐩𝐢𝐜 𝐛𝐡𝐞𝐣 𝐝𝐨, 𝐦𝐢𝐥𝐤𝐞 𝐝𝐞𝐤𝐡𝐧𝐚 𝐡𝐚𝐢!** 😉📸",
          "**𝐌𝐚𝐚𝐬𝐨𝐨𝐦 𝐝𝐢𝐤𝐡𝐧𝐞 𝐤𝐢 𝐚𝐜𝐭𝐢𝐧𝐠 𝐦𝐚𝐭 𝐤𝐚𝐫, 𝐬𝐚𝐛 𝐩𝐚𝐭𝐚 𝐡𝐚𝐢!** 😏😂",
          "**𝐌𝐮𝐡 𝐝𝐡𝐨 𝐥𝐨, 𝐦𝐮𝐬𝐤𝐚𝐧 𝐚𝐚 𝐣𝐚𝐲𝐞𝐠𝐢!** 😁🪞",
          "**𝐀𝐫𝐞𝐞! 𝐄𝐤 𝐜𝐡𝐨𝐭𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐤𝐚𝐫 𝐝𝐨, 𝐝𝐢𝐥 𝐛𝐞𝐡𝐥 𝐣𝐚𝐲𝐞!** 📩❤️",
          "**𝐇𝐚𝐬 𝐝𝐨 𝐣𝐢, 𝐥𝐨𝐠 𝐬𝐨𝐜𝐡𝐞𝐧𝐠𝐞 𝐤𝐢 𝐤𝐮𝐜𝐡 𝐚𝐜𝐡𝐚 𝐡𝐨 𝐠𝐲𝐚!** 😂🔥",
          "**𝐂𝐡𝐚𝐥𝐨 𝐭𝐡𝐨𝐝𝐚 𝐦𝐚𝐬𝐭𝐢 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢𝐧, 𝐧𝐚𝐡𝐢 𝐭𝐨 𝐛𝐨𝐫𝐢𝐧𝐠 𝐳𝐢𝐧𝐝𝐚𝐠𝐢 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢!** 🎉😎",
          "**𝐀𝐣 𝐬𝐚𝐦𝐚𝐧𝐞 𝐬𝐞 𝐞𝐤 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐚𝐲𝐚 𝐭𝐨 𝐛𝐚𝐭𝐚𝐮𝐧 𝐤𝐲𝐚 𝐦𝐚𝐬𝐭 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢!** 🤩💬",
          "**𝐒𝐨𝐧𝐞 𝐬𝐞 𝐩𝐡𝐞𝐥𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐤𝐚 𝐢𝐧𝐭𝐳𝐚𝐫 𝐫𝐡𝐚, 𝐦𝐚𝐠𝐚𝐫 𝐭𝐮𝐦 𝐛𝐢𝐠𝐚𝐝𝐞 𝐧𝐢𝐤𝐥𝐞!** 😜💤",
          "**𝐉𝐢𝐧𝐝𝐚𝐠𝐢 𝐬𝐞 𝐣𝐚𝐥𝐝𝐢 𝐩𝐚𝐫𝐞𝐬𝐡𝐚𝐧 𝐦𝐚𝐭 𝐡𝐨, 𝐦𝐞𝐦𝐞 𝐝𝐞𝐤𝐡𝐨 𝐚𝐮𝐫 𝐦𝐮𝐬𝐤𝐚𝐧 𝐝𝐨!** 😂💖",
          "**𝐊𝐚𝐛𝐡𝐢 𝐦𝐢𝐥 𝐛𝐡𝐢 𝐥𝐢𝐲𝐚 𝐜𝐚𝐫𝐨 𝐲𝐚𝐚𝐫, 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐬𝐞 𝐤𝐲𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢!** 😉🤝",
          "**𝐊𝐮𝐜𝐡 𝐦𝐚𝐬𝐭 𝐩𝐥𝐚𝐧 𝐛𝐚𝐧𝐚𝐭𝐞 𝐡𝐚𝐢𝐧, 𝐣𝐨 𝐛𝐚𝐝𝐦𝐞 𝐤𝐡𝐮𝐝 𝐡𝐢 𝐜𝐚𝐧𝐜𝐞𝐥 𝐤𝐚𝐫 𝐝𝐞𝐧𝐠𝐞!** 😆🔥",
          "**𝐌𝐮𝐬𝐤𝐚𝐧 𝐝𝐞𝐤𝐡𝐤𝐚𝐫 𝐡𝐢 𝐬𝐚𝐛 𝐬𝐞𝐭 𝐡𝐨 𝐣𝐚𝐭𝐚 𝐡𝐚𝐢!** 😊✨",
          "**𝐏𝐚𝐫𝐞𝐬𝐡𝐚𝐧 𝐦𝐚𝐭 𝐡𝐨, 𝐛𝐚𝐬 𝐦𝐮𝐣𝐡𝐞 𝐞𝐤 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐝𝐞𝐝𝐨!** 💬💖",
          "**𝐀𝐛 𝐢𝐭𝐧𝐢 𝐢𝐧𝐭𝐳𝐚𝐫 𝐧𝐚 𝐤𝐚𝐫𝐨, 𝐛𝐬 𝐞𝐤 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐛𝐡𝐞𝐣 𝐝𝐨!** 😍📨",
          "**𝐀𝐩𝐧𝐞 𝐩𝐡𝐨𝐭𝐨 𝐛𝐡𝐞𝐣𝐧𝐞 𝐤𝐚 𝐬𝐨𝐜𝐡𝐚, 𝐦𝐚𝐠𝐚𝐫 𝐡𝐨𝐬𝐡 𝐮𝐝 𝐣𝐚𝐭𝐞 𝐡𝐚𝐢𝐧!** 😂📸",
          "**𝐀𝐛 𝐬𝐞𝐫𝐢𝐨𝐮𝐬 𝐧𝐚 𝐡𝐨, 𝐣𝐨𝐤𝐞𝐬 𝐬𝐮𝐧𝐨 𝐚𝐮𝐫 𝐡𝐚𝐬𝐨!** 😆🎭",
          "**𝐀𝐫𝐞 𝐬𝐮𝐧𝐨, 𝐡𝐚𝐬 𝐛𝐡𝐢 𝐥𝐢𝐲𝐚 𝐤𝐚𝐫𝐨, 𝐧𝐚𝐡𝐢 𝐭𝐨 𝐥𝐨𝐠 𝐬𝐨𝐜𝐡𝐞𝐧𝐠𝐞 𝐤𝐢 𝐛𝐢𝐥𝐥 𝐛𝐡𝐚𝐫𝐧𝐞 𝐤𝐚 𝐝𝐮𝐤𝐡 𝐡𝐚𝐢!** 😂🔥",
          "**𝐕𝐂 𝐜𝐡𝐚𝐥𝐨, 𝐦𝐚𝐳𝐞 𝐤𝐢 𝐛𝐚𝐭𝐞𝐧 𝐡𝐨𝐧𝐠𝐢!** 🎤😏",
          "**𝐎𝐲𝐲! 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐝𝐞𝐤𝐡𝐨 𝐦𝐞𝐫𝐚, 𝐤𝐨𝐢 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐚𝐚𝐲𝐚 𝐡𝐚𝐢!** 😜📩",
          "**𝐀𝐛𝐞 𝐦𝐮𝐬𝐤𝐚𝐧 𝐭𝐡𝐨𝐝𝐚 𝐚𝐜𝐡𝐞 𝐬𝐞 𝐝𝐞𝐧𝐚, 𝐥𝐨𝐠 𝐬𝐨𝐜𝐡𝐧𝐚 𝐛𝐚𝐧𝐝 𝐤𝐚𝐫 𝐝𝐞𝐧𝐠𝐞!** 😂🔥",
          "**𝐉𝐚𝐧𝐞 𝐤𝐚 𝐧𝐚𝐚𝐦 𝐦𝐚𝐭 𝐥𝐨, 𝐦𝐚𝐫𝐝 𝐡𝐚𝐢𝐧 𝐣𝐢, 𝐝𝐢𝐥 𝐧𝐚𝐳𝐮𝐤 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢!** 😆❤️",
          "**𝐊𝐚𝐡𝐚 𝐠𝐮𝐦 𝐡𝐨, 𝐬𝐨𝐜𝐢𝐚𝐥 𝐦𝐞𝐝𝐢𝐚 𝐩𝐚𝐫 𝐝𝐡𝐮𝐧𝐝 𝐫𝐡𝐚 𝐭𝐡𝐚 𝐭𝐮𝐦𝐡𝐞!** 🔍😂",
          "**𝐀𝐣 𝐢𝐬𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐬𝐞 𝐤𝐨𝐢 𝐜𝐡𝐞𝐞𝐳 𝐚𝐜𝐡𝐡𝐢 𝐡𝐨 𝐣𝐚𝐚𝐲𝐞!** 🤞🔥",
          "**𝐌𝐚𝐫𝐨 𝐦𝐚𝐭, 𝐦𝐚𝐳𝐚𝐚𝐤 𝐭𝐡𝐚 𝐦𝐞𝐫𝐚!** 😅😂",
          "**𝐃𝐨𝐬𝐭𝐢 𝐦𝐚𝐳𝐚𝐚𝐤 𝐛𝐡𝐚𝐫𝐢 𝐡𝐨𝐭𝐢 𝐡𝐚𝐢, 𝐦𝐚𝐠𝐚𝐫 𝐦𝐮𝐡 𝐦𝐞𝐭𝐡𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢!** 😆🍬",
          "**𝐏𝐡𝐨𝐭𝐨 𝐝𝐞𝐤𝐡𝐤𝐞 𝐡𝐚𝐫 𝐛𝐚𝐫 𝐩𝐲𝐚𝐫 𝐡𝐨𝐣𝐚𝐭𝐚 𝐡𝐚𝐢, 𝐲𝐞 𝐜𝐡𝐚𝐥 𝐤𝐲𝐚 𝐫𝐡𝐚 𝐡𝐚𝐢!** 🤩📸",
          "**𝐓𝐡𝐨𝐝𝐚 𝐡𝐚𝐬 𝐥𝐨, 𝐣𝐢𝐧𝐝𝐚𝐠𝐢 𝐥𝐨𝐧𝐠 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢!** 😁🔥",
          "**𝐀𝐣 𝐤𝐨𝐢 𝐚𝐚𝐜𝐡𝐢 𝐛𝐚𝐚𝐭 𝐤𝐚𝐫𝐨, 𝐦𝐚𝐫 𝐣𝐚𝐮𝐧𝐠𝐚 𝐡𝐚𝐬𝐭𝐞 𝐡𝐚𝐬𝐭𝐞!** 🤣😂",
          "**𝐃𝐢𝐥 𝐬𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐚𝐲𝐚 𝐭𝐡𝐚, 𝐚𝐛 𝐣𝐚𝐚𝐧 𝐦𝐞𝐢𝐧 𝐣𝐚𝐚𝐧 𝐚𝐚 𝐠𝐲𝐢!** 😍🔥",
          "**𝐊𝐡𝐚𝐭𝐚𝐦 𝐡𝐨𝐠𝐚𝐲𝐚 𝐝𝐨𝐬𝐭𝐢 𝐤𝐚 𝐫𝐢𝐬𝐡𝐭𝐚, 𝐣𝐚𝐛 𝐭𝐮𝐦𝐡𝐞 𝐚𝐚𝐬𝐭𝐢𝐧 𝐦𝐞 𝐦𝐨𝐡𝐚𝐛𝐛𝐚𝐭 𝐦𝐢𝐥𝐠𝐲𝐢!** 😏🔥",
          "**𝐏𝐡𝐨𝐭𝐨 𝐤𝐢𝐭𝐧𝐢 𝐚𝐚𝐜𝐡𝐢 𝐡𝐨, 𝐦𝐚𝐠𝐚𝐫 𝐭𝐮 𝐡𝐚𝐫 𝐛𝐚𝐫 𝐝𝐢𝐥 𝐥𝐨𝐨𝐭 𝐥𝐞𝐭𝐚 𝐡𝐚𝐢!** 😆🔥",
          "**𝐂𝐡𝐚𝐥𝐨 𝐯𝐜 𝐦𝐞 𝐦𝐞𝐞𝐭 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢𝐧, 𝐛𝐚𝐭𝐞𝐧 𝐬𝐚𝐦𝐧𝐞 𝐤𝐢 𝐚𝐜𝐡𝐢 𝐡𝐨𝐭𝐢 𝐡𝐚𝐢!** 🎙️😊",
          "**𝐀𝐫𝐞 𝐲𝐚𝐚𝐫! 𝐌𝐮𝐬𝐤𝐚𝐧 𝐛𝐚𝐧𝐚𝐲𝐞 𝐫𝐚𝐡𝐨, 𝐣𝐢𝐧𝐝𝐚𝐠𝐢 𝐚𝐚𝐬𝐚𝐧 𝐡𝐨𝐣𝐚𝐲𝐞𝐠𝐢!** 😊✨",
          "**𝐊𝐚𝐛𝐡𝐢 𝐣𝐚𝐧𝐞 𝐤𝐢 𝐛𝐚𝐚𝐭 𝐧𝐚 𝐤𝐚𝐫𝐨, 𝐝𝐨𝐬𝐭𝐨𝐧 𝐤𝐨 𝐝𝐢𝐥 𝐭𝐨𝐝𝐧𝐞 𝐤𝐢 𝐚𝐚𝐝𝐭 𝐧𝐚𝐡𝐢!** 😜🤞",
          "**𝐀𝐩𝐧𝐞 𝐥𝐢𝐲𝐞 𝐣𝐞𝐞𝐭𝐞 𝐫𝐚𝐡𝐨, 𝐣𝐢𝐧𝐝𝐚𝐠𝐢 𝐬𝐞 𝐩𝐲𝐚𝐚𝐫 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐚!** ❤️🔥",
          "**𝐀𝐫𝐞 𝐬𝐮𝐧𝐨, 𝐡𝐚𝐬 𝐛𝐡𝐢 𝐥𝐢𝐲𝐚 𝐤𝐚𝐫𝐨, 𝐧𝐚𝐡𝐢 𝐭𝐨 𝐥𝐨𝐠 𝐬𝐨𝐜𝐡𝐞𝐧𝐠𝐞 𝐤𝐢 𝐛𝐢𝐥𝐥 𝐛𝐡𝐚𝐫𝐧𝐞 𝐤𝐚 𝐝𝐮𝐤𝐡 𝐡𝐚𝐢!** 😂🔥",
          "**𝐕𝐂 𝐜𝐡𝐚𝐥𝐨, 𝐦𝐚𝐳𝐞 𝐤𝐢 𝐛𝐚𝐭𝐞𝐧 𝐡𝐨𝐧𝐠𝐢!** 🎤😏",
          "**𝐎𝐲𝐲! 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐝𝐞𝐤𝐡𝐨 𝐦𝐞𝐫𝐚, 𝐤𝐨𝐢 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐚𝐚𝐲𝐚 𝐡𝐚𝐢!** 😜📩",
          "**𝐀𝐛𝐞 𝐦𝐮𝐬𝐤𝐚𝐧 𝐭𝐡𝐨𝐝𝐚 𝐚𝐜𝐡𝐞 𝐬𝐞 𝐝𝐞𝐧𝐚, 𝐥𝐨𝐠 𝐬𝐨𝐜𝐡𝐧𝐚 𝐛𝐚𝐧𝐝 𝐤𝐚𝐫 𝐝𝐞𝐧𝐠𝐞!** 😂🔥",
          "**𝐉𝐚𝐧𝐞 𝐤𝐚 𝐧𝐚𝐚𝐦 𝐦𝐚𝐭 𝐥𝐨, 𝐦𝐚𝐫𝐝 𝐡𝐚𝐢𝐧 𝐣𝐢, 𝐝𝐢𝐥 𝐧𝐚𝐳𝐮𝐤 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢!** 😆❤️",
          "**𝐊𝐚𝐡𝐚 𝐠𝐮𝐦 𝐡𝐨, 𝐬𝐨𝐜𝐢𝐚𝐥 𝐦𝐞𝐝𝐢𝐚 𝐩𝐚𝐫 𝐝𝐡𝐮𝐧𝐝 𝐫𝐡𝐚 𝐭𝐡𝐚 𝐭𝐮𝐦𝐡𝐞!** 🔍😂",
          "**𝐊𝐚𝐡𝐢𝐧 𝐭𝐮𝐦 𝐠𝐚𝐲𝐚𝐛 𝐭𝐨 𝐧𝐚𝐡𝐢 𝐡𝐨 𝐠𝐲𝐞? 𝐀𝐩𝐧𝐚 𝐦𝐮𝐡 𝐝𝐢𝐤𝐡𝐚𝐨!** 😆",
          "**𝐌𝐨𝐣 𝐤𝐫𝐨, 𝐝𝐮𝐧𝐢𝐲𝐚 𝐛𝐡𝐢 𝐦𝐚𝐚𝐫𝐨 𝐠𝐢𝐥𝐚!** 😜🔥",
          "**𝐀𝐩𝐧𝐞 𝐦𝐨𝐨𝐝 𝐬𝐞 𝐦𝐨𝐦𝐨𝐬 𝐧𝐚𝐡𝐢 𝐛𝐧𝐚𝐨, 𝐡𝐚𝐦𝐞𝐬𝐡𝐚 𝐚𝐚𝐜𝐡𝐚 𝐫𝐚𝐤𝐡𝐨!** 😂🥟",
          "**𝐂𝐡𝐚𝐢 𝐬𝐞 𝐣𝐲𝐚𝐝𝐚 𝐚𝐮𝐫 𝐝𝐨𝐬𝐭𝐨𝐧 𝐬𝐞 𝐤𝐚𝐦 𝐩𝐲𝐚𝐫 𝐡𝐨 𝐡𝐢 𝐧𝐚𝐡𝐢 𝐬𝐚𝐤𝐭𝐚!** ☕❤️",
          "**𝐍𝐨𝐧-𝐬𝐭𝐨𝐩 𝐡𝐚𝐬𝐨, 𝐜𝐡𝐢𝐧𝐭𝐚 𝐤𝐡𝐚𝐭𝐚𝐦 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢!** 😂🔥",
          "**𝐘𝐞 𝐝𝐮𝐧𝐢𝐲𝐚 𝐝𝐞𝐤𝐡 𝐥𝐞𝐤𝐢𝐧 𝐚𝐩𝐧𝐢 𝐦𝐚𝐬𝐭𝐢 𝐣𝐚𝐫𝐢 𝐫𝐚𝐤𝐡𝐨!** 😆🔥",
          "**𝐀𝐫𝐞 𝐝𝐨𝐬𝐭𝐨𝐧 𝐤𝐚 𝐩𝐲𝐚𝐫 𝐡𝐚𝐢, 𝐛𝐚𝐭𝐭𝐢 𝐛𝐧𝐝 𝐤𝐚𝐫 𝐤𝐞 𝐬𝐨𝐧𝐚 𝐦𝐚𝐭!** 😂😂",
          "**𝐁𝐢𝐣𝐥𝐢 𝐣𝐢𝐭𝐧𝐚 𝐣𝐡𝐚𝐭𝐤𝐚 𝐦𝐚𝐭 𝐝𝐨, 𝐣𝐨𝐤𝐞 𝐣𝐚𝐝𝐚 𝐝𝐨!** ⚡😂",
          "**𝐉𝐨 𝐛𝐡𝐢 𝐡𝐨, 𝐚𝐩𝐧𝐚 𝐝𝐚𝐲 𝐛𝐞𝐬𝐭 𝐛𝐧𝐚𝐨!** 😊🔥",
          "**𝐃𝐢𝐥 𝐬𝐞 𝐬𝐮𝐧𝐨, 𝐝𝐨𝐬𝐭𝐨𝐧 𝐤𝐨 𝐧𝐚 𝐜𝐡𝐨𝐝𝐨!** ❤️🔥",
          "**𝐁𝐚𝐡𝐚𝐧𝐞 𝐛𝐚𝐧𝐚𝐧𝐚 𝐛𝐚𝐧𝐝 𝐤𝐚𝐫𝐨, 𝐦𝐚𝐳𝐚 𝐮𝐭𝐡𝐚𝐨!** 😆🔥",
          "**𝐂𝐡𝐢𝐥𝐥 𝐤𝐚𝐫𝐨, 𝐤𝐚𝐡𝐢𝐧 𝐳𝐲𝐚𝐝𝐚 𝐬𝐨𝐜𝐡 𝐧𝐚 𝐣𝐚𝐨!** 😎🔥",
          "**𝐀𝐩𝐧𝐞 𝐝𝐢𝐥 𝐬𝐞 𝐣𝐢𝐨, 𝐬𝐚𝐛 𝐛𝐚𝐝𝐡𝐢𝐲𝐚 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐚!** ❤️🔥",
          "**𝐂𝐡𝐨𝐭𝐢 𝐜𝐡𝐨𝐭𝐢 𝐛𝐚𝐭𝐨𝐧 𝐦𝐞 𝐦𝐨𝐣 𝐝𝐡𝐮𝐧𝐝𝐨!** 😁🔥"
]

        ]


async def is_user_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)
    except UserNotParticipant:
        return False


@app.on_message(filters.command(["gntag"], prefixes=["/", "!"]))
async def mention_all_gn(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 🚨 This command can only be used in groups! 🚨.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ **Oops! You're not an admin, baby!** Only admins can tag members.")

    if chat_id in spam_chats:
        return await message.reply("๏ ⚠ Please stop the running mention process first before using this command! 🚫...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(GN_MESSAGES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["gmtag"], prefixes=["/", "!"]))
async def mention_all_gm(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 🚨 This command can only be used in groups! 🚨.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ **Oops! You're not an admin, baby!** Only admins can tag members.")

    if chat_id in spam_chats:
        return await message.reply("๏ ⚠ Please stop the running mention process first before using this command! 🚫...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(GM_MESSAGES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["hitag"], prefixes=["/", "!"]))
async def mention_all_hi(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 🚨 This command can only be used in groups! 🚨.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ **Oops! You're not an admin, baby!** Only admins can tag members.")

    if chat_id in spam_chats:
        return await message.reply("๏ ⚠ Please stop the running mention process first before using this command! 🚫...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(HI_MESSAGES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["lifetag"], prefixes=["/", "!"]))
async def mention_all_quotes(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 🚨 This command can only be used in groups! 🚨.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ **Oops! You're not an admin, baby!** Only admins can tag members.")

    if chat_id in spam_chats:
        return await message.reply("๏ ⚠ Please stop the running mention process first before using this command! 🚫...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(QUOTES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["shayari"], prefixes=["/", "!"]))
async def mention_all_shayari(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 🚨 This command can only be used in groups! 🚨.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ **Oops! You're not an admin, baby!** Only admins can tag members.")

    if chat_id in spam_chats:
        return await message.reply("๏ ⚠ Please stop the running mention process first before using this command! 🚫...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(SHAYARI)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["tagall"], prefixes=["/", "!"]))
async def mention_all_tagall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 🚨 This command can only be used in groups! 🚨.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ **Oops! You're not an admin, baby!** Only admins can tag members.")

    if chat_id in spam_chats:
        return await message.reply("๏ ⚠ Please stop the running mention process first before using this command! 🚫...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(TAG_ALL)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["gmstop", "gnstop", "histop", "lifestop", "shayarioff", "tagoff", "tagstop"], prefixes=["/", "!"]))
async def cancel_mention(client, message):
    chat_id = message.chat.id
    if not chat_id in spam_chats:
        return await message.reply("๏ **Tagging is currently disabled.**")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ **Oops! You're not an admin, baby!** Only admins can tag members.")

    spam_chats.remove(chat_id)
    await message.reply("๏ 🦋Mention Rokne wale ki maa ka Bharosa Jeetu.....🫠 ๏")
