import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("button")

    button = browser.find_element_by_css_selector('button')
    button.click()
    time.sleep(1)

    browser.switch_to.window(browser.window_handles[1])

    time.sleep(1)
    x_element = browser.find_element_by_css_selector('#input_value')

    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector('button')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
