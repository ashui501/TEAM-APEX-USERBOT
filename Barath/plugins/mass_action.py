from pyrogram import filters
from pyrogram import enums
from pyrogram.types import *
from Barath import barath as bot
from config import HANDLER,OWNER_ID

async def is_owner(chat_id: int, user_id: int):
    async for x in bot.get_chat_members(chat_id):
        if x.status == enums.ChatMemberStatus.OWNER:
             if x.user.id == user_id:
                 return True
             else: return False



@bot.on_message(filters.command(["unbanall","massunban"], prefixes=HANDLER))
async def unbanall(_, message):
     user_id = message.from_user.id
     chat_id = message.chat.id
     if user_id not in OWNER_ID and (await is_owner(chat_id,user_id)) == False:
          return await message.reply("`You Can't Access This!`")
     elif message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply("`This Command Only work in Groups!`")
     else:
       try:
          BANNED = []
          unban = 0
          async for m in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
                 BANNED.append(m.user.id)
                 await bot.unban_chat_member(chat_id,m.user.id)
                 unban +=1
          await message.reply("**Found Banned Members**: `{}`\n**Unbanned Successfully**: `{}`".format(len(BANNED), unban))
       except Exception as e:
           print(e)
          

@bot.on_message(filters.command(["sbanall","banall","massban"], prefixes=HANDLER))
async def banall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id not in OWNER_ID and (await is_owner(chat_id,user_id)) == False:
         return await message.reply("`You Can't Access This!`")
    elif message.chat.type == enums.ChatType.PRIVATE:
         return await message.reply("`This Command Only work in Groups!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in bot.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await bot.ban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await bot.ban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Banned**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)
     

@bot.on_message(filters.command(["skickall","kickall","masskick"], prefixes=HANDLER))
async def kickall(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if user_id not in OWNER_ID and (await is_owner(chat_id,user_id)) == False:
          return await message.reply("`You Can't Access This!`")
    elif message.chat.type == enums.ChatType.PRIVATE:
          return await message.reply("`This Command Only work in Groups!`")
    else:  
       try: 
          Members = []
          Admins = []
          async for x in bot.get_chat_members(chat_id):
              if not x.privileges:
                    Members.append(x.user.id)
              else:
                    Admins.append(x.user.id)
          for user_id in Members:
               if message.text.split()[0].lower().startswith("s"):
                        m = await bot.ban_chat_member(chat_id, user_id)
                        await bot.unban_chat_member(chat_id, user_id)
                        await m.delete()
               else:
                   await bot.ban_chat_member(chat_id, user_id)
                   await bot.unban_chat_member(chat_id, user_id)
          await message.reply_text("**Successfully Kicked**: `{}`\n**Remaining Admins**: `{}`".format(len(Members),len(Admins),))
       except Exception as e:
        print(e)


@bot.on_message(filters.command(["unbanchannel"], prefixes=HANDLER))
async def unbanchannel(_, message):
    user_id = message.from_user.id
    chat_id = -1001809308823
    if user_id not in OWNER_ID and (await is_owner(chat_id, user_id)) == False:
        return await message.reply("`You Can't Access This!`")
    elif message.chat.type not in [enums.ChatType.CHANNEL, enums.ChatType.SUPERGROUP]:
        return await message.reply("`This Command Only works in Channels or Supergroups!`")
    
    await message.reply("kela unbanning to all wait for 1 hour")

    try:
        BANNED = []
        unban = 0
        async for m in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
            BANNED.append(m.user.id)
            await bot.unban_chat_member(chat_id, m.user.id)
            unban += 1
        await message.reply("**Found Banned Channel Members**: `{}`\n**Unbanned Successfully**: `{}`".format(len(BANNED), unban))
    except Exception as e:
        print(e)

