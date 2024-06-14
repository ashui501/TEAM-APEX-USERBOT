import requests
from pyrogram import filters, Client
from pyrogram.types import Message
from Barath.__main__ import barath as app
from config import OWNER_ID
from Barath import HANDLER


def fetch_data(query: str, message: str) -> tuple:
    try:
        response = requests.get(f"https://stark.animecloud.tech/chat?brain_id={message.from_user.id}&prompt={query}&bot_name=Sophia&user_name={message.from_user.first_name}&gender=FEMALE")
        response.raise_for_status()
        data = response.json()
        return data.get("message", "No response from the API."), None
    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

@app.on_message(filters.command(["chat", "gpt"], prefixes=HANDLER) & filters.user(OWNER_ID))
async def chatgpt4(_: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Master, Please provide a query.")

    query = " ".join(message.command[1:])
    txt = await message.reply_text("`Processing...`")
    api_response, error_message = fetch_data(query, message)
    await txt.edit(api_response or error_message)
