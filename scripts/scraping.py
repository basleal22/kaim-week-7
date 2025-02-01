import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from telethon import TelegramClient
import csv
async def scraper(client, channel_username, writer):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title  # Extract the channel's title

    # Specifies to fetch up to 600 messages
    async for message in client.iter_messages(entity, limit=60000):
        # Write the channel title along with other data (excluding media handling)
        writer.writerow([channel_title, channel_username, message.id, message.message, message.date])

async def main(client):
    await client.start()
    

    # Open the CSV file and prepare the writer
    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # Include channel title in the header
        
        # List of channels to scrape
        channels = [
    'https://t.me/DoctorsET',
    'https://t.me/lobelia4cosmetics',
    'https://t.me/yetenaweg',
    'https://t.me/EAHCI'
    ]        
        # Iterate over channels and scrape data into the single CSV file
        for channel in channels:
            await scraper(client, channel, writer)
            print(f"Scraped data from {channel}")
    