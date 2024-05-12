import telebot

bot = telebot.TeleBot('Token')


@bot.message_handler(commands=['site', 'website'])
def open_website(message):
    bot.send_message(message.chat.id, 'Открываю сайт...')
    bot.send_chat_action(message.chat.id, 'typing')  # Показываем "набор сообщения"
    bot.send_message(message.chat.id, 'https://mkgt.ru')


@bot.message_handler(commands=['start', 'main', 'hello'])
def greet_user(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '<b>Справочная информация!</b>', parse_mode='html')


@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    else:
        bot.send_message(message.chat.id, "Простите, я не понимаю вас. Если вам нужна помощь, наберите /help.")


bot.infinity_polling()
