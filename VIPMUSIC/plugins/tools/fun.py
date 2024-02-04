# Import necessary libraries
import os
import random
import asyncio
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
from gtts import gTTS

# Load environment variables
load_dotenv()

# Initialize the Telegram bot
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

bot = Client(
    "VIP-MUSIC",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
)

# List of slap GIFs
slap_gifs = [
    "https://ik.imagekit.io/a7tzxdo7c/TG/TG%20GIF/how-dare-you-whisper-such-a-thing.gif",
    "https://ik.imagekit.io/a7tzxdo7c/TG/TG%20GIF/kevin-hart-slap.gif",
    # Add more slap GIFs here
]

# Define slap command
@bot.on_message(filters.command("slap"))
async def slap_command(_, message: Message):
    # Check if the command is a reply to a user
    if message.reply_to_message and message.reply_to_message.from_user:
        # Get a random slap GIF
        slap_gif = random.choice(slap_gifs)
        # Send the slap GIF to the replied user
        await message.reply_animation(slap_gif)
    else:
        await message.reply_text("Please reply to a user to slap.")

# Run the bot
if __name__ == "__main__":
    bot.run()
