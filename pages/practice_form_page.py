from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.components import Components


class PracticeFormPage:
    name = "PracticeFormPage"
    url = "https://demoqa.com/automation-practice-form"

    def __init__(self, driver):
        self.driver = driver

        self.first_name = Components(driver, (By.CSS_SELECTOR, "input#firstName"))
        self.last_name = Components(driver, (By.CSS_SELECTOR, "input#lastName"))
        self.user_email = Components(driver, (By.CSS_SELECTOR, "input#userEmail"))
        self.submit_button = Components(driver, (By.CSS_SELECTOR, "button#submit"))
        self.form = Components(driver, (By.CSS_SELECTOR, "form"))

        self.state_input = Components(
            driver, (By.CSS_SELECTOR, "#state input")
        )
        self.city_input = Components(
            driver, (By.CSS_SELECTOR, "#city input")
        )

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)

    def select_state(self, state_name: str):
        self.state_input.find_element().send_keys(state_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[class*='option']")
            )
        ).click()

    def select_city(self, city_name: str):
        self.city_input.find_element().send_keys(city_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[class*='option']")
            )
        ).click()
