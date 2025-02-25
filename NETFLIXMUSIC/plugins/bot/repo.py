from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NETFLIXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ 𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙉𝙚𝙩𝙛𝙡𝙞𝙭 𝙍𝙚𝙥𝙤𝙨 ✪

➲ Easily deploy all repositories on Heroku without errors ✰  
➲ No Heroku ban issues ✰  
➲ No ID ban issues ✰  
➲ Unlimited dynos ✰  
➲ Runs 24/7 with zero lag ✰  

► If you face any issues, feel free to share a screenshot!  
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("Add Me Babes✪", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("Owner", url="https://t.me/Shrushthi_25"),
             InlineKeyboardButton("Support", url="https://t.me/Beats_Support"),
             ],
     
             [
             InlineKeyboardButton("Support ᴄʜᴀᴛ", url="https://t.me/Beat_Support"),          
             InlineKeyboardButton("Music", url=f"https://github.com/Shruti1447/NETFLIXMUSIC"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/tLx.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
