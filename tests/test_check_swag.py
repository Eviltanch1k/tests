from pages.swag_labs import SwagLabs


def test_check_icon(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_icon(), "Иконка login_logo не найдена"


def test_check_username(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_username(), "Поле имени пользователя не найдено"


def test_check_password(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_password(), "Поле пароля не найдено"
