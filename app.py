from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Instanciando o selenium, definindo navegador e abrindo página, onde se fará a raspagem de dados
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Abrindo um site com Selenium
driver.get('https://sitepreco1.netlify.app/')