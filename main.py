from logging import handlers
import pandas as pd
import time
lista_meses = ['Teste', 'Estamos testando sistema de email aguarda, o programa fechara automatico se estiver tudo ok.']

for mes in lista_meses:
    print(mes)

time.sleep(5)

#como executar comando em cmd com python
#import os
#os.system('notepad')



#abrindo uma pagina e clicar algo
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    navegador = p.chromium.launch(headless=True)
    pagina = navegador.new_page() 
    pagina.set_viewport_size({"width": 640, "height": 600})        
    pagina.goto("https://pipelinepiscinas.com.br/pipe/index.php")  
    time.sleep(8)
    pagina.keyboard.press("End")
    pagina.fill('xpath=//*[@id="nome"]', 'Osmar')
    pagina.fill('xpath=//*[@id="email"]', 'osmar@ppiscinas.com.br')
    pagina.select_option('xpath=//*[@id="setor"]', value='1')
    pagina.fill('xpath=//*[@id="fone"]', '1433221709')
    pagina.fill('xpath=//*[@id="cidade"]', 'cambará')
    pagina.select_option('xpath=//*[@id="encontre"]', value='Google')
    pagina.fill('xpath=//*[@id="texto"]', 'automacao')  
    pagina.fill('xpath=//*[@id="soma"]', '1')
    time.sleep(2)
    pagina.locator('xpath=//*[@id="btn_submit"]').click()
    time.sleep(3)

    pagina.goto("https://franquiapipeline.com/")
    time.sleep(5)
    pagina.keyboard.press("End")
    pagina.fill('xpath=//*[@id="form-field-name"]', 'Osmar')
    pagina.fill('xpath=//*[@id="form-field-cidade"]', 'automacao')
    pagina.fill('xpath=//*[@id="form-field-field_f4ac283"]', 'osmar@ppiscinas.com.br')
    pagina.fill('xpath=//*[@id="form-field-field_609cea0"]', '1433221709')
    time.sleep(2)
    pagina.locator('xpath=//*[@id="enviar"]').click()
    time.sleep(10)

    #pagina = navegador.close()


  