from telethon import TelegramClient, events
import asyncio
# List of channels to scrape
CHANNELS = [
    'https://t.me/DoctorsET',
    'https://t.me/ChemedTelegramChannel',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/yetenaweg',
    'https://t.me/EAHCI'
]
async def scrape_tel(channel_link,client):
    #Scrapes the last 1000 messages from a given Telegram channel
    channel_username = channel_link.split('/')[-1]
    channel = await client.get_entity(channel_username)
    messages = await client.get_messages(channel, limit=10000)
    
    # Process and display messages
    for message in messages:
        if message.text:
            print(f"Message from {channel_username}: {message.text}")
async def main():
    for channel in CHANNELS:
        print(f"Scraping {channel}...")
        await scrape_tel(channel)
async def scrape_multiple_channels(client, channels):
    """Scrapes messages from multiple Telegram channels."""
    for channel in channels:
        print(f"Scraping {channel}...")
        await scrape_tel(client, channel)