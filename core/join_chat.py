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



client1 = TelegramClient(config.number, config.api_id, config.api_hash)
chat = input("Введите чат (в формате nX1901678jqB6w0MDU1 )> ")
client1.start()
async def main():
    updates = await client1(ImportChatInviteRequest(chat))
    print(Fore.LIGHTMAGENTA_EX + "[+] Бот присоиденлся к чату")
if __name__ == '__main__':
  client1.loop.run_until_complete(main())
  client1.loop.close()
