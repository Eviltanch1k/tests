import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.modal_dialogs import ModalDialogs


PAGE_URL = "https://demoqa.com/modal-dialogs"


@pytest.fixture(autouse=True)
def check_page_available():
    try:
        response = requests.get(PAGE_URL, timeout=5)
        if response.status_code != 200:
            pytest.skip(f"Страница недоступна, статус: {response.status_code}")
    except requests.RequestException as e:
        pytest.skip(f"Страница недоступна: {e}")


def test_check_modal(browser):
    """
    i.  На странице присутствуют 2 кнопки Small modal и Large modal
    ii. При клике на каждую открывается модальное окно
    iii.У каждого окна есть кнопка Close — по клику окно закрывается
    """
    page = ModalDialogs(browser)
    page.visit()

    # --- Small modal ---
    assert page.small_modal_button.is_visible(), (
        "Кнопка 'Small modal' не найдена на странице"
    )
    assert page.large_modal_button.is_visible(), (
        "Кнопка 'Large modal' не найдена на странице"
    )

    page.small_modal_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal.show"))
    )
    assert page.modal_overlay.is_visible(), (
        "Модальное окно Small не открылось после клика"
    )

    page.small_modal_close.click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal.show"))
    )
    assert not page.modal_overlay.is_visible(), (
        "Модальное окно Small не закрылось после клика Close"
    )

    # --- Large modal ---
    page.large_modal_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal.show"))
    )
    assert page.modal_overlay.is_visible(), (
        "Модальное окно Large не открылось после клика"
    )

    page.large_modal_close.click()
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal.show"))
    )
    assert not page.modal_overlay.is_visible(), (
        "Модальное окно Large не закрылось после клика Close"
    )
