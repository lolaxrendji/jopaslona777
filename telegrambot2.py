from telebot import types
from telebot.types import  ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import telebot
from time import sleep 
import random 

bankai = '5920567505:AAH6bp7mqaEGPJzch4wAmqF6FFB8yBnMWsw'
bot = telebot.TeleBot(bankai)

#текстик
@bot.message_handler(commands=['start'])
def button(message):

#кнопки
    markup =  types.InlineKeyboardMarkup(row_width=2)
    ban =  types.InlineKeyboardButton('Хочешь узнать ответы на важнейшие вопросы человечества?', callback_data='question_1')
    ban2 =  types.InlineKeyboardButton('да иди ты нахуй со своими ответами', callback_data='сам')
    markup.add(ban, ban2)
 
    bot.send_message(message.chat.id, 'че каво сучара', reply_markup=markup)
   

#ответы
@bot.callback_query_handler(func=lambda call:True)
def corn(call):

    if call.message:

     if call.data == "question_1":

        markup =  types.InlineKeyboardMarkup(row_width=2)
        ban =  types.InlineKeyboardButton('Сколько весит мама Вани?', callback_data='question_2')
        ban2 = types.InlineKeyboardButton('Сколько раз ебали маму Вани?', callback_data='сам2')
        ban3 = types.InlineKeyboardButton("Сколько раз мама Вани лично сосала у Тимофей?", callback_data='сам3')
        markup.add(ban, ban2, ban3)
        bot.send_message(call.message.chat.id, 'меню',reply_markup= markup )

     elif call.data =='сам':
      markup =  types.InlineKeyboardMarkup(row_width=2)
      back =  types.InlineKeyboardButton('назад', callback_data='question_1')
      markup.add(back)

      bot.send_message(call.message.chat.id, 'сам иди противная пиздопроебина', reply_markup=markup)

     elif call.data == 'question_2':
      markup =  types.InlineKeyboardMarkup(row_width=2)
      back =  types.InlineKeyboardButton('назад', callback_data='question_1')
      markup.add(back)
      bot.send_message(call.message.chat.id, 'Сверх много', reply_markup=markup)

     elif call.data =='сам2':
      bot.send_message(call.message.chat.id, 'Такого числа еще даже не придумали', callback_data='сам3', reply_markup=markup)

     elif call.data =='сам3':
      bot.send_message(call.message.chat.id, '1000-7 раз', reply_markup=markup)

     elif call.data == 'question_2':
      bot.send_message(call.message.chat.id, 'Назад', reply_markup=markup )

     elif call.data == 'сам2':
      bot.send_message(call.message.chat.id, 'Назад',  reply_markup=markup)

     elif call.data == 'сам3':
      bot.send_message(call.message.chat.id, 'Назад', reply_markup=markup )











bot.polling()