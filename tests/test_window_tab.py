from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.links_page import LinksPage


def test_home_link_opens_new_tab(browser):
    """
    b. На странице есть ссылка 'Home'
    c. Текст ссылки == 'Home'
    d. href ссылки == 'https://demoqa.com'
    e. При клике на ссылку открывается новая вкладка
    """
    page = LinksPage(browser)
    page.visit()

    assert page.home_link.is_visible(), (
        "Ссылка 'Home' не найдена на странице"
    )

    link_text = page.home_link.get_text()
    assert link_text == "Home", (
        f"Текст ссылки не совпадает. Ожидалось: 'Home', фактически: '{link_text}'"
    )

    link_href = page.home_link.get_attribute("href")
    assert link_href == "https://demoqa.com", (
        f"href ссылки не совпадает. Ожидалось: 'https://demoqa.com', "
        f"фактически: '{link_href}'"
    )

    original_handles = browser.window_handles
    page.home_link.click()

    WebDriverWait(browser, 10).until(
        EC.new_window_is_opened(original_handles)
    )
    new_handles = browser.window_handles
    assert len(new_handles) == len(original_handles) + 1, (
        f"Новая вкладка не открылась. "
        f"Было: {len(original_handles)}, стало: {len(new_handles)}"
    )

    browser.switch_to.window(new_handles[-1])
    print(f"Новая вкладка открыта: {browser.current_url}")
    browser.close()
    browser.switch_to.window(original_handles[0])
