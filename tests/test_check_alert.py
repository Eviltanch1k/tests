from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.alerts_page import AlertsPage


def test_timer_alert(browser):
    """
    i.  На странице присутствует кнопка #timerAlertButton
    ii. Через 5 сек после клика всплывает алерт
    """
    page = AlertsPage(browser)
    page.visit()

    assert page.timer_alert_button.is_visible(), (
        "Кнопка #timerAlertButton не найдена на странице"
    )

    page.timer_alert_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert is not None, "Алерт не появился в течение 10 секунд после клика"

    alert_text = alert.text
    print(f"Текст алерта: {alert_text}")
    alert.accept()
