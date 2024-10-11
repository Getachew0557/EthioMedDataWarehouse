from telethon import TelegramClient
import os
import logging

# Set up logging
log_dir = '../logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'info.log'), mode='a'),
        logging.FileHandler(os.path.join(log_dir, 'error.log'), mode='a'),
        logging.StreamHandler()  # To also print logs to console
    ]
)

# Your API ID and API Hash (from my.telegram.org)
api_id = ''
api_hash = ''

# Define the client
client = TelegramClient('session_name', api_id, api_hash)

# Connect to Telegram
client.start()
logging.info("Connected to Telegram successfully.")

channel = '@CheMed123'
image_save_path = '../images/'
os.makedirs(image_save_path, exist_ok=True)

async def scrape_channel():
    logging.info(f"Starting to scrape images from {channel}...")
    async for message in client.iter_messages(channel):
        if message.photo:
            try:
                file_path = await message.download_media(file=image_save_path)
                logging.info(f"Image saved to {file_path}")
            except Exception as e:
                logging.error(f"Error downloading image: {e}")

with client:
    client.loop.run_until_complete(scrape_channel())
    logging.info("Scraping process completed.")
