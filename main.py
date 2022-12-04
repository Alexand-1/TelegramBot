import telebot
from telebot import types, TeleBot

bot: TeleBot = telebot.TeleBot("5239789352:AAFly-1frquRLPFOHl93uq_tci_rrFLavR8")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, <b>{message.from_user.first_name}</b>, напиши /help"
    bot.send_message(message.chat.id, mess, parse_mode="html")
@bot.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.youtube.com/watch?v=gke69PitnHk"))
    bot.send_message(message.chat.id,"Перейдите на сайт", reply_markup=markup)

@bot.message_handler(commands=["help"])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton("/website")
    start = types.KeyboardButton("/start")
    markup.add(website,start)
    bot.send_message(message.chat.id,"ладно", reply_markup=markup)

bot.polling(non_stop=True)
