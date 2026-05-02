import time

from .pages.accordion import Accordion


def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert accordion.section1_content.is_visible(), (
        "Ожидалось, что #section1Content > p будет виден сразу после открытия страницы"
    )

    accordion.section1_heading.click()
    time.sleep(2)

    assert not accordion.section1_content.is_visible(), (
        "Ожидалось, что #section1Content > p будет скрыт после клика по #section1Heading"
    )


def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()

    assert not accordion.section2_content_p1.is_visible(), (
        "Ожидалось, что #section2Content > p:nth-child(1) будет скрыт по умолчанию"
    )
    assert not accordion.section2_content_p2.is_visible(), (
        "Ожидалось, что #section2Content > p:nth-child(2) будет скрыт по умолчанию"
    )
    assert not accordion.section3_content.is_visible(), (
        "Ожидалось, что #section3Content > p будет скрыт по умолчанию"
    )
