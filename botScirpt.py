import telebot
import random
from telebot import types


bot=telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAEEd59iWBVF8_derZexT5aQoHTXTqFc9AAC_BQAAn4V8UujCb9JigoNciME')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1=types.KeyboardButton('🎲Рандомное число')
    item2=types.KeyboardButton('🤡Послать бота')
    item3=types.KeyboardButton('📚Помощь')
    markup.add(item1,item2,item3)

    name=f"Ну привет <b>{message.from_user.first_name}</b>, чем я могу тебе помочь? "
    bot.send_message(message.chat.id,name, parse_mode='html', reply_markup=markup ,)  #reply_markup=markup2)

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.chat.type=='private':
        if message.text=='🎲Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 9999)))
        elif message.text=='🤡Послать бота':
            ###idem2=types.InlineKeyboardButton('Ладно', callback_data='no')

            bot.send_message(message.chat.id, 'Сам иди нахуй')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEeERiWDY8NiPF77w_T2VPp7sEAnbB6gAC9gADPIpXGnliQ5BtmPh1IwQ')
        elif message.text=='📚Помощь':
            bot.send_message(message.chat.id, 'Брат я хз чем тебе помочь лучше чекни эту гифку внизу👇🏻')
            bot.send_animation(message.chat.id, 'https://media.giphy.com/media/GeimqsH0TLDt4tScGw/giphy.gif')
        elif message.text=='/help':
            bot.send_message(message.chat.id, '<b>📊Тут ты найдешь все ответы на свои вопросы</b> \n \n Перезапуск бота - /start \n Помощь /help \n \n Source - <a href="https://youtu.be/dQw4w9WgXcQ">Скачать!</a>', parse_mode='html')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEeBRiWCr7HT195nKakOWx-8WoME_7rgACyxMAAgEk8UuOOshZI-DWpyME')
        else:
            bot.send_message(message.chat.id, 'брат я не знаю чё тебе ответить')
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEd7RiWBv0x9ASN8_7TQtA2WbDfcwgzAAC5wADOPCiGl8KzGGrjFEmIwQ')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Ну и зачем ты эту фотку скинул?')

#@bot.callback_query_handler(func=lambda call:True)
#def callback_inline(call):
    try:
        if call.message:
            if call.data=='ok':
                bot.send_message(message.chat.id, 'ладно')
            elif call.data=='no':
                bot.send_message(message.chat.id,'Ладно извини брат')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Еще раз')
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text='хуйня', reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)  