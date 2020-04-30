from selenium.webdriver import Firefox
from time import sleep

url = "https://curso-python-selenium.netlify.app/aula_03.html"

browser = Firefox()

browser.get(url)

sleep(5)

a = browser.find_element_by_tag_name("a")

for click in range(10):
    ps = browser.find_elements_by_tag_name("p")
    a.click()
    print(f"Valor de p {ps[-1].text} <--> valor do click {click}")

    print(f"Os valores são iguais {ps[-1].text == str(click)}")


print(f"texto de a: {a.text}")
