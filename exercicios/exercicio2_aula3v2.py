# Crie um programa com selenium
# - Jogue o jogo
# - Quando vc ganhar o script deve parar de ser executado

from selenium.webdriver import Firefox
from time import sleep
import re as r


url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

browser = Firefox()
browser.get(url)

sleep(10)

a = browser.find_element_by_tag_name("a")
msg = ''

while 'Você ganhou' not in msg:
    a.click()
    msg = browser.find_elements_by_tag_name("p")[-1].text

browser.quit()
