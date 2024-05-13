import telebot
import sqlite3

<<<<<<< HEAD
bot = telebot.TeleBot('Token')
name = None

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('tatusha.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, давай тебя зарегистрируем! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)
=======
bot = telebot.TeleBot('Token')
>>>>>>> 72aa26052862010eba3d0aa0014e7baed3c9d7b5


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('tatusha.db')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (name, password))
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('tatusha.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')  # Исправлено "SELEST" на "SELECT"
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, Пароль: {el[2]}\n'  # Исправлено "/n" на "\n"
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)  # Исправлено "message" на "call.message"

bot.infinity_polling()
