import pyautogui
import time
# print('Posicione o MOUSE')
# time.sleep(3)
# x, y = pyautogui.position()
# print ("Posicao atual do mouse:")
# print ("x = "+str(x)+" y = "+str(y))

#retorna Truee se x & y estiverem dentro da tela
# print ("\nEsta dentro da tela?")
# resp = pyautogui.onScreen(x, y)
# print (str(resp))

pyautogui.click(1105, 1067)
pyautogui.moveTo(920, 523, 0)
for i in range(10):
    #pyautogui.moveTo(920, 523, 0)
    if(pyautogui.position != 920, 523):
        pyautogui.click()
    time.sleep(0.1)
pyautogui.hotkey('alt', 'tab')