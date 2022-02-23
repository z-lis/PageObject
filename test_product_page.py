import time
import pytest
from pages.base_page import BasePage
from pages.product_page import ProductPage


@pytest.mark.parametrize('promo_number', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_number}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    # time.sleep(2)
    page.solve_quiz_and_get_code()
    # time.sleep(1000)
    page.product_name_must_match()
    page.product_price_must_match()
