# Importação da biblioteca Selenium
from selenium import webdriver

# Instanciando o Selenium
url = webdriver.Chrome()

# abrindo a página
url.get('https://rdralves.github.io/home/')

input('qualquer coisa...')
