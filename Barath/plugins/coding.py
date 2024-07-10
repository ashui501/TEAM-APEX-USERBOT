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


import random
from pyrogram import Client, filters
pyrogram.types import Message
from Barath import barath, MODULE
from config import HANDLER,  OWNER_ID


@barath.on_message(filters.command("cd", prefixes=HANDLER) & filters.me)
async def coding(client, message):
    args = message.text.split(" ")[1:]
    codingdata = [
  "https://graph.org/file/72e66a11ba6d7bd121e80.jpg",
  "https://graph.org/file/02e94b94f118322533c31.jpg",
  "https://graph.org/file/3ae8cb93471d0160ac8c2.jpg",
  "https://graph.org/file/a6966a6f3674b6dd97727.jpg",
  "https://graph.org/file/52bc897252d72a95f4c0a.jpg",
  "https://graph.org/file/ae5439c8b8169b2a7c4e6.jpg",
  "https://graph.org/file/02e94b94f118322533c31.jpg",
  "https://graph.org/file/72e66a11ba6d7bd121e80.jpg",
    ]
    coding_url = random.choice(codingdata)
    await message.reply_photo(coding_url)

add_command_help(
    "•─╼⃝𖠁 Cᴏᴅɪɴɢ",
    [
       ["coding", "Gɪᴠᴇ random Cᴏᴅɪɴɢ pic."],
        ],
)
