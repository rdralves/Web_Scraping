# Importação da biblioteca Selenium
from selenium import webdriver

# Instanciando o Selenium
url = webdriver.Chrome()

# abrindo a página
url.get('https://forms.gle/fTG7MkjZqWaRgg2GA')

input('qualquer coisa...')
