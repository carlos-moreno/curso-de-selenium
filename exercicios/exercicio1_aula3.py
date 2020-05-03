# Gere um dicionário, onde a chave é a tag h1
# - O valor deve ser um novo dicionário
# - cada chave do valor deverá ser o valor de 'atributo'
# - cada valor deve ser o texto contido no elemento

from selenium.webdriver import Firefox
from time import sleep
import pprint

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

browser = Firefox()

browser.get(url)

sleep(5)

h1 = browser.find_element_by_tag_name('h1')
ps = browser.find_elements_by_tag_name('p')

d_values = {}

for p in ps:
    d_values[p.get_attribute('atributo')] = p.text

pprint.pprint({h1.text: d_values})

browser.quit()
