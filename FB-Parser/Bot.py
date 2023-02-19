from socket import timeout
import telebot
import time

import Core
from Config import token
from Config import keycode

l_users = ['817515456']

bot = telebot.TeleBot(token, parse_mode=None)

#Регистрация в боте
@bot.message_handler(content_types=['text'])
def register_message(message):
    if message.text == keycode:
        if message.chat.id not in l_users:
            l_users.append(message.chat.id)
            bot.send_message(message.chat.id, 'Registered!')
        elif message.chat.id in l_users:
            bot.send_message(message.chat.id, 'Already registered!')
        else:
            bot.send_message(message.chat.id, 'Something went wrong!')

#Рассылка пользователям
def mailing(msg):
    fin_msg = ''
    for i in msg:
        print(msg)
        '''
        team = i['team']
        fpr = i['fpr']
        goals = i['goals']
        min_ = i['min']
        score = i['score']
        fin_msg += team + fpr + goals + min_ + score + 'n'
        '''
    for user in l_users:
        bot.send_message(user, msg)
        
def gogo(fin_msg):
    with bot:
        bot.polling()
        mailing(fin_msg)
        bot.stop_polling()

'''
#Перезапуск Core скрипта и получение конечного сообщения
def repeater():
    data = Core.main_fun()
    for item in range(len(data)):
        item = str(item+1)
        print(type(data[item]))
    
def main_func():
    while True:
    
        repeater()
        time.sleep(180)

if __name__ == "__main__":
    main_func()
'''