import pyautogui
import time

pyautogui.press('winleft')
time.sleep(1)
pyautogui.write("Bloco de Notas")
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('alt', 'Space') # Press the hotkey combination.
time.sleep(0.5)
pyautogui.press(['down', 'down', 'down', 'down'])  # Press the down arrow key 4 times.
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.write("Hello Word")
time.sleep(2)
# Pegando a posição atual do mouse
#currentMouseX, currentMouseY = pyautogui.position()
#print(currentMouseX, currentMouseY)
pyautogui.moveTo(24, 32)
pyautogui.click()
pyautogui.press(['down', 'down', 'down', 'down'])
pyautogui.press('enter')
pyautogui.write("teste_pyautogui")
time.sleep(1)
pyautogui.moveTo(790, 548)
pyautogui.click()
pyautogui.moveTo(1890, 9)
pyautogui.click()

#pip freeze > requirements.txt ==> Salvando a lista de requerimentos
#pip install -r requirements.txt ==> Instalando as dependencias do projeto
#pip install pip-chill ==> Cria um arquivo de dependiencias sem pacotes de terceiros

# ===== Criando um arquivo executavel =====
# Instale o pacote "pyinstaller"
# Execute o comando no terminal ==> "pyinstaller --onefile -w introduction.py"