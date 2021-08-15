from telethon import TelegramClient
import requests
import os
from colorama import Fore, Back, Style
import nekos
import config

client1 = TelegramClient(config.number, config.api_id, config.api_hash) 




client1.start()

chat = input(Fore.RED + "Введите чат/пользователя")
print("NOTE: можете указать url картинки для спама картинками :)")
message = input("Введите сообщение каким проспамить")
print(Back.GREEN + "Cпам начался! Спамим!")

async def main():
	while True:
		await client1.send_message(chat, message)
		await client1.send_file(chat, 'https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg')

if __name__ == '__main__':
  client1.loop.run_until_complete(main())
  client1.loop.close()