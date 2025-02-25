from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend([
    InlineQueryResultArticle(
        title="⏸ Pause",
        description="Pause the currently playing stream on video chat.",
        thumb_url="https://envs.sh/tlN.jpg",
        input_message_content=InputTextMessageContent("/pause"),
    ),
    InlineQueryResultArticle(
        title="▶️ Resume",
        description="Resume the paused stream on video chat.",
        thumb_url="https://envs.sh/tlH.jpg",
        input_message_content=InputTextMessageContent("/resume"),
    ),
    InlineQueryResultArticle(
        title="⏭ Skip",
        description="Skip the currently playing stream and move to the next one.",
        thumb_url="https://envs.sh/tlg.jpg",
        input_message_content=InputTextMessageContent("/skip"),
    ),
    InlineQueryResultArticle(
        title="🛑 End",
        description="End the currently playing stream on video chat.",
        thumb_url="https://envs.sh/tlm.jpg",
        input_message_content=InputTextMessageContent("/end"),
    ),
    InlineQueryResultArticle(
        title="🔀 Shuffle",
        description="Shuffle the queued songs in the playlist.",
        thumb_url="https://envs.sh/tlM.jpg",
        input_message_content=InputTextMessageContent("/shuffle"),
    ),
    InlineQueryResultArticle(
        title="🔁 Loop",
        description="Loop the currently playing track on video chat.",
        thumb_url="https://envs.sh/tly.jpg",
        input_message_content=InputTextMessageContent("/loop 3"),
    ),
])