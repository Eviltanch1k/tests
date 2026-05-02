import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.web_tables_page import WebTablesPage


COLUMNS = ["First Name", "Last Name", "Age", "Email", "Salary", "Department"]


@pytest.mark.parametrize("column_name", COLUMNS)
def test_sort_by_column(browser, column_name):
    """
    При клике на заголовок столбца происходит сортировка:
    заголовок получает класс '-sort-asc'.
    При повторном клике — класс меняется на '-sort-desc'.
    """
    page = WebTablesPage(browser)
    page.visit()

    header_locator = (
        By.XPATH,
        f"//div[@class='rt-th rt-resizable-header -cursor-pointer']"
        f"[.//span[text()='{column_name}']]",
    )

    header = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(header_locator)
    )
    header.click()

    header = browser.find_element(*header_locator)
    classes_after_first_click = header.get_attribute("class")
    assert "-sort-asc" in classes_after_first_click, (
        f"После первого клика по '{column_name}' ожидался класс '-sort-asc', "
        f"фактические классы: '{classes_after_first_click}'"
    )

    header.click()

    header = browser.find_element(*header_locator)
    classes_after_second_click = header.get_attribute("class")
    assert "-sort-desc" in classes_after_second_click, (
        f"После второго клика по '{column_name}' ожидался класс '-sort-desc', "
        f"фактические классы: '{classes_after_second_click}'"
    )
