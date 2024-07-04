from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class BasePage:
    """
    This class contains all common elements and functionalities available to all pages.
    """

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.driver.implicitly_wait(20)

    def click(self, by_locator, wait=20) -> None:
        """
        performs click on web element whose locator is passed to it.
        :param by_locator: by_locator: ways to identify one or more specific elements in the DOM.
        :param wait: time in seconds to wait untilTimeoutException is thrown.
        :return: None
        """
        WebDriverWait(self.driver, wait).until(ec.element_to_be_clickable(by_locator)).click()

    def assert_element_text(self, by_locator, element_text, wait=20) -> None:
        """
        asserts comparison of a web element's text with passed in text.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param element_text: the text that should be compared to the element's text
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: None
        """
        assert WebDriverWait(self.driver, wait).until(ec.visibility_of_element_located(by_locator)).text == element_text

    def enter_text(self, by_locator, text, wait=20) -> None:
        """
        performs text entry of the passed in text, in a web element whose locator is passed to it.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param text: the text that should be inserted into the element.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: None
        """
        WebDriverWait(self.driver, wait).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    # This function checks if the web element whose locator has been passed to it, is enabled or not
    # and returns web element if it is enabled.
    def is_enabled(self, by_locator, wait=20) -> bool:
        """
        check if element is enabled or not.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: true is element is enabled, false otherwise.
        """
        return WebDriverWait(self.driver, wait).until(ec.visibility_of_element_located(by_locator)).is_displayed()

    # This function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_displayed(self, by_locator, wait=20) -> bool:
        """
        check if element it visible or not.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: true is element is enabled, false otherwise.
        """
        return WebDriverWait(self.driver, wait).until(ec.visibility_of_element_located(by_locator)).is_displayed()

    def hover_to(self, by_locator, wait=20) -> None:
        """
        moves the mouse pointer over a web element whose locator has been passed to it.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: None
        """
        ActionChains(self.driver).move_to_element(
            WebDriverWait(self.driver, wait).until(ec.visibility_of_element_located(by_locator))).perform()

    def find_element(self, by_locator, expected_conditions, wait=20) -> WebElement:
        """
        locate element in a page.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param expected_conditions: wait for a certain condition to occur.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: web element.
        """
        return WebDriverWait(self.driver, wait).until(expected_conditions(by_locator))

    def find_elements(self, by_locator, expected_conditions, wait=20) -> List[WebElement]:
        """
        locate elements in a page.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param expected_conditions: wait for a certain condition to occur.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: list of webelements.
        """
        return WebDriverWait(self.driver, wait).until(expected_conditions(by_locator))

    def find_element_by_text(self, text, wait=20) -> WebElement:
        """
        Locate element by text.
        :param text: the text that should exist in the element.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: web element
        """
        return WebDriverWait(self.driver, wait).until(
            ec.element_to_be_clickable((By.XPATH, f'//*[normalize-space(text()) = \'{text}\']')))

    def click_element_by_text(self, text) -> None:
        """
        click element by text value.
        :param text: the text that should exist in the element.
        :return: None
        """
        self.find_element_by_text(text).click()

    def click_using_javascript(self, element) -> None:
        """
        performs click on web element using JavaScript whose locator is passed to it.
        :param element: web element to scroll into.
        :return: None
        """
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_using_coordinate(self, x, y) -> None:
        """
        scrolls the page to absolute coordinates.
        :param x: scrollLeft
        :param y: scrollTop
        :return: None.
        """
        self.driver.execute_script(f'window.scrollBy({x},{y})')

    def scroll_button_till_end(self) -> None:
        """
        scroll the page to the button.
        :return: None.
        """
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def find_element_and_scroll(self, by_locator, expected_conditions, wait=20) -> None:
        """
        scroll to the element we want to find.
        :param by_locator: ways to identify one or more specific elements in the DOM.
        :param expected_conditions: wait for a certain condition to occur.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: None.
        """
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            WebDriverWait(self.driver, wait).until(expected_conditions(by_locator)))

    def scroll_to_element(self, element) -> None:
        """
        scroll to the element.
        :param element: web element to scroll into.
        :return: None.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_url(self, url: str, wait: int = 20) -> None:
        """
        Waits until the current URL matches the specified URL.
        :param url: the URL to wait for.
        :param wait: time in seconds to wait until TimeoutException is thrown.
        :return: None
        """
        WebDriverWait(self.driver, wait).until(ec.url_to_be(url))
