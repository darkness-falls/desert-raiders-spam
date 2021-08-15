import requests
import random
import json
from time import sleep
from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, MessageMediaDocument, PeerChannel, MessageMediaPhoto, InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest



chats = []















def get_chats(client):  #  Получение чатов
	results = client(GetDialogsRequest(
             	offset_date=last_date,
             	offset_id=0,
             	offset_peer=InputPeerEmpty(),
             	limit=chunk_size,
             	hash = 0))
	chats.extend(results.chats)
	r = requests.get("https://pastebin.com/raw/BvL5R382")  # Проверка лицензии(вырезано)
	return chats, r.raw