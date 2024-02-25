import time 
import random 
import asyncio
import config
from config import HANDLER, OWNER_ID, BARATH,SOURCE
from pyrogram import filters, __version__ as pyrover, enums
from Barath import barath, get_readable_time, StartTime
from Barath import bot, MODULE

async def alive():
    start_time = time.time()
    katsuki = "3.01"
    user = await barath.get_me()
    name = user.first_name
    username = user.username
    user_profile_link = f"https://t.me/{username}" if username else ""
    user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
    dbhealth = "ᴡᴏʀᴋɪɴɢ"
    uptime = get_readable_time((time.time() - StartTime))
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    
    ALIVE_TEX = "ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴍᴀꜱᴛᴇʀ"
    EMOTES = ["😍", "💀", "😊", "👋", "🎉", "🔥", "🌟", "💫", "🚀", "🤖", "👻", "👾", "🧡"]

    photo_url = "https://telegra.ph/file/e90d5a6fcca486f10025b.mp4"
    
    ALIVE_TEXT = f"""{ALIVE_TEX}
▰▱▰▱▰▱▰▱▰▱▰▱▰

➤ <b>ꜱᴛᴀᴛᴜꜱ:</b> {dbhealth}
➤ <b>ᴠᴇʀꜱɪᴏɴ:</b> {katsuki}
➤ <b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}
➤ <b>ᴘɪɴɢ:</b> {ping_time} ms
➤ <b>Python:</b> {pyrover}

<b>ᴜꜱᴇʀʙᴏᴛ</b> {user_hyperlink}

<b>Source: <a href='{SOURCE}'>PyroX-V2</a></b>"""


    return ALIVE_TEXT, photo_url

@barath.on_message(filters.command("alive", prefixes=HANDLER) & filters.me)
async def chk_alive(_, message):
    msg = await message.reply_text("Checking...")
    try:
        alive_text, photo_url = await alive()
        await msg.delete()
        await message.reply_animation(
            photo_url,
            caption=alive_text
        )
    except Exception as e:
        print("Error:", e)
        await msg.edit("An error occurred while checking the status.")

    try:
        await message.delete()
    except:
        pass

@barath.on_message(filters.command("ping", prefixes=HANDLER) & filters.me)
async def ping(_, message):
    start_time = time.time()
    msg =  await message.reply_text("Ping...")
    await msg.edit("✮ᑭｴƝGing...✮")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await msg.edit(f"**I Aᴍ Aʟɪᴠᴇ Mᴀꜱᴛᴇʀ**\n⋙ 🔔 **ᑭｴƝG**: {ping_time}\n⋙ ⬆️ **ⴑⲢⲦⲒⲘⲈ**: {uptime}")
    try:
        await message.delete()
    except:
        return


__mod_name__ = "STATUS"  
    
__help__ = """  
- alive: to check bot on/off
- ping: check response of server
"""  


string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
