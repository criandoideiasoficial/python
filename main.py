from logging import handlers
import pandas as pd
#lista_meses = ['janeiro', 'fevereiro']

#for mes in lista_meses:
#    print(mes)


#como executar comando em cmd com python
#import os
#os.system('notepad')


#abrindo uma pagina e clicar algo
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://pipelinepiscinas.com.br/pipe/index.php") 
    time.sleep(10)
    pagina.keyboard.press("End")
    pagina.fill('xpath=//*[@id="nome"]', 'Osmar')
    pagina.fill('xpath=//*[@id="email"]', 'osmar@ppiscinas.com.br')
    pagina.select_option('xpath=//*[@id="setor"]', value='1')
    pagina.fill('xpath=//*[@id="fone"]', '1433221709')
    pagina.fill('xpath=//*[@id="cidade"]', 'cambará')
    pagina.select_option('xpath=//*[@id="encontre"]', value='Google')
    pagina.fill('xpath=//*[@id="texto"]', 'automacao')  
    pagina.fill('xpath=//*[@id="soma"]', '1')
    time.sleep(5)
    pagina.locator('xpath=//*[@id="btn_submit"]').click()
    time.sleep(5)

    pagina.goto("https://franquiapipeline.com/")
    time.sleep(5)
    pagina.keyboard.press("End")
    pagina.fill('xpath=//*[@id="form-field-name"]', 'Osmar')
    pagina.fill('xpath=//*[@id="form-field-cidade"]', 'cambara')
    pagina.fill('xpath=//*[@id="form-field-field_f4ac283"]', 'osmar@ppiscinas.com.br')
    pagina.fill('xpath=//*[@id="form-field-telefone"]', '1433221709')
    time.sleep(5)
    pagina.locator('xpath=//*[@id="elementor-popup-modal-232"]/div/div[2]/div/section/div/div/div/div[3]/div/form/div/div[5]/button').click()
    time.sleep(5)

    #pagina = navegador.close()