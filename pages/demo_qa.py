from selenium.webdriver.common.by import By

from ..components.components import Components


class DemoQa:
    name = "DemoQa"
    url = "https://demoqa.com/"

    def __init__(self, driver):
        self.driver = driver

        self.elements_card = Components(
            driver,
            (By.XPATH, "//h5[text()='Elements']/ancestor::div[contains(@class,'card')]"),
        )

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
