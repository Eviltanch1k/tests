from selenium.webdriver.common.by import By

from components.components import Components


class LinksPage:
    name = "LinksPage"
    url = "https://demoqa.com/links"

    def __init__(self, driver):
        self.driver = driver

        self.home_link = Components(driver, (By.CSS_SELECTOR, "#simpleLink"))

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
