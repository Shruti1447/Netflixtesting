import math
import time
from typing import Union
from pyrogram.types import InlineKeyboardButton
from NETFLIXMUSIC.utils.formatters import time_to_seconds
from NETFLIXMUSIC import app

LAST_UPDATE_TIME = {}

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ), 
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐑𝐞𝐩𝐥𝐚𝐲 🔄",
                callback_data=f"ADMIN Replay|{user_id}"
            ),
            InlineKeyboardButton(
                text="⏹ 𝐒𝐭𝐨𝐩",
                callback_data=f"ADMIN Stop|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ 𝐌𝐨𝐫𝐞 ๏",
                callback_data=f"PanelMarkup None|{user_id}",
            ),
        ],
    ]
    return buttons

def should_update_progress(chat_id):
    current_time = time.time()
    last_update = LAST_UPDATE_TIME.get(chat_id, 0)
    if current_time - last_update >= 6:
        LAST_UPDATE_TIME[chat_id] = current_time
        return True
    return False

def generate_progress_bar(played_sec, duration_sec):
    if duration_sec == 0:
        percentage = 0
    else:
        percentage = (played_sec / duration_sec) * 100
    percentage = min(percentage, 100)

    bar_length = 12
    filled_length = int(round(bar_length * percentage / 100))

    bar = '▰' * filled_length + '▱' * (bar_length - filled_length)
    return bar

def stream_markup_timer(_, chat_id, played, dur):
    if not should_update_progress(chat_id):
        return None

    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)

    bar = generate_progress_bar(played_sec, duration_sec)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="⏩ 𝐑𝐞𝐬𝐮𝐦𝐞",
                callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⏸ 𝐏𝐚𝐮𝐬𝐞",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𝐒𝐤𝐢𝐩 ⏭",
                callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏹ 𝐒𝐭𝐨𝐩",
                callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝐑𝐞𝐩𝐥𝐚𝐲 🔄",
                callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ 𝐌𝐨𝐫𝐞 ๏",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
    ]
    return buttons

def telegram_markup_timer(_, chat_id, played, dur):
    if not should_update_progress(chat_id):
        return None

    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)

    bar = generate_progress_bar(played_sec, duration_sec)

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="⏩ 𝐑𝐞𝐬𝐮𝐦𝐞",
                callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⏸ 𝐏𝐚𝐮𝐬𝐞",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𝐒𝐤𝐢𝐩 ⏭",
                callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏹ 𝐒𝐭𝐨𝐩",
                callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝐑𝐞𝐩𝐥𝐚𝐲 🔄",
                callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ 𝐌𝐨𝐫𝐞 ๏",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
    ]
    return buttons

def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏩ 𝐑𝐞𝐬𝐮𝐦𝐞",
                callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⏸ 𝐏𝐚𝐮𝐬𝐞",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𝐒𝐤𝐢𝐩 ⏭",
                callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="⏹ 𝐒𝐭𝐨𝐩",
                callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝐑𝐞𝐩𝐥𝐚𝐲 🔄",
                callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ 𝐌𝐨𝐫𝐞 ๏",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
    ]

    return buttons

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"SHRUSHTHIPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"SHRUSHTHIPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}"
            ),
        ],
    ]
    return buttons

def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}"
            ),
        ],
    ]
    return buttons

def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="⏩",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="๏ 𝐍𝐞𝐱𝐭 ๏",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close"
            ),
        ],
    ]
    return buttons


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏸ 𝐏𝐚𝐮𝐬𝐞",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏹ 𝐒𝐭𝐨𝐩",
                callback_data=f"ADMIN Stop|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝐒𝐤𝐢𝐩 ⏭",
                callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏩ 𝐑𝐞𝐬𝐮𝐦𝐞",
                callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="𝐑𝐞𝐩𝐥𝐚𝐲 🔄",
                callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⌜๏ 𝐌𝐎𝐑𝐄 ๏⌟",
                callback_data=f"PanelMarkup None|{chat_id}"
            ),
        ],
    ]
    return buttons

def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ 🎶 𝐀𝐝𝐝 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐲𝐥𝐢𝐬𝐭 🎶 ✚",
                callback_data=f"add_playlist {videoid}"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎧 𝐒𝐮𝐟𝐟𝐥𝐞",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𝐋𝐨𝐨𝐩 🔄",
                callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏪ 10 𝐒𝐞𝐜",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="10 𝐒𝐞𝐜 ⏩",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🏠 𝐇𝐨𝐦𝐞 ",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            )   
        ]
    ]
    return buttons