import time
from typing import List, Optional
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.common.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from src.managers.config_manager import ConfigManager

conf = ConfigManager()

BASE_URL = conf.get_config_value('settings', 'login', 'url', default=None)
USER_SETTINGS_BUTTON = (
    By.XPATH, '//div[@class=\'MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-1f7m2mg\']')
NUMBER_OF_TASKS_VALUE = (By.XPATH, '//span[@class=\' css-eh0jb8\']')
ADD_TASK_BUTTON = (By.XPATH, '//button[@class=\'MuiButtonBase-root MuiButton-root MuiButton-text '
                             'MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root '
                             'MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium '
                             ' css-13dw26a\']')
TASK_NAME_TEXTBOX = (By.XPATH, '(//input)[1]')
TASK_DESCRIPTION_TEXTBOX = (By.XPATH, '(//textarea)[1]')
TASK_CATEGORY_DROP_DOWN_LIST = (By.XPATH, '//div[@class=\'MuiInputBase-root MuiOutlinedInput-root'
                                          ' MuiInputBase-colorPrimary MuiInputBase-formControl css-9t65zx\']')
TASK_CATEGORY_BUTTON = (By.XPATH, '//ul[@class=\'MuiList-root MuiList-padding MuiMenu-list css-r8u8y9\']')
TASK_CATEGORY_OPTIONS = (By.XPATH, '//ul[@class=\'MuiList-root MuiList-padding MuiMenu-list css-r8u8y9\']/li')
CREATE_TASK_BUTTON = (By.ID, '//button[@class=\'MuiButtonBase-root MuiButton-root MuiButton-text'
                             ' MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root '
                             'MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium'
                             ' MuiButton-textSizeMedium css-vbgh04\']')
TASKS_ELEMENTS = (By.XPATH, '//div[@class=\'TaskContainer css-1vzn3uu\']')
TASK_EDIT_OPTION = (By.XPATH, '(//ul[@class=\'MuiList-root MuiList-padding MuiMenu-list css-r8u8y9\']//li)[7]')
TASK_DELETE_OPTION = (By.XPATH, '(//ul[@class=\'MuiList-root MuiList-padding MuiMenu-list css-r8u8y9\']//li)[9]')
SAVE_TASK_BUTTON = (By.XPATH, '(//button[@class=\'MuiButtonBase-root MuiButton-root MuiButton-text'
                              ' MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root '
                              'MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium'
                              ' MuiButton-textSizeMedium css-1yt8in3\'])[2]')
TASK_DESCRIPTION_EDIT_FIELD = (By.XPATH, '//textarea[1]')
DELETE_TASK_BUTTON = (By.XPATH, '//button[@class=\'MuiButtonBase-root'
                                ' MuiButton-root MuiButton-text MuiButton-textError'
                                ' MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root'
                                ' MuiButton-text MuiButton-textError MuiButton-sizeMedium '
                                'MuiButton-textSizeMedium css-1s4rms\']')
SEARCH_TASK = (By.XPATH, '//input[@class=\'MuiInputBase-input MuiOutlinedInput-input '
                         'MuiInputBase-inputAdornedStart css-zhq0ju\']')
ADD_TASK_TEXT = (By.XPATH, '(//li[@class=\'MuiButtonBase-root MuiMenuItem-root '
                           'MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-w1k5yy\'])[2]')


class TodoAppPage(BasePage):
    def __init__(self, driver: webdriver):
        """
        Initializes the TodoAppPage object with a WebDriver and the URL of the login page.
        :param driver: The WebDriver instance to interact with the browser.
        """
        super().__init__(driver)

    def create_task(self, task_name: str, task_description: str, category: str) -> None:
        """
        Creates a new task with the specified name, description, and category.
        :param task_name: The name of the task to be created.
        :param task_description: The description of the task to be created.
        :param category: The category of the task to be created.
        :return: None.
        """
        self.click(USER_SETTINGS_BUTTON)
        self.click(ADD_TASK_TEXT)
        self.enter_text(TASK_NAME_TEXTBOX, task_name)
        self.enter_text(TASK_DESCRIPTION_TEXTBOX, task_description)
        self.open_categories_drop_down_list()
        self.select_category(category=category)
        time.sleep(1)
        self.click_element_by_text(text='Create Task')
        time.sleep(3)

    def open_categories_drop_down_list(self) -> None:
        """
        Opens the drop-down list for task categories.
        :return: None.
        """
        self.click(TASK_CATEGORY_DROP_DOWN_LIST)

    def select_category(self, category: str) -> None:
        """
        Selects a category from the drop-down list.
        :param category: The category to be selected.
        :return: None.
        """
        categories = self.find_elements(
            by_locator=TASK_CATEGORY_OPTIONS,
            expected_conditions=ec.visibility_of_all_elements_located)
        for element in categories:
            if category in element.text:
                element.click()
                element.send_keys(Keys.ESCAPE)
                break

    def get_all_tasks(self) -> Optional[List[WebElement]]:
        """
        Retrieves all task elements on the page.
        :return: A list of WebElement representing the tasks, or an empty list if no tasks are found.
        """
        try:
            return self.find_elements(
                by_locator=TASKS_ELEMENTS,
                expected_conditions=ec.visibility_of_all_elements_located)
        except TimeoutException:
            return []

    def get_task_name(self, element: WebElement) -> str:
        """
        Retrieves the name of a task from the given task element.
        :param element: The WebElement representing the task.
        :return: The name of the task.
        """
        return element.find_element(By.XPATH, '..//h3[@class=\'css-18hlvm3\']').text

    def get_task_description(self, task_name: str) -> str:
        """
        Retrieves the description of a task given its name.
        :param task_name: The name of the task whose description is to be retrieved.
        :return: The description of the task.
        """
        try:
            tasks = self.get_all_tasks()
            for task in tasks:
                name = self.get_task_name(element=task)
                if name == task_name:
                    return task.find_element(By.XPATH, '..//p[@class=\'css-1sarz7y\']/div').text
        except TimeoutException:
            raise

    def is_task_exist(self, task_name: str) -> bool:
        """
        Checks if a task with the given name exists.
        :param task_name: The name of the task to check for existence.
        :return: True if the task exists, False otherwise.
        """
        try:
            tasks = self.get_all_tasks()
            for task in tasks:
                name = self.get_task_name(element=task)
                if name == task_name:
                    return True
            return False
        except TimeoutException:
            return False

    def open_task_options(self, task_name: str) -> None:
        """
        Opens the options menu for a task with the given name.
        :param task_name: The name of the task whose options menu is to be opened.
        :return: None.
        """
        try:
            tasks = self.get_all_tasks()
            for task in tasks:
                name = self.get_task_name(element=task)
                if name == task_name:
                    task.find_element(
                        By.XPATH,
                        '..//button[@class=\'MuiButtonBase-root MuiIconButton-root'
                        ' MuiIconButton-sizeMedium css-1rvh9qm\']').click()
        except TimeoutException:
            raise

    def edit_task_name(self, task_name: str) -> None:
        """
        Edits the name of a task.
        :param task_name: The new name for the task.
        :return: None.
        """
        self.open_edit_option()
        self.edit_description(task_name=task_name)
        time.sleep(5)

    def open_edit_option(self) -> None:
        """
        Opens the edit option for a task.
        :return: None.
        """
        self.click(TASK_EDIT_OPTION)

    def edit_description(self, task_name: str) -> None:
        """
        Edits the description of a task.
        :param task_name: The new description for the task.
        :return: None.
        """
        element = self.find_element(
            by_locator=TASK_DESCRIPTION_EDIT_FIELD,
            expected_conditions=ec.visibility_of_element_located)
        self.clear_field(element=element)
        time.sleep(2)
        self.enter_text(TASK_DESCRIPTION_EDIT_FIELD, task_name)
        self.click(SAVE_TASK_BUTTON)

    def clear_field(self, element: WebElement) -> None:
        """
        Clears the text in a given WebElement.
        :param element: The WebElement to be cleared.
        :return: None.
        """
        length = len(element.text)
        for i in range(length):
            element.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)

    def delete_task(self, task_name: str) -> None:
        """
        Deletes a task with the given name.
        :param task_name: The name of the task to be deleted.
        :return: None.
        """
        self.open_task_options(task_name=task_name)
        self.click(TASK_DELETE_OPTION)
        self.click(DELETE_TASK_BUTTON)

    def search_task(self, task_name: str) -> None:
        """
        Searches for a task with the given task name,
        :param task_name: The name of the task to be deleted.
        :return: None
        """
        self.enter_text(SEARCH_TASK, task_name)

    def get_number_of_tasks(self) -> int:
        """
        Read number of tasks exist.
        :return: Number of tasks.
        """
        return len(self.get_all_tasks())
