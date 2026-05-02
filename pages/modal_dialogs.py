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
        self.home_icon = Components(driver, (By.CSS_SELECTOR, "header a"))

        self.small_modal_button = Components(driver, (By.CSS_SELECTOR, "#showSmallModal"))
        self.large_modal_button = Components(driver, (By.CSS_SELECTOR, "#showLargeModal"))

        self.small_modal_close = Components(driver, (By.CSS_SELECTOR, "#closeSmallModal"))
        self.large_modal_close = Components(driver, (By.CSS_SELECTOR, "#closeLargeModal"))

        self.modal_overlay = Components(driver, (By.CSS_SELECTOR, ".modal.show"))

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
