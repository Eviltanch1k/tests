import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.web_tables_page import WebTablesPage


FIRST_NAME = "Алексей"
LAST_NAME = "Смирнов"
EMAIL = "alexey@test.com"
AGE = "30"
SALARY = "75000"
DEPARTMENT = "QA"


def test_web_tables_crud(browser):
    """
    a. Страница открывается, есть кнопка Add
    b. По клику на Add открывается диалог
    c. Нельзя сохранить пустую форму — диалог остаётся
    d. После заполнения и Submit — диалог закрывается, запись в таблице
    e. Клик на карандаш — диалог открывается с введёнными данными
    f. Изменить имя и сохранить — таблица обновляется
    g. Клик на корзину — запись удаляется
    """
    page = WebTablesPage(browser)
    page.visit()

    # b. Клик Add — диалог открывается
    page.add_button.click()
    assert page.modal_dialog.is_visible(), "Диалог не открылся после клика Add"

    # c. Отправка пустой формы — диалог должен остаться
    page.submit_button.click()
    assert page.modal_dialog.is_visible(), (
        "Диалог закрылся при отправке пустой формы — ожидалась блокировка"
    )

    # d. Заполняем форму и сохраняем
    page.fill_form(FIRST_NAME, LAST_NAME, EMAIL, AGE, SALARY, DEPARTMENT)
    page.submit_button.click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog"))
    )
    assert page.is_record_in_table(FIRST_NAME), (
        f"Запись '{FIRST_NAME}' не появилась в таблице после добавления"
    )

    # e. Клик на карандаш — диалог открывается с данными
    page.get_edit_button(FIRST_NAME).click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog"))
    )
    assert page.first_name_input.get_attribute("value") == FIRST_NAME, (
        f"В диалоге редактирования имя не совпадает: "
        f"'{page.first_name_input.get_attribute('value')}' != '{FIRST_NAME}'"
    )

    # f. Изменяем имя и сохраняем
    updated_name = "Дмитрий"
    page.first_name_input.find_element().clear()
    page.first_name_input.send_keys(updated_name)
    page.submit_button.click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.modal-dialog"))
    )
    assert page.is_record_in_table(updated_name), (
        f"Обновлённое имя '{updated_name}' не отображается в таблице"
    )
    assert not page.is_record_in_table(FIRST_NAME), (
        f"Старое имя '{FIRST_NAME}' всё ещё есть в таблице после обновления"
    )

    # g. Клик на корзину — запись удаляется
    page.get_delete_button(updated_name).click()
    time.sleep(1)
    assert not page.is_record_in_table(updated_name), (
        f"Запись '{updated_name}' всё ещё есть в таблице после удаления"
    )
