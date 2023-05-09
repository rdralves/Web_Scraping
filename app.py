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
        titulos = self.webdrive.find_elements( "//a[@id='video-title']")
        for titulo in titulos:
            print(f"video encontrado {titulo}").text


        input("jdfkjdsk")


bot = RoboYoutube()
bot.busca("teste")
input("digite algo")