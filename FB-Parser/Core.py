import requests
from bs4 import BeautifulSoup
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from Config import WebDriver

def get_html(url):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, WebDriver, 'chromedriver')   #Папка с драйвером для установленного браузера

    webdriver_path = file_path
    driver = webdriver.Chrome(webdriver_path)
    driver.maximize_window()

    driver.get(url=url)
    time.sleep(3)

    html = driver.page_source

    return html


def zero_one():
    r = 1
    def one_zero():
        nonlocal r
        r += 1*k
        k *= -1
        return r
    return one_zero
      
def parser(soup):
    l_teams = []
    l_fpr = []
    l_goals = []
    l_min = []
    l_score = []

    #Парс нечетных блоков
    trs_0 = soup.findAll('div', class_='rcnt tr_0')
    
    for i in range(len(trs_0)):
        
        #Команды и дата
        teams_date = trs_0[i].find('div', class_='tnms').find('a', class_='tnmscn')
        
        home_team = teams_date.find('span', class_='homeTeam').text
        away_team = teams_date.find('span', class_='awayTeam').text
        date = teams_date.find('span', class_='date_bah').text
        teams = (home_team + ' > ' + away_team + ': ' + date)
        l_teams.append(teams)

        #Более/Менее                                                                                
        fprc = str(trs_0[i].find('div', class_='fprc'))
        
        for a in range(len(fprc) - 1):
            if (fprc[a] == 'r' and fprc[a + 1] == '"' and fprc[a + 2] == '>'):
                probability_more = fprc[a + 3:a + 5]
                l_fpr.append(probability_more)

        #Колличество голов
        tabonly = str(trs_0[i].find('div', class_='avg_sc tabonly'))
        
        for b in range(len(tabonly) - 1):
            if (tabonly[b] == 'y' and tabonly[b + 1] == '"' and tabonly[b + 2] == '>'):
                goals = tabonly[b + 3:b + 7]
                l_goals.append(goals)

        #Текущая минута
        time = str(trs_0[i].find('span', class_='l_min'))

        for c in range(len(time) - 1):
            if (time[c] == 'n' and time[c + 1] == '"' and time[c + 2] == '>' and time[c + 3] != '<'):
                min = time[c + 3:c + 5]
                l_min.append(min)

            elif (time[c] == 'n' and time[c + 1] == '"' and time[c + 2] == '>' and time[c + 3] == '<'):
                l_min.append('non')

        #Счет
        score = str(trs_0[i].find('b', class_='l_scr'))
        score = score[17:]
        
        if len(score)>4:
            l_score.append(score[:5])
        else:
            l_score.append('non')
            '''
        for d in range(len(score) - 1):
            if (score[d] == 'r' and score[d + 1] == '"' and score[d + 2] == '>') and score[d + 3]!= '<':
                score = score[d + 3:d + 8]
                l_score.append(score)

            elif (score[d] == 'r' and score[d + 1] == '"' and score[d + 2] == '>') and score[d + 3] == '<':
                l_score.append('non')
            '''
    
        #####################################################################################################
   
    #Парс четных блоков
    trs_1 = soup.findAll('div', class_='rcnt tr_1')

    for i in range(len(trs_1)):

        #Команды и дата
        teams_date = trs_1[i].find('div', class_='tnms').find('a', class_='tnmscn')
        
        home_team = teams_date.find('span', class_='homeTeam').text
        away_team = teams_date.find('span', class_='awayTeam').text
        date = teams_date.find('span', class_='date_bah').text
        teams = (home_team + ' > ' + away_team + ': ' + date)
        l_teams.append(teams)

        #Более/Менее                                                                                
        fprc = str(trs_1[i].find('div', class_='fprc'))
        
        for a in range(len(fprc) - 1):
            if (fprc[a] == 'r' and fprc[a + 1] == '"' and fprc[a + 2] == '>'):
                probability_more = fprc[a + 3:a + 5]
                l_fpr.append(probability_more)


        #Колличество голов
        tabonly = str(trs_1[i].find('div', class_='avg_sc tabonly'))
        
        for b in range(len(tabonly) - 1):
            if (tabonly[b] == 'y' and tabonly[b + 1] == '"' and tabonly[b + 2] == '>'):
                goals = tabonly[b + 3:b + 7]
                l_goals.append(goals)

        #Текущая минута
        time = str(trs_1[i].find('span', class_='l_min'))

        for c in range(len(time) - 1):
            if (time[c] == 'n' and time[c + 1] == '"' and time[c + 2] == '>' and time[c + 3] != '<'):
                min = time[c + 3:c + 5]
                l_min.append(min)

            elif (time[c] == 'n' and time[c + 1] == '"' and time[c + 2] == '>' and time[c + 3] == '<'):
                l_min.append('non')

        #Счет
        score = str(trs_1[i].find('b', class_='l_scr'))
        score = score[17:]
        
        if len(score)>4:
            l_score.append(score[:5])
        else:
            l_score.append('non')

    return l_teams, l_fpr, l_goals,l_min, l_score


#Проверка по условиям всего списка матчей
def get_match(l_teams, l_fpr, l_goals,l_min, l_score):        

    l = [len(l_teams), len(l_fpr),len(l_goals),len(l_min),len(l_score)]
    for i in range(4):
        if l[i]>l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    print(l)


    l_target = {}
    for i in range(l[0]):
        try:
            if int(l_fpr[i])>=52 and l_min[i]!='non' and l_score[i]=='0 - 0':
                print(l_teams[i])
                print(l_fpr[i])
                print(l_goals[i])
                print(l_min[i])
                print(l_score[i])
                match = {'team': f'{l_teams[i]}',
                         'fpr': f'{l_fpr[i]}',
                         'goals': f'{l_goals[i]}',
                         'min': f'{l_min[i]}',
                         'score': f'{l_score[i]}'}
                l_target[f'{len(l_target)+1}'] = match
        except Exception:
            print(':)')
    return l_target

    
def main_fun():
    url = 'https://www.forebet.com/ru/prognozi-na-segodnq/prognozi-mnee-bolee' #Ссылка на ресурс для парса

    r = get_html(url)
    soup = BeautifulSoup(r , "lxml")

    l_teams, l_fpr, l_goals,l_min, l_score = parser(soup)
    print(len(l_teams), len(l_fpr), len(l_goals), len(l_min), len(l_score))

    responce = get_match(l_teams, l_fpr, l_goals,l_min, l_score)
    return responce
    

if __name__ == "__main__":
    main_fun()


    # parser(soup)
    # print(len(l_teams), len(l_fpr), len(l_goals), len(l_min), len(l_score))
    # #print(l_teams[1])
    # #print(l_fpr[1])
    # #print(l_goals[1])
    # #print(l_min[1])
    # #print(l_score[1])


