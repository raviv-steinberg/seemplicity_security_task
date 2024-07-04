import pytest
from src.managers.config_manager import ConfigManager
from src.managers.driver_manager import DriverManager


def pytest_addoption(parser):
    """
    Adds a command-line option to pytest for specifying the browser type.
    """
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser type to use for tests: chrome, firefox, edge, brave"
    )


@pytest.fixture(scope='session')
def initiate_config():
    """
    Fixture to initialize the ConfigManager instance for session-wide configuration.
    :return: Instance of ConfigManager for accessing configuration settings.
    """
    yield ConfigManager()


@pytest.fixture(scope='function')
def initiate_driver(pytestconfig, initiate_config):
    """
    Fixture to initialize the WebDriver instance for each test function.
    :param pytestconfig: Pytest configuration object for accessing command-line options.
    :param initiate_config: Instance of ConfigManager for fetching configuration values.
    :return: WebDriver instance configured with browser URL from config.
    """
    browser = pytestconfig.getoption("browser")
    driver = DriverManager.init_driver(browser=browser)
    driver.get(initiate_config.get_config_value('settings', 'login', 'url', default=None))
    yield driver
    driver.quit()
