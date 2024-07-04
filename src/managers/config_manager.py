import yaml
import os

from src.utils.project import Project

FILE_NAME = 'config.yaml'


class ConfigManager:
    """
    Manages the configuration settings from a YAML file.
    """

    def __init__(self):
        """
        Initializes the ConfigManager by setting the path to the configuration file and loading its content.
        """
        self.config_file = os.path.join(Project.get_rootpath(), FILE_NAME)
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """
        Loads the configuration from the YAML file.
        :return: The loaded configuration data
        """
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_config_value(self, *keys, default=None):
        """
        Retrieves a configuration value based on the provided keys.
        :param keys: Sequence of keys to retrieve the configuration value
        :param default: Default value to return if the key is not found
        :return: The configuration value, or the default value if not found
        """
        value = self.config
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key, default)
            else:
                return default
        return value
