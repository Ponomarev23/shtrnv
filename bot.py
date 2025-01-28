import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Укажите здесь ваш API токен и ссылку на веб-приложение
API_TOKEN = '7797487743:AAH5BUOV-SY0Wuws5-LrArfXt5GjtXQppuI'
WEB_APP_URL = 'https://t.me/swrec_bot/distribution'  # Замените на URL вашего веб-приложения

# Инициализация бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем клавиатуру с одной кнопкой
    markup = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton("Открыть", url=WEB_APP_URL)
    markup.add(web_app_button)

    # Отправляем сообщение с кнопкой
    bot.send_message(
        message.chat.id,
        "Привет! Это чат-бот Sovietwave Records. Нажми кнопку ниже, чтобы отправить свой сингл на дистрибуцию",
        reply_markup=markup
    )

# Обработчик команды /openapp для открытия веб-приложения
@bot.message_handler(commands=['openapp'])
def open_web_app(message):
    # Создаем клавиатуру с одной кнопкой для перехода в веб-приложение
    markup = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton("Перейти к веб-приложению", url=WEB_APP_URL)
    markup.add(web_app_button)

    # Используйте прямую ссылку на изображение
    image_url = "https://imgur.com/zhm5j9p"  # Замените на ваше изображение
    bot.send_photo(
        message.chat.id,
        image_url,
        caption="Привет! Это чат-бот Sovietwave Records. Нажми кнопку ниже, чтобы отправить свой сингл на дистрибуцию.",
        reply_markup=markup
    )

# Запуск бота
bot.polling()
