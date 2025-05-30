import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER = os.getenv("OWNER")

# pyrogram client
app = Client(
    "banall",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Define your main inline keyboard buttons
main_buttons = [[
    InlineKeyboardButton('✚ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ ✚', url='https://t.me/BAN_ALL_OPBOT?startgroup=true')
], [
    InlineKeyboardButton('❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️', url='https://t.me/UncleChipssBot')
], [
    InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers0'),
    InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ɢʀᴏᴜᴘ', url='https://t.me/SuperToppers')
], [
    InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@SuperToppers')
]]

@app.on_message(
    filters.command("start")
    & filters.private
)
async def start_command(client, message: Message):
    start_text = (
        "┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼──────• \n"
        f"┆✦ » ʜᴇʏ {message.from_user.mention}✨ \n"
        "└──────────────────────• \n"
        "✦ » ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ ʙᴀɴᴀʟʟ ʙᴏᴛ. \n"
        "✦ » ʙᴀɴ ᴏʀ ᴅᴇsᴛʀᴏʏ ᴀʟʟ ᴛʜᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ᴀ ɢʀᴏᴜᴘ ᴡɪᴛʜɪɴ ᴀ ғᴇᴡ sᴇᴄᴏɴᴅs. \n"
        "✦ » ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ, ɢɪᴠᴇ ᴍᴇ ᴏɴʟʏ ʙᴀɴ ᴘᴏᴡᴇʀ ᴀɴᴅ ᴛʏᴘᴇ /banall ᴛᴏ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.\n\n"
        "•──────────────────────• \n"
        "❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ ➪ ˹ Sᴜᴘᴇʀ Tᴏᴘᴘᴇʀs ˼ \n"
        "•──────────────────────•"
    )
    await message.reply_photo(
        photo="https://ibb.co/7P7Z3FP",
        caption=start_text,
        reply_markup=InlineKeyboardMarkup(main_buttons)
    )

@app.on_message(
    filters.command("banall")
    & filters.group
)
async def banall_command(client, message: Message):
    print("getting members from {}".format(message.chat.id))
    async for i in app.get_chat_members(message.chat.id):
        try:
            await app.ban_chat_member(chat_id=message.chat.id, user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
        except Exception as e:
            print("failed to kick {} from {}: {}".format(i.user.id, message.chat.id, e))
    print("process completed")


# start bot client
app.start()
print("Banall-Bot Booted Successfully")
idle()
