from pages.practice_form_page import PracticeFormPage


def test_login_form_validate(browser):
    """
    1. Перейти на https://demoqa.com/automation-practice-form
    2. Проверить плейсхолдеры у полей first_name, last_name, user_email
    3. Проверить атрибут 'pattern' у поля user_email
    4. Отправить пустую форму и проверить наличие класса 'was-validated' у формы
    """
    page = PracticeFormPage(browser)
    page.visit()

    assert page.first_name.get_attribute("placeholder") == "First Name", (
        f"Неверный placeholder у поля First Name: "
        f"'{page.first_name.get_attribute('placeholder')}'"
    )
    assert page.last_name.get_attribute("placeholder") == "Last Name", (
        f"Неверный placeholder у поля Last Name: "
        f"'{page.last_name.get_attribute('placeholder')}'"
    )
    assert page.user_email.get_attribute("placeholder") == "name@example.com", (
        f"Неверный placeholder у поля Email: "
        f"'{page.user_email.get_attribute('placeholder')}'"
    )

    assert page.user_email.get_attribute("pattern") is not None, (
        "Атрибут 'pattern' отсутствует у поля user_email"
    )

    page.submit_button.click()

    form_class = page.form.get_attribute("class")
    assert "was-validated" in form_class, (
        f"Класс 'was-validated' не найден у элемента формы после попытки "
        f"отправки пустой формы. Текущие классы: '{form_class}'"
    )
