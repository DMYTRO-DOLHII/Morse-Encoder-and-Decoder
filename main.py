# #######################################################################################
#     ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗        ██████╗  ██████╗ ████████╗    #
#     ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝        ██╔══██╗██╔═══██╗╚══██╔══╝    #
#     ██╔████╔██║██║   ██║██████╔╝███████╗█████╗          ██████╔╝██║   ██║   ██║       #
#     ██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝          ██╔══██╗██║   ██║   ██║       #
#     ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗███████╗██████╔╝╚██████╔╝   ██║       #
#     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═════╝  ╚═════╝    ╚═╝       #
# #######################################################################################

from telebot import TeleBot
from telebot import types

import morse
from morse import *

TOKEN = "5868626838:AAHYrddsF8mkph3pCzc0FlPourojxT3-1uo"
bot = TeleBot(TOKEN)
DMYTRO_ID = 427780118


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, "Howdy, how are you doing?")


@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('to_decode.wav', 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, "I have decode your voice as : " + to_latin(decode_morse("to_decode.wav")))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.delete_message(message.chat.id, message.id)


@bot.message_handler(content_types=['voice'])
def handle(message):
    print(message)


@bot.inline_handler(lambda query: query.query != "")
def query_text(inline_query):
    morse_sound(to_morse(inline_query.query))
    voice = open("morse_voice/in_morse.wav", "rb")
    res = bot.send_voice(DMYTRO_ID, voice)
    # r = types.InlineQueryResultVoice(id=1, voice_url="morse_voice/morse_code.wav", title="MORSE")
    r = types.InlineQueryResultCachedVoice(id=1, voice_file_id=res.voice.file_id, title="MORSE")
    bot.answer_inline_query(inline_query.id, [r])


bot.polling()
