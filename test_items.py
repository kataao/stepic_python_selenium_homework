import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button_should_be_dispalyed(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(10)
    assert len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")) == 1, "Button 'Add to basket' is not displayed"
    