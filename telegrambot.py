#!/usr/bin/env python
# coding: utf-8


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

