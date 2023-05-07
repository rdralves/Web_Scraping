from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os

os.system("cls")

# Inciando a classe roboYoutube
class RoboYoutube():
    def __init__(self):
        self.webdrive = webdriver.Chrome()

    def busca(self, busca):
        url = f"https://www.youtube.com/results?search_query={busca}"
        self.webdrive.get(url)


bot = RoboYoutube()
bot.busca("como colocar codigo python no html com flask digao007sp")
input("fdjfkjadskfj")