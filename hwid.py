import os
import requests
import time
import subprocess
import urllib3

urllib3.disable_warnings() # desabilita o log do request

hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip() # pega o hwid
request = requests.get('https://pastebin.com/raw/LINK', verify=False) # entra no link onde armazena os hwid's

def menu():
    os.system("cls")
    print("oi")

if hwid in request.text: # checa se o hwid é válido
   print("HWID autorizado, redirecionando...")
   time.sleep(2.4)
   menu()
else: # checa se o hwid é inválido
   print("HWID não autorizado")
   time.sleep(2.4)
   quit()

if __name__ == '__main__':
    menu()
