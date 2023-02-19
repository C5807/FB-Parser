from random import randint
import time
import Core

from socket import timeout
import telebot

from Config import token
from Config import keycode
from Config import whitelist

def cheker():
    print('checker start')
    l_data = Core.main_fun()

    try:
        for item in range(len(l_data)):
            item = str(item+1)
            team = l_data[item]['team']
            fpr = l_data[item]['fpr']
            goals = l_data[item]['goals']
            min = l_data[item]['min']
            score = l_data[item]['score']

            msg = str(
                    'Команды: ' + team +
                    '\nБолее: ' + fpr +
                    '\nКоличество голов: ' + goals +
                    '\nМинута: '+ min +
                    '\nСчёт: '+ score
                )
            l_matches = []

            print('checking...')
            if team not in l_ckecklist and team not in l_matches:
                l_ckecklist.append(team)
                l_matches.append(msg)
                print('new match added')
                
            else:
                continue

            return l_matches

    except:
        print(':p')

def mailing():
    for user in whitelist:
        try:
            for item in range(len(cheker())):
                try:
                    print('send')
                    bot.send_message(chat_id=user, text=(cheker()))
                except:
                    print('not send')
        except:
            print('mailing error')
def pol():
    
    mailing()
    print('mailing start')

def main():
    while True:
        cheker()        
        pol()
        print('sleeep.... z-z-z...')
        time.sleep(randint(30,60))

if __name__ == '__main__':
    l_ckecklist = []
    bot = telebot.TeleBot(token)
    main()

print('pol')
bot.polling()