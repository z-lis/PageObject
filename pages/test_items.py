def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_button = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))

    assert add_button > 0, 'Элемент не найден'