from pages.text_box_page import TextBoxPage


def test_text_box(browser):
    """
    1. Перейти на https://demoqa.com/text-box
    2. Ввести текст в поля Full Name и Current Address
    3. Нажать Submit
    4. Проверить, что снизу появились 2 элемента с нашим текстом
    """
    full_name_text = "Иван Иванов"
    current_address_text = "ул. Ленина, д. 10, кв. 5"

    page = TextBoxPage(browser)
    page.visit()

    page.full_name.send_keys(full_name_text)
    page.current_address.send_keys(current_address_text)
    page.submit_button.click()

    assert full_name_text in page.output_name.get_text(), (
        f"Текст '{full_name_text}' не найден в выводе Name: "
        f"'{page.output_name.get_text()}'"
    )
    assert current_address_text in page.output_current_address.get_text(), (
        f"Текст '{current_address_text}' не найден в выводе Current Address: "
        f"'{page.output_current_address.get_text()}'"
    )
