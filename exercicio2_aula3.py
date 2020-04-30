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

a = browser.find_element_by_tag_name('a')
p = browser.find_elements_by_tag_name('p')

number = r.search(r"\d+", p[-1].text)

a.click()

p = browser.find_elements_by_tag_name('p')

result = r.search(r"\d+", p[-1].text)

while number.group() != result.group():
    a.click()
    p = browser.find_elements_by_tag_name('p')
    result = r.search(r"\d+", p[-1].text)

sleep(2)
browser.quit()
