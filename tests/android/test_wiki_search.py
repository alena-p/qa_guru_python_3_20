import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


def test_search_results():
    with allure.step("Activate search field"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Type search request"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
        ).send_keys("BrowserStack")
    with allure.step("Verify serach results are present"):
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
        ).should(have.size_greater_than(0))


def test_open_article():
    with allure.step("Activate search field"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Type search request"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
        ).send_keys("obama")
    with allure.step("Click to the first article"):
        browser.all(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_container")
        ).first.click()
    with allure.step("Verify article is open"):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(
            have.text("An error occurred")
        )
