#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import requests
from pyrogram import Client, filters
from config import OWNER_ID
from config import HANDLER 

api_url = "https://pinteresimage.nepcoderdevs.workers.dev/"

def get_images(prompt, l):
    response = requests.get(f"{api_url}?query={prompt}&limit={l}")
    data = response.json()
    return [result["imageUrl"] for result in data["results"]]


@barath.on_message(filters.command(["pinterest"], ".") & (filters.me)
def send_images(client, message):
    command = message.text.split(maxsplit=2)
    if len(command) < 3:
        message.reply_text("Invalid command format. Please use .pinterest <amt> <prompt>")
        return
    limit = command[1]
    prompt  = ''.join(command[2:])
    images = get_images(prompt, limit)
    chat_id = message.chat.id

    for image in images:
        client.send_photo(chat_id, photo=image)
