from Barath import *
from pyrogram import *
import base64
import requests
from Barath import barath
from config import HANDLER


@barath.on_message(filters.command("imgur", prefixes=HANDLER) & filters.me)
async def imgur(_, message):
    msg = await message.reply_text("`Starting upload...`")
    if message.reply_to_message and message.reply_to_message.photo:
        photo_path = await message.reply_to_message.download()
        with open(photo_path, "rb") as file:
            data = file.read()
            base64_data = base64.b64encode(data)
        url = "https://api.imgur.com/3/image"
        headers = {"Authorization": "Client-ID a10ad04550b0648"}
        response = requests.post(url, headers=headers, data={"image": base64_data})
        result = response.json()
        await msg.edit_text(f"""f"**Your link has been generated**: {result["data"]["link"]}""", disable_web_page_preview=True)
    elif message.reply_to_message and message.reply_to_message.animation:
        animation_path = await message.reply_to_message.download()
        with open(animation_path, "rb") as file:
            data = file.read()
            base64_data = base64.b64encode(data)
        url = "https://api.imgur.com/3/image"
        headers = {"Authorization": "Client-ID a10ad04550b0648"}
        response = requests.post(url, headers=headers, data={"image": base64_data})
        result = response.json()
        await msg.edit_text(f"""f"**Your link has been generated**: {result["data"]["link"]}""", disable_web_page_preview=True)
    else:
        await msg.edit_text("Please reply to a photo or animation (GIF) to upload to Imgur.")

# Thanks for https://t.me/NandhaBots by providing this code!
