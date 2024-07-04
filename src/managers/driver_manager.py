import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class DriverManager:
    @staticmethod
    def init_driver(browser: str = 'chrome') -> webdriver:
        """
        Initializes and returns a WebDriver for the specified browser.
        :param browser: The browser type to initialize ('chrome', 'firefox', 'edge', 'brave').
        :return: A WebDriver object initialized with specific options.
        """
        if browser == 'chrome':
            return webdriver.Chrome(
                service=ChromeService(executable_path=DriverManager.get_executable_path('chrome')),
                options=DriverManager.get_chrome_options())
        elif browser == 'firefox':
            return webdriver.Firefox(
                service=FirefoxService(executable_path=DriverManager.get_executable_path('firefox')),
                options=DriverManager.get_firefox_options())
        elif browser == 'edge':
            return webdriver.Edge(
                service=EdgeService(executable_path=DriverManager.get_executable_path('edge')),
                options=DriverManager.get_edge_options())
        elif browser == 'brave':
            return webdriver.Chrome(
                service=ChromeService(executable_path=DriverManager.get_executable_path('brave')),
                options=DriverManager.get_brave_options())
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def get_chrome_options() -> ChromeOptions:
        """
        Creates and returns Chrome options for the WebDriver.
        :return: A ChromeOptions object configured with arguments to enhance usability.
        """
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        return chrome_options

    @staticmethod
    def get_firefox_options() -> FirefoxOptions:
        """
        Creates and returns Firefox options for the WebDriver.
        :return: A FirefoxOptions object configured with arguments to enhance usability.
        """
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        return firefox_options

    @staticmethod
    def get_edge_options() -> EdgeOptions:
        """
        Creates and returns Edge options for the WebDriver.
        :return: An EdgeOptions object configured with arguments to enhance usability.
        """
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        return edge_options

    @staticmethod
    def get_brave_options() -> ChromeOptions:
        """
        Creates and returns Brave options for the WebDriver.
        :return: A ChromeOptions object configured for Brave.
        """
        brave_options = ChromeOptions()
        brave_binary = DriverManager.find_brave_binary()
        if brave_binary:
            brave_options.binary_location = brave_binary
        else:
            raise FileNotFoundError("Brave browser executable not found. Please ensure Brave is installed.")

        brave_options.add_argument("--disable-blink-features=AutomationControlled")
        brave_options.add_argument("--disable-infobars")
        brave_options.add_argument("--start-maximized")
        brave_options.add_argument("--disable-extensions")
        return brave_options

    @staticmethod
    def find_brave_binary() -> str:
        """
        Attempts to find the Brave browser binary in common installation paths.
        :return: The file path of the Brave browser executable, or None if not found.
        """
        if platform.system() == "Windows":
            paths = [
                "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
                "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            ]
        elif platform.system() == "Darwin":
            paths = ["/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"]
        elif platform.system() == "Linux":
            paths = ["/usr/bin/brave-browser", "/usr/local/bin/brave-browser"]
        else:
            raise ValueError(f"Unsupported operating system: {platform.system()}")

        for path in paths:
            if os.path.exists(path):
                return path
        return None

    @staticmethod
    def get_executable_path(browser: str) -> str:
        """
        Retrieves the executable path for the specified WebDriver.
        :param browser: The browser type to get the executable path for ('chrome', 'firefox', 'edge', 'brave').
        :return: The file path of the WebDriver executable.
        """
        if browser in ['chrome', 'brave']:
            return ChromeDriverManager().install()
        elif browser == 'firefox':
            return GeckoDriverManager().install()
        elif browser == 'edge':
            return EdgeChromiumDriverManager().install()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
