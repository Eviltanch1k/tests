from selenium.webdriver.common.by import By

from components.components import Components


class TextBoxPage:
    name = "TextBoxPage"
    url = "https://demoqa.com/text-box"

    def __init__(self, driver):
        self.driver = driver

        self.full_name = Components(driver, (By.CSS_SELECTOR, "input#userName"))
        self.current_address = Components(driver, (By.CSS_SELECTOR, "textarea#currentAddress"))
        self.submit_button = Components(driver, (By.CSS_SELECTOR, "button#submit"))

        self.output_name = Components(driver, (By.CSS_SELECTOR, "#output #name"))
        self.output_current_address = Components(driver, (By.CSS_SELECTOR, "#output #currentAddress"))

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
