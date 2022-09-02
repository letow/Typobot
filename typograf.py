import telebot
import requests
import html

token = open('token.txt', 'r')
bot = telebot.TeleBot(token.read())
token.close()


@bot.channel_post_handler(content_types=['text'])
def typograf(post):
    unedited_text = post.text
    response = requests.post('https://www.typograf.ru/webservice/', data={'text': r'{}'.format(unedited_text),
                                                                          'chr': 'utf-8',
                                                                          'xml':'<?xml version="1.0" encoding="utf-8" ?><preferences><tags delete="2">1</tags></preferences>'})
    edited_text = html.unescape(str(response.content, encoding='utf-8'))
    bot.edit_message_text(edited_text, post.chat.id, post.id, parse_mode='MARKDOWN')

print('Bot is running. Press Ctrl+C to stop it.')
bot.infinity_polling()
