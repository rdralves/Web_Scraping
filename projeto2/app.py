# Importação da biblioteca Selenium
from selenium import webdriver
import os 

os.system("cls")

# Instanciando o Selenium
url = webdriver.Chrome()

# abrindo a página
url.get('https://rdralves.github.io/home/')

# preencher email
url.find_element('//*[@id="exampleInputEmail1"]').send_keys('rdr@gmail.com')
# preecher cpf

# peencher senha

# clicar no botão Enviar

input('qualquer coisa...')
