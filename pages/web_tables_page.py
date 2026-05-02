from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from components.components import Components


class WebTablesPage:
    name = "WebTablesPage"
    url = "https://demoqa.com/webtables"

    def __init__(self, driver):
        self.driver = driver

        self.add_button = Components(driver, (By.CSS_SELECTOR, "button#addNewRecordButton"))

        self.first_name_input = Components(driver, (By.CSS_SELECTOR, "input#firstName"))
        self.last_name_input = Components(driver, (By.CSS_SELECTOR, "input#lastName"))
        self.email_input = Components(driver, (By.CSS_SELECTOR, "input#userEmail"))
        self.age_input = Components(driver, (By.CSS_SELECTOR, "input#age"))
        self.salary_input = Components(driver, (By.CSS_SELECTOR, "input#salary"))
        self.department_input = Components(driver, (By.CSS_SELECTOR, "input#department"))
        self.submit_button = Components(driver, (By.CSS_SELECTOR, "button#submit"))

        self.modal_dialog = Components(driver, (By.CSS_SELECTOR, "div.modal-dialog"))

        self.next_button = Components(driver, (By.CSS_SELECTOR, "button.-next"))
        self.previous_button = Components(driver, (By.CSS_SELECTOR, "button.-previous"))
        self.pagination_total = Components(driver, (By.CSS_SELECTOR, "span.-totalPages"))

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)

    def fill_form(self, first_name, last_name, email, age, salary, department):
        self.first_name_input.find_element().clear()
        self.first_name_input.send_keys(first_name)
        self.last_name_input.find_element().clear()
        self.last_name_input.send_keys(last_name)
        self.email_input.find_element().clear()
        self.email_input.send_keys(email)
        self.age_input.find_element().clear()
        self.age_input.send_keys(age)
        self.salary_input.find_element().clear()
        self.salary_input.send_keys(salary)
        self.department_input.find_element().clear()
        self.department_input.send_keys(department)

    def add_record(self, first_name, last_name, email, age, salary, department):
        self.add_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog"))
        )
        self.fill_form(first_name, last_name, email, age, salary, department)
        self.submit_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog"))
        )

    def get_edit_button(self, row_text: str) -> Components:
        locator = (
            By.XPATH,
            f"//div[@class='rt-tr-group'][.//div[contains(text(),'{row_text}')]]"
            f"//span[@title='Edit']",
        )
        return Components(self.driver, locator)

    def get_delete_button(self, row_text: str) -> Components:
        locator = (
            By.XPATH,
            f"//div[@class='rt-tr-group'][.//div[contains(text(),'{row_text}')]]"
            f"//span[@title='Delete']",
        )
        return Components(self.driver, locator)

    def is_record_in_table(self, text: str) -> bool:
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        return any(text in row.text for row in rows)

    def set_rows_per_page(self, value: str):
        select_el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "select[aria-label='rows per page']")
            )
        )
        Select(select_el).select_by_visible_text(value)
