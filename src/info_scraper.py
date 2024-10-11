import pandas as pd
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel
import asyncio
import logging
import os

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

# Telegram API credentials
API_ID = ''
API_HASH = ''
PHONE_NUMBER = ''

client = TelegramClient('session_name', API_ID, API_HASH)

async def connect_telegram():
    logging.info("Connecting to Telegram...")
    try:
        await client.start(PHONE_NUMBER)
        if not await client.is_user_authorized():
            try:
                await client.send_code_request(PHONE_NUMBER)
                await client.sign_in(PHONE_NUMBER, input('Enter the code: '))
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Enter your 2FA password: '))
        logging.info("Successfully connected to Telegram.")
    except Exception as e:
        logging.error(f"Error while connecting to Telegram: {e}")

async def scrape_channel_messages(channel_username, limit=10000):
    logging.info(f"Scraping messages from {channel_username}...")
    try:
        channel = await client.get_entity(PeerChannel(int(channel_username)) if channel_username.isdigit() else channel_username)
    except Exception as e:
        logging.error(f"Could not access channel {channel_username}: {e}")
        return pd.DataFrame()

    messages = []
    async for message in client.iter_messages(channel, limit=limit):
        messages.append({
            'message_id': message.id,
            'date': message.date,
            'text': message.message,
            'sender_id': message.sender_id
        })
    
    logging.info(f"Scraped {len(messages)} messages from {channel_username}.")
    return pd.DataFrame(messages)

async def scrape_multiple_channels(channel_list, message_limit=1000):
    logging.info("Starting to scrape multiple channels...")
    all_data = pd.DataFrame()

    for channel in channel_list:
        channel_data = await scrape_channel_messages(channel, limit=message_limit)
        all_data = pd.concat([all_data, channel_data], ignore_index=True)

    return all_data

async def main():
    channel_list = [
        '@DoctorsET',
        '@CheMed123',
        '@lobelia4cosmetics',
        '@yetenaweg',
        '@EAHCI'
    ]

    await connect_telegram()
    scraped_data = await scrape_multiple_channels(channel_list)
    
    output_file = '../data/telegram_medical_businesses_data.csv'
    scraped_data.to_csv(output_file, index=False)
    logging.info(f"Data scraping complete. Data saved to '{output_file}'.")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
