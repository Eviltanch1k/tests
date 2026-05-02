from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage


class SwagLabs(BasePage):
    def exist_icon(self) -> bool:
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_username(self) -> bool:
        try:
            self.find_element(locator='input#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_password(self) -> bool:
        try:
            self.find_element(locator='input#password')
        except NoSuchElementException:
            return False
        return True
