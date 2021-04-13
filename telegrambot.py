#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""import telebot
from pymongo import MongoClient

tb = telebot.TeleBot('1620634974:AAHvDRfnpKm6OMViwLf_V07vLb96WCZXJ8g')

client = MongoClient()
db = client.first_db
users = db['users']

@tb.message_handler(commands=['start','go'])
def start_handler(message):
    msg = tb.send_message(message.chat.id, "привет, отравь логин и пароль")
    tb.register_next_step_handler(msg, auth)
    
def auth(message):
    data = message.text.split()
    
    check = users.find_one({
        'username': str(data['username']),
        'password': str(data['password']),
    })
    
    if check is None:
        tb.send_message(message.chat.id, r'Неправильно введен логин иили пароль')
    else:
        msg = tb.send_message(message.chat.id, 'Ну что?')
        tb.register_next_step_handler(msd, next_step_func)
        """


# In[13]:


import telebot

tb = telebot.TeleBot('1620634974:AAHvDRfnpKm6OMViwLf_V07vLb96WCZXJ8g')

@tb.message_handler(commands=['start', 'halp'])
def send_welcom(message):
    tb.reply_to(message, f'Хей крошка картошка, {message.from_user.first_name}')

@tb.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        tb.send_message(message.from_user.id, 'Привет')
    else: tb.send_message(message.from_user.id, 'Я понимаю только слово привет')
tb.polling(none_stop=True)

