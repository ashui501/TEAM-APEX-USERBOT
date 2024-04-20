import sys
import io, time
import re
import os
import subprocess
import traceback
from pyrogram import filters, enums
from pyrogram.types import Message 
from pyrogram.errors import MessageTooLong



@app.on_message(filters.command("e",prefixes=config.PREFIXES & filters.user(your id here)))
async def evaluate(app , message):
    global r, bot, m
    status_message = await message.reply_text("`Running ...`")
    try:
        cmd = message.text.split(maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    start_time = time.time()

    r = message.reply_to_message 
    m = message

    if r:
        reply_to_id = r.id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, app, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    taken_time = round((time.time() - start_time), 3)
    output = evaluation.strip()
 
    final_output = lang['eval_01'].format(cmd, taken_time, output)
 
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            thumb=THUMB_ID,
            caption=cmd,
            quote=True,
            
        )
        os.remove(filename)
        await status_message.delete()
        return
    else:
        await status_message.edit(final_output, parse_mode=enums.ParseMode.HTML)
        return
