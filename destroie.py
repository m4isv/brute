import requests
from time import sleep
from os import system
from brute.arte import execute
import threading


system('clear')
execute()


verde = '\033[5;32m'
vermelhor = '\033[5;31m'
feixa = '\033[m'


url: str = input(f'{vermelhor} URL: {feixa}')

if not url.startswith('https://') and not url.endswith('/'):
	url = 'https://'+url
	url = url + '/'



def tarefa1():
    with open('brute/big.txt') as f:
        for pecorre in f.readlines():
            linhas = pecorre.strip()
            URL_COMPLETA: str = url + linhas
            req = requests.get(URL_COMPLETA)
            CODIGO = req.status_code
            print(f'{verde}{URL_COMPLETA}{feixa}: {vermelhor}{CODIGO}{feixa}')


threading.Thread(target=tarefa1).start()



    

            
