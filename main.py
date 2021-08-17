import os
from colorama import Fore, Back, Style

print("Телеграм спаммер")



conf = os.path.exists('core/config.py')
if conf is False:
	api_id = input('Введите api id: ')
	api_hash = input("Введите api hash: ")
	number = input("Введите номер телефона: ")
	f = open('core/config.py', "w")
	f.write(f"api_id = '{api_id}'\napi_hash = '{api_hash}'\nnumber = '{number}'")
	f.close()


print(Fore.LIGHTCYAN_EX + """
    ____                      __     ____        _     __              
   / __ \___  ________  _____/ /_   / __ \____ _(_)___/ /__  __________
  / / / / _ \/ ___/ _ \/ ___/ __/  / /_/ / __ `/ / __  / _ \/ ___/ ___/
 / /_/ /  __(__  )  __/ /  / /_   / _, _/ /_/ / / /_/ /  __/ /  (__  ) 
/_____/\___/____/\___/_/   \__/  /_/ |_|\__,_/_/\__,_/\___/_/  /____/  
                                                                                                                                            
""")

print("""
88. Присоидениться к приватному чату
99. Присоидениться к публичному каналу

1. Спам заданным сообщениями/картинками
2. Спам хентаем (медленно но разными гифками)
3. Спам хентаем (быстро но одной гифкой)
""")

while True:
	user_input = int(input(">>> "))

	if user_input == 2:
		os.system("python3 core/slow_hentai_spammer.py")
	elif user_input == 1:
		os.system("python3 core/sms_spammer.py")
	elif user_input == 3:
		os.system("python3 core/fast_hentai.py")
	elif user_input == 88:
		os.system("python3 core/join_chat.py")
	elif user_input == 99:
		os.system("python3 core/join_chat1.py")
	else:
		print("Ошибка")
