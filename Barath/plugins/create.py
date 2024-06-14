#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

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

from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(
    filters.command(["create"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gcch(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.edit(f".ᴄʀᴇᴀᴛᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    bunny = await message.edit("ᴘʀᴏᴄᴇꜱꜱɪɴɢ....")
    fuk = """ʙʏ - @STORM_CHATZ

- ɢɪᴠᴇ ʀᴇꜱᴘᴇᴄᴛ ᴛᴀᴋᴇ ʀᴇꜱᴘᴇᴄᴛ

- ᴅᴏɴ'ᴛ ᴀʙᴜꜱᴇ ᴀɴʏᴏɴᴇ

- ᴅᴏɴ'ᴛ ᴜꜱᴇ 18+ ᴄᴏɴᴛᴇɴᴛꜱ

- ᴜʀɢᴇɴᴛ ᴄᴀʟʟ ᴏɴʟʏ

- ɴᴏ ꜱᴇʟʟɪɴɢ ᴏʀ ʙᴜʏɪɴɢ

- ᴅᴏɴ'ᴛ ᴜꜱᴇ ꜱʟᴀɴɢ ʟᴀɴɢᴜᴀɢᴇ ᴡʜɪʟᴇ ᴛᴀʟᴋɪɴɢ ɪɴ ɢʀᴏᴜᴘ"""
    if group_type == "group": 
        _id = await client.create_supergroup(group_name, fuk)
        await bunny.edit(
            f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ....",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":  
        _id = await client.create_channel(group_name, fuk)
        await bunny.edit(
            f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʀᴇᴀᴛᴇᴅ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ....",
            disable_web_page_preview=True,
        )
