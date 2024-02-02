from ... import *
from pyrogram import *
from pyrogram.types import *


@app.on_message(filters.command(["bin", "ccbin", "bininfo"], [".", "!", "/"]))
async def check_ccbin(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>ᴘʟᴇᴀꜱᴇ ɢɪᴠᴇ ᴍᴇ ᴀ ʙɪɴ ᴛᴏ\nɢᴇᴛ ʙɪɴ ᴅᴇᴛᴀɪʟꜱ !</b>"
        )
    try:
        await message.delete()
    except:
        pass
    aux = await message.reply_text("<b>ᴄʜᴇᴄᴋɪɴɢ...</b>")
    bin = message.text.split(None, 1)[1]
    if len(bin) < 6:
        return await aux.edit("<b>❌ ᴡʀᴏɴɢ ʙɪɴ❗...</b>")
    try:
        resp = await api.bininfo(bin)
        await aux.edit(f"""
<b>💠 ʙɪɴ ꜰᴜʟʟ ᴅᴇᴛᴀɪʟꜱ:</b>

<b>🏦 ʙᴀɴᴋ:</b> <tt>{resp.bank}</tt>
<b>💳 ʙɪɴ:</b> <tt>{resp.bin}</tt>
<b>🏡 ᴄᴏᴜɴᴛʀʏ:</b> <tt>{resp.country}</tt>
<b>🇮🇳 ꜰʟᴀɢ:</b> <tt>{resp.flag}</tt>
<b>🧿 ɪꜱᴏ:</b> <tt>{resp.iso}</tt>
<b>⏳ ʟᴇᴠᴇʟ:</b> <tt>{resp.level}</tt>
<b>🔴 ᴘʀᴇᴘᴀɪᴅ:</b> <tt>{resp.prepaid}</tt>
<b>🆔 ᴛʏᴘᴇ:</b> <tt>{resp.type}</tt>
<b>ℹ️ ᴠᴇɴᴅᴏʀ:</b> <tt>{resp.vendor}</tt>"""
        )
    except:
        return await aux.edit(f"""
🚫 ʙɪɴ ɴᴏᴛ ʀᴇᴄᴏɢɴɪᴢᴇᴅ. ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴀ ᴠᴀʟɪᴅ ʙɪɴ.""")
