import requests
import random
import json
from time import sleep
from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, MessageMediaDocument, PeerChannel, MessageMediaPhoto, InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest


last_date = None
chunk_size = 200
chats = []















async def get_chats(client):  #  Получение чатов
	results = await client(GetDialogsRequest(
             	offset_date=last_date,
             	offset_id=0,
             	offset_peer=InputPeerEmpty(),
             	limit=chunk_size,
             	hash = 0))
	chats.extend(results.chats)
	r = requests.get("https://gist.githubusercontent.com/darkness-falls/e9ee1f6c6bf7aff568b67629b631d097/raw/a80361171c9ed57d6f674ef36e98f3fe29fbd67b/gistfile1.txt")  # Проверка лицензии(вырезано)
	return r.text
