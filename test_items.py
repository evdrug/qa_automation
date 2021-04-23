def test_search_button_add_to_cart(browser):
    link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = browser.find_elements_by_css_selector('.btn-add-to-basket1')
    assert len(button) == 1, 'Элемент не найден!!!'