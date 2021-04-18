import math
import time

from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_css_selector('#input_value')

    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    rbutton = browser.find_element_by_css_selector('#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rbutton)
    rbutton.click()
    button = browser.find_element_by_css_selector('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
