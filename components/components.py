from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Components:
    def __init__(self, driver: WebDriver, locator: tuple, timeout: int = 10):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout

    def find_element(self) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.locator)
        )

    def click(self) -> None:
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.locator)
        ).click()

    def get_text(self) -> str:
        return str(self.find_element().text)
