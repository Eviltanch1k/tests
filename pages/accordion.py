from selenium.webdriver.common.by import By

from ..components.components import Components


class Accordion:
    name = "Accordion"
    url = "https://demoqa.com/accordian"

    def __init__(self, driver):
        self.driver = driver

        self.section1_heading = Components(
            driver, (By.CSS_SELECTOR, "#section1Heading")
        )
        self.section1_content = Components(
            driver, (By.CSS_SELECTOR, "#section1Content > p")
        )

        self.section2_content_p1 = Components(
            driver, (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
        )
        self.section2_content_p2 = Components(
            driver, (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
        )
        self.section3_content = Components(
            driver, (By.CSS_SELECTOR, "#section3Content > p")
        )

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
