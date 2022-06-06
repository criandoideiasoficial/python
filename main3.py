import pyautogui, time

pauseSeconds = 0.3

# Open Windows Calculator via CLI
pyautogui.hotkey('winleft', 'r') #segura e aperte outro
pyautogui.typewrite('notepad', ) #escreva
pyautogui.press('enter', ) #um click no teclado
time.sleep(1)

pyautogui.typewrite('vai se fuder otario.', interval=0.10) #escreva com intervalo
pyautogui.press('enter', )
pyautogui.typewrite('aqui é hacker.', interval=0.15)
time.sleep(1)
pyautogui.hotkey('alt', 'f4')
pyautogui.press('tab',)
pyautogui.press('enter',)

