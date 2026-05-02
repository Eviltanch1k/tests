from pages.practice_form_page import PracticeFormPage


def test_fill_state_and_city(browser):
    """
    1. Перейти на https://demoqa.com/automation-practice-form
    2. Заполнить поле State (выбрать из выпадающего списка)
    3. Заполнить поле City (выбрать из выпадающего списка)
    """
    state_name = "NCR"
    city_name = "Delhi"

    page = PracticeFormPage(browser)
    page.visit()

    page.select_state(state_name)
    page.select_city(city_name)
