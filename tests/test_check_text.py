import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.components import Components


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


def test_check_footer_text(driver):
    driver.get("https://demoqa.com/")

    footer = Components(driver, (By.CSS_SELECTOR, "footer span"))
    expected_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
    actual_text = footer.get_text()

    assert actual_text == expected_text, (
        f"Текст в подвале не совпадает.\n"
        f"Ожидалось: {expected_text!r}\n"
        f"Получено:  {actual_text!r}"
    )


def test_check_elements_page_center_text(driver):
    driver.get("https://demoqa.com/")

    elements_card = Components(
        driver,
        (By.XPATH, "//h5[text()='Elements']/ancestor::div[contains(@class,'card')]"),
    )
    elements_card.click()

    WebDriverWait(driver, 10).until(EC.url_contains("/elements"))

    center_text = Components(
        driver,
        (By.CSS_SELECTOR, "div.col-12.mt-4.col-md-6 .main-header"),
    )
    expected_text = "Please select an item from left to start practice."
    actual_text = center_text.get_text()

    assert actual_text == expected_text, (
        f"Текст по центру не совпадает.\n"
        f"Ожидалось: {expected_text!r}\n"
        f"Получено:  {actual_text!r}"
    )
