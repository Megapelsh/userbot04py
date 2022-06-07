from telethon.sync import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()


print('User-Bot started')
donorGroup = os.getenv('DONOR_GROUP')
targetGroup = os.getenv('TARGET_GROUP')
api_id = bool(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')


client = TelegramClient(donorGroup, api_id, api_hash)


@client.on(events.NewMessage(chats=donorGroup))
async def my_event_handler(event):
    await client.send_message(targetGroup, event.text)
    print(event.text)


client.start()
client.run_until_disconnected()
