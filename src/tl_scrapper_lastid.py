import logging
from telethon import TelegramClient
import csv
import os
import json
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    filename='scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables once
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')

# Function to read channels from a JSON file
def load_channels_from_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get('channels', []), data.get('comments', [])
    except Exception as e:
        logging.error(f"Error reading channels from JSON: {e}")
        return [], []

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir, num_messages):
    try:
        entity = await client.get_entity(channel_username)
        channel_title = entity.title
        
        message_count = 0
        async for message in client.iter_messages(entity):
            if message_count >= num_messages:
                break  # Stop after scraping the specified number of messages
            
            media_path = None
            if message.media:
                filename = f"{channel_username}_{message.id}.{message.media.document.mime_type.split('/')[-1]}" if hasattr(message.media, 'document') else f"{channel_username}_{message.id}.jpg"
                media_path = os.path.join(media_dir, filename)
                await client.download_media(message.media, media_path)
                logging.info(f"Downloaded media for message ID {message.id}.")
            
            writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])
            logging.info(f"Processed message ID {message.id} from {channel_username}.")
            
            message_count += 1

        if message_count == 0:
            logging.info(f"No messages found for {channel_username}.")

    except Exception as e:
        logging.error(f"Error while scraping {channel_username}: {e}")

# Initialize the client once with a session file
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    try:
        await client.start(phone)
        logging.info("Client started successfully.")
        
        media_dir = 'photos'
        os.makedirs(media_dir, exist_ok=True)

        # Load channels from JSON file
        channels, comments = load_channels_from_json('channels.json')
        
        num_messages_to_scrape = 20  # Specify the number of messages to scrape

        for channel in channels:
            # Create a CSV file named after the channel
            csv_filename = f"{channel[1:]}_data.csv"  # Remove '@' from channel name
            with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])
                
                await scrape_channel(client, channel, writer, media_dir, num_messages_to_scrape)
                logging.info(f"Scraped data from {channel}.")

        # Log commented channels if needed
        if comments:
            logging.info(f"Commented channels: {', '.join(comments)}")

    except Exception as e:
        logging.error(f"Error in main function: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
