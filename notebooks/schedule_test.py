# Notebook parsing_with_Simych.ipynb
# C:\ProgramData\anaconda3\python.exe C:/Users/User/my_learning/parsing_cases/notebooks/schedule_test.py
import telebot
from datetime import datetime
import config

print("123 - Hello Nick!")
print("321 - Notebook testing SCHEDULE")

bot = telebot.TeleBot(config.token)

# Отправляем сообщение в указанный chat_id и завершаем работу
chat_id = "1938719365"  # Узнать его можно через @userinfobot
message_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Бот запущен. Никаких действий не требуется!\nРаботает планировщик заданий WINDOWS! Время: {message_time}")

bot.send_message(chat_id, f"""123 - Hello Nick!\n321 - Notebook testing PARSING_CASES/.../SCHEDULE_TEST.PY\n
Бот запущен. Никаких действий не требуется!\nРаботает планировщик заданий WINDOWS!\n
Сообщение отправлено! Скрипт завершается.\nВремя: {message_time}\n\nВыключаюсь...""")
bot.stop_polling()  # Останавливаем бота
print("Выключаюсь...")