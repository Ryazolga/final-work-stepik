from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #----alternate page transition
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
        #----in test_main_page.py uncomment to line 11 , and comment to line 8,10

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Registration link is not presented"

