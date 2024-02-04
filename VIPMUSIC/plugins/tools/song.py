import os
import future
import asyncio
import requests
import wget
import time
import yt_dlp
from urllib.parse import urlparse
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from instascrape import Post
from instascrape import Profile
from VIPMUSIC import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos

#-------------------


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("song"))
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("**🔄 sᴇᴀʀᴄʜɪɴɢ... **")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results[0]["views"]
        channel_name = results[0]["channel"]

    except Exception as e:
        m.edit("**⚠️ ɴᴏ ʀᴇsᴜʟᴛs ᴡᴇʀᴇ ғᴏᴜɴᴅ. ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ ᴛʏᴘᴇᴅ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ sᴏɴɢ ɴᴀᴍᴇ**")
        print(str(e))
        return
    m.edit("**📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ...**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**📤 ᴜᴘʟᴏᴀᴅɪɴɢ...**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}\nRᴇǫᴜᴇsᴛᴇᴅ ʙʏ ➪{message.from_user.mention}\nVɪᴇᴡs➪ {views}\nCʜᴀɴɴᴇʟ➪ {channel_name}",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error !!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
        

# ------------------------------------------------------------------------------- #

###### INSTAGRAM REELS DOWNLOAD

@app.on_message(filters.command(["ig"], ["/", "!", "."]))
async def download_instareels(c: app, m: Message):
    try:
        reel_url = m.command[1]
    except IndexError:
        await m.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ʟɪɴᴋ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪᴛ...")
        return

    if not reel_url.startswith("https://www.instagram.com/reel/"):
        await m.reply_text("Iɴ ᴏʀᴅᴇʀ ᴛᴏ ᴏʙᴛᴀɪɴ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ʀᴇᴇʟ, ᴀ ᴠᴀʟɪᴅ ʟɪɴᴋ ɪs ɴᴇᴄᴇssᴀʀʏ. Kɪɴᴅʟʏ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ᴡɪᴛʜ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ʟɪɴᴋ.")
        return

    try:
        post = Post(url=reel_url)
        post.load()
        media_url = post.url
        media_type = post.type
        if media_type == "GraphVideo":
            await m.reply_video(media_url)
        elif media_type == "GraphImage":
            await m.reply_photo(media_url)
        elif media_type == "GraphSidecar":
            # Handle multiple media (carousel)
            # You can customize this part based on your needs
            media_urls = [item.url for item in post['edge_sidecar_to_children']['edges']]
            await m.reply_media_group([{"type": "photo", "media": url} for url in media_urls])
        else:
            await m.reply_text("Unsupported media type.")
    except Exception as e:
        await m.reply_text(f"Error: {str(e)}")


######

@app.on_message(filters.command(["reel"], ["/", "!", "."]))
async def instagram_reel(client, message):
    if len(message.command) == 2:
        url = message.command[1]
        # Assuming you want to use the 'instascrape' library here for profile scraping
        profile = Profile(url)
        profile.load()
        reels = profile.get_posts(filters=lambda post: post.is_reel)

        if reels:
            video_url = reels[0].url
            await message.reply_video(f"{video_url}")
        else:
            await message.reply("No reels found on the profile.")
    else:
        await message.reply("Please provide a valid Instagram URL using the /reels command.")
