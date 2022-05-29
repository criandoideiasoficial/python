from logging import handlers
import pandas as pd
lista_meses = ['janeiro', 'fevereiro']

for mes in lista_meses:
    print(mes)


#como executar comando em cmd com python
#import os
#os.system('notepad')


#abrindo uma pagina e clicar algo
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.firefox.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://pipelinepiscinas.com.br")   
    time.sleep(5)