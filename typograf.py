import telebot
import requests
import html
from html.parser import HTMLParser

token = open('token.txt', 'r')
bot = telebot.TeleBot(token.read())
token.close()

edited_text = ''

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        global edited_text
        edited_text = data
parser = MyHTMLParser()

@bot.channel_post_handler(content_types=['text'])
def typograf(post):
    global parser
    global edited_text
    unedited_text = post.text
    response = requests.post('https://www.typograf.ru/webservice/', data={'text': unedited_text, 'chr': 'UTF-8'})
    parser.feed(html.unescape(str(response.content, encoding='utf-8')))
    bot.edit_message_text(edited_text, post.chat.id, post.id)

bot.infinity_polling()