import pyautogui, time

pauseSeconds = 0.3

# 
pyautogui.alert('ATENÇÃO!!! Em quanto programa estiver em funcionamento não mecher no Computador até receber novo aviso de tudo pronto.')
pyautogui.PAUSE = 0.5
pyautogui.hotkey('winleft') #segura e aperte outro
time.sleep(1)
pyautogui.typewrite('anydesk', interval=0.05) #escreva
pyautogui.press('enter', ) #um click no teclado
time.sleep(2)
pyautogui.click(800,180)
time.sleep(1)
pyautogui.typewrite('375', interval=0.10)
time.sleep(1)
pyautogui.click(800,200)
time.sleep(35)
pyautogui.click(1457,914)
pyautogui.click()
time.sleep(2)
pyautogui.doubleClick(597,736)
time.sleep(5)
pyautogui.doubleClick(770,335)
time.sleep(3)
pyautogui.click(1152,757)
time.sleep(1)
pyautogui.click(745,670)
time.sleep(1)
pyautogui.click(743,701)
time.sleep(1)
pyautogui.click(853,779)
time.sleep(14)
pyautogui.click(936,784)
time.sleep(1)
pyautogui.click(1223,750)
time.sleep(1)
pyautogui.click(1341,239)
time.sleep(2)
pyautogui.click(1901,7)
time.sleep(1)
pyautogui.alert('OPERAÇÃO COMCLUIDA COM SUCESSO, AGORA VOCÊ JÁ PODE USAR O COMPUTADOR, OBRIGADO.')


#pyautogui.typewrite('vai se fuder otario.', interval=0.10) #escreva com intervalo
#pyautogui.press('enter', )
#pyautogui.typewrite('aqui é hacker.', interval=0.15)
#time.sleep(1)
#pyautogui.hotkey('alt', 'f4')
#pyautogui.press('tab',)
#pyautogui.press('enter',)
