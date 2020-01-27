import telebot
import pyowm

owm = pyowm.OWM('4299135e23529e7000601549bbf0aafc', language = 'ru')
bot = telebot.TeleBot("978059010:AAFqMBA72ZOyFyB7LyiuUS19Q39BhmjE_nI")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature("celsius")["temp"]

	answer = 'В городе ' + message.text + " сейчас " + w.get_detailed_status() + '\n'
	answer += "Температура " + str(temp) + "\n"

	bot.send_message(message.chat.id, answer)


bot.polling( none_stop = True)
