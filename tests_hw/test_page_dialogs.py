from .pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    """
    1. Перейти на https://demoqa.com/modal-dialogs
    2. Проверить, что кнопок подменю на странице — 5 шт.
    """
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    expected_count = 5
    actual_count = modal_page.submenu_buttons.get_count()

    assert actual_count == expected_count, (
        f"Ожидалось {expected_count} кнопок подменю, "
        f"фактически найдено: {actual_count}"
    )


def test_navigation_modal(browser):
    """
    1. Перейти на https://demoqa.com/modal-dialogs
    2. Обновить страницу
    3. Перейти на главную страницу через иконку
    4. Сделать шаг назад стрелкой браузера
    5. Установить размеры экрана 900x400
    6. Сделать шаг вперёд стрелкой браузера
    7. Проверить URL главной страницы
    8. Проверить title главной страницы
    9. Вернуть размеры экрана по умолчанию 1000x1000
    """
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    browser.refresh()

    modal_page.home_icon.click()

    browser.back()

    browser.set_window_size(900, 400)

    browser.forward()

    expected_url = "https://demoqa.com/"
    assert browser.current_url == expected_url, (
        f"Ожидался URL {expected_url!r}, фактический: {browser.current_url!r}"
    )

    expected_title = "DEMOQA"
    assert browser.title == expected_title, (
        f"Ожидался title {expected_title!r}, фактический: {browser.title!r}"
    )

    browser.set_window_size(1000, 1000)
