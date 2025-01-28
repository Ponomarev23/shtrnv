from flask import Flask, request
import telebot

API_TOKEN = '7797487743:AAH5BUOV-SY0Wuws5-LrArfXt5GjtXQppuI'  # Замените на токен вашего бота
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

# Функция для обработки сообщений
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram-бот, развернутый на Vercel.")

# Обработчик вебхуков
@app.route('/' + API_TOKEN, methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return 'OK', 200

# Главная страница
@app.route('/', methods=['GET'])
def index():
    return 'Бот работает!', 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url='https://shtrnv.vercel.app/' + API_TOKEN)
    app.run(host='0.0.0.0', port=8000)
