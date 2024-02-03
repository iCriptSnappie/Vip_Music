import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            username = message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
            msg = (
                f"**📝Mᴜsɪᴄ Bᴏᴛ Aᴅᴅᴇᴅ Iɴ A #Nᴇᴡ_Gʀᴏᴜᴘ**\n\n"
                f"**📌Cʜᴀᴛ Nᴀᴍᴇ:** {message.chat.title}\n"
                f"**🍂Cʜᴀᴛ Iᴅ:** {message.chat.id}\n"
                f"**🔐Cʜᴀᴛ Usᴇʀɴᴀᴍᴇ:** @{username}\n"
                f"**📈Gʀᴏᴜᴘ Mᴇᴍʙᴇʀs:** {count}\n"
                f"**🤔Aᴅᴅᴇᴅ Bʏ:** {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"😍Aᴅᴅᴇᴅ Bʏ😍", url=f"tg://openmessage?user_id={message.from_user.id}")]
         ]))


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#Lᴇғᴛ_Gʀᴏᴜᴘ</u></b> ✫\n\nCʜᴀᴛ Tɪᴛʟᴇ : {title}\n\nCʜᴀᴛ Iᴅ : {chat_id}\n\nRᴇᴍᴏᴠᴇᴅ Bʏ : {remove_by}\n\nBᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
