import webbrowser
import time
import os

print('Почему ты плачешь?')
if input() == 'Я пуджа апнул':
    os.system('cls||clear')
    time.sleep(0.5)
    for i in range(2):
        for s in range(3):
            print('Загрузка', '.' *(s + 1), sep = '')
            time.sleep(0.5)
            os.system('cls||clear')
    webbrowser.open_new('https://store.steampowered.com/app/570/Dota_2/?l=russian')
time.sleep(1)