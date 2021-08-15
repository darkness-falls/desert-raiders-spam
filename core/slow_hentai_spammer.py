from telethon import TelegramClient
from colorama import Fore, Back, Style
import nekos
import config

client1 = TelegramClient(config.number, config.api_id, config.api_hash) 


client1.start()

chat = input(Fore.RED + "Введите чат/пользователя")
message = nekos.img('random_hentai_gif')
print(Back.GREEN + "Cпам начался! Спамим хентаем :)")

async def main():
	while True:
		await client1.send_message(chat, message)

if __name__ == '__main__':
  client1.loop.run_until_complete(main())
  client1.loop.close()