# Importação da biblioteca Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os



dados = {
    'email': 'rdr@gmail.com',
    'cpf': 12365498798,
    'senha': 'rdr123'
}
os.system("cls")
print("Iniciando nosso robô...")

# Instanciando o Selenium
url = webdriver.Chrome()

# abre página
url.get('https://rdralves.github.io/home/')

# preencher email
url.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]').send_keys(dados['email'])
time.sleep(0.5)

# preenche cpf
url.find_element(By.XPATH, '//*[@id="exampleInputCPF"]').send_keys(dados['cpf'])
time.sleep(0.5)

# peenche senha
url.find_element(
    By.XPATH, '//*[@id="exampleInputPassword1"]').send_keys(dados['senha'])
time.sleep(0.5)

# clica no botão Enviar
url.find_element(By.XPATH, '/html/body/div/form/button').click()
time.sleep(0.5)

# finalizado o robo
print('Missão cumprinda...')