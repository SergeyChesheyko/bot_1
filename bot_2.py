import telebot
from telebot import types # импортируем для создания кнопок
bot = telebot.TeleBot('5460516821:AAES5K6yUAryjCzeecWIl0GvrAWQ7FJqQg4')

@bot.message_handler(commands=['start'])

def start(message):
    mess = f'<b>Доброго времени суток, {message.from_user.first_name}! Вас приветствует официальный бот водоема Рыбалка Ковалевичи!' \
           f' Здесь вы можете узнать подробную информацию про отдых у нас на водоеме! </b>'
    photo = open('besed.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    map = types.KeyboardButton('Карта')
    start = types.KeyboardButton('/Погода')
    cena = types.KeyboardButton('Цены')
    location = types.KeyboardButton('Координаты')
    vk = types.KeyboardButton('/VK')
    inst = types.KeyboardButton('/Instagram')
    markup.add(map, start, location, cena, vk, inst)
    bot.send_message(message.chat.id, '/menu', reply_markup=markup)



@bot.message_handler(commands=['map'])
def map(message):
    photo = open('karta.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['location'])
def location(message):
    bot.send_location(message.chat.id, 53.471145, 27.700752)

@bot.message_handler(content_types=[ "photo"])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'ВАУ, крутое фото!')

@bot.message_handler(commands=['VK'])
def VK(message):
    markup = types.InlineKeyboardMarkup() #создаем кнопки с помощью библиотеки types
    # этот метод позволяет встраивать в сообщения кнопи, картинки и тд
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://vk.com/carpfisher_by'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup) #при отправке сообщения нужно прикреплять кнопки

@bot.message_handler(commands=['Instagram'])
def Instagram(message):
    markup = types.InlineKeyboardMarkup() #создаем кнопки с помощью библиотеки types
    # этот метод позволяет встраивать в сообщения кнопи, картинки и тд
    markup.add(types.InlineKeyboardButton('Посетить веб сайт', url='https://instagram.com/carpfisher.by'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup) #при отправке сообщения нужно прикреплять кнопки

@bot.message_handler(commands=['Погода'])
def Погода(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('10 дней', url='https://www.gismeteo.by/weather-kovalevichi-121347/10-days/'))
    markup.add(types.InlineKeyboardButton('3 дня', url='https://www.gismeteo.by/weather-kovalevichi-121347/3-days/'))
    markup.add(types.InlineKeyboardButton('Сегодня', url='https://www.gismeteo.by/weather-kovalevichi-121347/'))
    markup.add(types.InlineKeyboardButton('Сейчас', url='https://www.gismeteo.by/weather-kovalevichi-121347/now/'))
    bot.send_message(message.chat.id, 'Посмотреть погоду в Ковалевичах', reply_markup=markup) #при отправке сообщения нужно прикреплять кнопки

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    map = types.KeyboardButton('Карта')
    start = types.KeyboardButton('/Погода')
    cena = types.KeyboardButton('Цены')
    location = types.KeyboardButton('Координаты')
    vk = types.KeyboardButton('/VK')
    inst = types.KeyboardButton('/Instagram')
    markup.add(map, start, location, cena, vk, inst)
    bot.send_message(message.chat.id, 'Сделайте выбор:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "id":
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text == "Карта":
        photo = open('karta.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Цены":
        photo = open('цены.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Координаты":
        bot.send_location(message.chat.id, 53.471145, 27.700752)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')
bot.polling(none_stop=True)