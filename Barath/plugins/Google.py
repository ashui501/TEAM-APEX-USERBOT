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

# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

#REMAKE BY AKIRA ISHIKKI AND TRYTOLIVEALONE 





import requests
from bs4 import BeautifulSoup
from googlesearch import search
from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER,OWNER_ID
from Barath.helpers.basic import edit_or_reply


def googlesearch(query):
    co = 1
    returnquery = {}
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        url = str(j)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        metas = soup.find_all("meta")
        site_title = None
        for title in soup.find_all("title"):
            site_title = title.get_text()
        metadeta = [
            meta.attrs["content"]
            for meta in metas
            if "name" in meta.attrs and meta.attrs["name"] == "description"
        ]
        returnquery[co] = {"title": site_title, "metadata": metadeta, "url": j}
        co = co + 1
    return returnquery


@Client.on_message(
    filters.command(["ggl"], ".") & (filters.me)
)
async def gs(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    msg_txt = message.text
    returnmsg = ""
    query = None
    if " " in msg_txt:
        query = msg_txt[msg_txt.index(" ") + 1 : len(msg_txt)]
    else:
        await Man.edit("Give a query to search")
        return
    results = googlesearch(query)
    for i in range(1, 10, 1):
        presentquery = results[i]
        presenttitle = presentquery["title"]
        presentmeta = presentquery["metadata"]
        presenturl = presentquery["url"]
        print(presentquery)
        print(presenttitle)
        print(presentmeta)
        print(presenturl)
        if not presentmeta:
            presentmeta = ""
        else:
            presentmeta = presentmeta[0]
        returnmsg = (
            returnmsg
            + f"[{str(presenttitle)}]({str(presenturl)})\n{str(presentmeta)}\n\n"
        )
    await Man.edit(returnmsg)
