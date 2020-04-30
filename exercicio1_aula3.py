from selenium.webdriver import Firefox
from time import sleep
import pprint

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

browser = Firefox()

browser.get(url)

sleep(5)

h1 = browser.find_element_by_tag_name("h1")
ps = browser.find_elements_by_tag_name("p")

pp = pprint.PrettyPrinter(indent=4)
d_values = {}

for p in range(len(ps)):
    d_values[ps[p].get_attribute("atributo")] = ps[p].text

d = {h1.text: d_values}

pprint.pprint(d)
