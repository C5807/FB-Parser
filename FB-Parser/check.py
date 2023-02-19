from random import randint
import time
import Bot
import Core






def repeater(l_check_In):
    l_check = l_check_In
    data = Core.main_fun()

    for item in range(len(data)):
        item = str(item+1)
        # WARNING
        team = data[item]['team']
        print(type(team))
        # WARNING
        print(data[item])

        if team in l_check:
            del data[item]
        else:
            
            l_check[f'{team}'+'donilka'] = {'team': f'{data[item]["team"]}',
                                  'fpr': f'{data[item]["fpr"]}',
                                  'goals': f'{data[item]["goals"]}',
                                  'min': f'{data[item]["min"]}',
                                  'score': f'{data[item]["score"]}'}
            
            
        print(data[item])
    print(l_check)
    return l_check

def main_func():
    l_check = {}
    while True:
    
        msg = repeater(l_check)
        if len(msg)!=0:
            Bot.mailing(msg)
        else:
            print(':0')

        time.sleep(randint(180,360))
    

if __name__ == "__main__":
    main_func()
