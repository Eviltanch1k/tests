from selenium.webdriver.common.by import By

from components.components import Components


class ElementsPage:
    name = "ElementsPage"
    url = "https://demoqa.com/elements"

    def __init__(self, driver):
        self.driver = driver

        self.center_text = Components(
            driver,
            (By.CSS_SELECTOR, "div.col-12.mt-4.col-md-6 .main-header"),
        )

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
