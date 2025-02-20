import telebot
import openai
from config import *

chatStr = ''

def chatModel(prompt):
    global chatStr
    openai.api_key = CHAT_API
    chatStr += f"Ashu: {prompt}\nLisa: "
    response = openai.completions.create(
        model="davinci-002",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    chatStr += f"{response['choice'][0]['text']}\n"
    return response['choice'][0]['text']


bot = telebot.TeleBot(BOT_API)
@bot.message_handler(['start'])
def start(message):
    print(message)
    bot.reply_to(message, "Welcome this is Lisa!")


@bot.message_handler()
def chat(message):
    try:
        reply = chatModel(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        print(e)
        bot.reply_to(message, e)


print("Bot Started...")
bot.polling()
