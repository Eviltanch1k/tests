from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.web_tables_page import WebTablesPage


RECORDS = [
    ("Анна", "Козлова", "anna@test.com", "25", "50000", "HR"),
    ("Борис", "Попов", "boris@test.com", "32", "60000", "Dev"),
    ("Вера", "Новикова", "vera@test.com", "28", "55000", "QA"),
]


def test_web_tables_pagination(browser):
    """
    Предусловия: страница открыта, кол-во строк установлено 5.

    a. Кнопки Next и Previous заблокированы (атрибут disabled)
    b. После добавления 3 записей появляется 2-я страница (of 2)
       и кнопка Next становится доступной
    c. Клик Next → открывается 2-я страница
    d. Клик Previous → открывается 1-я страница
    """
    page = WebTablesPage(browser)
    page.visit()

    # Предусловие: устанавливаем 5 строк на страницу
    page.set_rows_per_page("5")

    # a. Next и Previous задизейблены при 3 записях (меньше 5)
    assert page.next_button.get_attribute("disabled") is not None, (
        "Кнопка Next должна быть заблокирована при количестве записей <= 5"
    )
    assert page.previous_button.get_attribute("disabled") is not None, (
        "Кнопка Previous должна быть заблокирована при количестве записей <= 5"
    )

    # b. Добавляем 3 новые записи (итого 6 > 5 — нужна 2-я страница)
    for first, last, email, age, salary, dept in RECORDS:
        page.add_record(first, last, email, age, salary, dept)

    # Проверяем, что появилась 2-я страница "of 2"
    total_pages = page.pagination_total.get_text()
    assert total_pages == "2", (
        f"Ожидалось '2' страницы, фактически: '{total_pages}'"
    )

    # Кнопка Next стала доступной
    assert page.next_button.get_attribute("disabled") is None, (
        "Кнопка Next должна быть активна после добавления 3 записей"
    )

    # c. Клик Next → 2-я страница
    page.next_button.click()
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "input[aria-label='jump to page']"),
            "2"
        )
    )
    current_page = browser.find_element(
        By.CSS_SELECTOR, "input[aria-label='jump to page']"
    ).get_attribute("value")
    assert current_page == "2", (
        f"После клика Next ожидалась страница 2, фактически: '{current_page}'"
    )

    # d. Клик Previous → 1-я страница
    page.previous_button.click()
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "input[aria-label='jump to page']"),
            "1"
        )
    )
    current_page = browser.find_element(
        By.CSS_SELECTOR, "input[aria-label='jump to page']"
    ).get_attribute("value")
    assert current_page == "1", (
        f"После клика Previous ожидалась страница 1, фактически: '{current_page}'"
    )
