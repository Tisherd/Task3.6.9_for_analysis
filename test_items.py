import time


def test_checking_button_ShopCard(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")