#https://www.youtube.com/watch?v=fp5-XQFr_nk - starting from 50 minutes
import telebot
bot = telebot.TeleBot("5326083198:AAH8arLtMCDrlpzChHUTFifdGIfaQ_UInE")#Token is changed

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)