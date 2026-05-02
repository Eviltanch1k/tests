from selenium.webdriver.common.by import By

from components.components import Components


class ModalDialogs:
    name = "ModalDialogs"
    url = "https://demoqa.com/modal-dialogs"

    def __init__(self, driver):
        self.driver = driver

        self.submenu_buttons = Components(
            driver,
            (By.CSS_SELECTOR, "div.element-list.show ul.menu-list > li"),
        )

        self.home_icon = Components(
            driver,
            (By.CSS_SELECTOR, "header a"),
        )

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
