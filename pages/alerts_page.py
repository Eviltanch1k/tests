from selenium.webdriver.common.by import By

from components.components import Components


class AlertsPage:
    name = "AlertsPage"
    url = "https://demoqa.com/alerts"

    def __init__(self, driver):
        self.driver = driver

        self.timer_alert_button = Components(
            driver, (By.CSS_SELECTOR, "#timerAlertButton")
        )

    def visit(self):
        print(f"Открываем страницу {self.name}: {self.url}")
        self.driver.get(self.url)
