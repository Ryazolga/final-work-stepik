from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login()

    page_login = LoginPage(browser,  browser.current_url)
    page_login.should_be_login_url()
    page_login.should_be_login_form()
    page_login.should_be_register_form()
