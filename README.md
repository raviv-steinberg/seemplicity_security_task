
# Seemplicity Security Task

This project is designed to automate testing for ESH Login page focusing on login functionality using Selenium and API testing with pytest.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/raviv-steinberg/seemplicity_security_task.git
    cd seemplicity_security_task
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Ensure that `config.yaml` is properly configured with the necessary settings. Example configuration:

```yaml
settings:
  login:
    url: 'https://react-cool-todo-app.netlify.app/'
  ```

## Running Tests with Different Browsers

To run the tests with different browsers, you can use the `--browser` command-line option with pytest. The supported browsers are chrome, firefox, edge, and brave.

#### Chrome (default):

 ```bash
 pytest
 ```

#### Firefox:

 ```bash
 pytest --browser=firefox
 ```

#### Edge:

 ```bash
 pytest --browser=edge
 ```

#### Brave:

 ```bash
 pytest --browser=brave
 ```

## Running Specific Tests

Using pytest tags
To run tests with a specific tag (`e.g., create_a_task\edit_task\delete_task\search_task`):

```bash
 pytest -m create_a_task
 ```

## Python Version

- **Python Version**: 3.12.

## Configuration Management and WebDriver Initialization

`ConfigManager`

The ConfigManager class handles the loading and retrieval of configuration settings from a YAML file.

- : Sets the path to the config.yaml file and loads its content.
- Loading Configuration: The _load_config method reads the YAML file and returns its content as a dictionary.
- Retrieving Configuration Values: The get_config_value method allows fetching values from the loaded configuration using a sequence of keys, with an optional default value if the keys are not found.

## DriverManager
`The DriverManager class manages the initialization of WebDriver instances for different browsers.`

- Initialization: The init_driver method initializes and returns a WebDriver for the specified browser (chrome, firefox, edge, brave).
- Browser Options: Methods like get_chrome_options, get_firefox_options, get_edge_options, and get_brave_options configure and return browser-specific options to enhance usability.
- Brave Browser Binary: The find_brave_binary method locates the Brave browser executable in common installation paths.
- WebDriver Executable Path: The get_executable_path method retrieves the executable path for the specified WebDriver using webdriver_manager.

## Pytest Configuration
Command-line Option: The pytest_addoption function adds a command-line option to specify the browser type for running tests.
Fixtures: The initiate_config and initiate_driver fixtures initialize the ConfigManager and WebDriver instances, respectively. The initiate_driver fixture also navigates to the login URL specified in the configuration.


## Test Cases Explanation
`test_create_a_task`

This test verifies the creation of a new task in the Todo application.

1. Generate a Random Task Name: A random string of 10 characters is generated to be used as the task name.
2. Initialize TodoAppPage: An instance of TodoAppPage is created using the provided initiate_driver.
3. Create Task: A task is created with the generated task name and categorized under 'Personal'.
4. Verify Task Creation: The test asserts that the task exists in the application by checking its presence with the task name.

`test_edit_task`

This test checks the functionality of editing an existing task's name and verifying the update.

1. Generate a Random Task Name: A random string of 10 characters is generated to be used as the task name.
2. Initialize TodoAppPage: An instance of TodoAppPage is created using the provided initiate_driver.
3. Create Task: A task is created with the generated task name and categorized under 'Personal'.
4. Open Task Options: The options for the created task are opened.
5. Edit Task Description: A new random string is generated for the task description, and the task description is updated.
6. Verify Task Name: The test asserts that the task still exists with the original task name.
7. Verify Task Description: The test asserts that the task's description has been updated to the new value.

`test_delete_task`

This test ensures that a task can be deleted successfully from the Todo application.

1. Generate a Random Task Name: A random string of 10 characters is generated to be used as the task name.
2. Initialize TodoAppPage: An instance of TodoAppPage is created using the provided initiate_driver.
3. Create Task: A task is created with the generated task name and categorized under 'Work'.
4. Verify Task Creation: The test asserts that the task exists in the application by checking its presence with the task name.
5. Delete Task: The created task is deleted.
6. Verify Task Deletion: The test asserts that the task no longer exists in the application.

`test_search_task`

This test validates the search functionality by creating a task and then searching for it.

1. Generate a Random Task Name: A random string of 10 characters is generated to be used as the task name.
2. Initialize TodoAppPage: An instance of TodoAppPage is created using the provided initiate_driver.
3. Create Task: A task is created with the generated task name and categorized under 'Work'.
4. Verify Task Creation: The test asserts that the task exists in the application by checking its presence with the task name.
5. Search Task: The task is searched for using its name.
6. Verify Task Search: The test asserts that the task exists and can be found through the search functionality.

Make sure the corresponding WebDriver executables and browsers are installed on your system. The webdriver_manager will automatically handle the download and installation of WebDriver executables.

`test_add_same_task_name_twice`

This test ensures that the application can handle the creation of multiple tasks with the same name and that the search functionality works correctly in this scenario.

1. Generate a Random Task Name: A random string of 10 characters is generated to be used as the task name.
2. Initialize TodoAppPage: An instance of TodoAppPage is created using the provided initiate_driver.
3. Create Task (First Instance): A task is created with the generated task name and categorized under 'Home'.
4. Verify Task Creation (First Instance): The test asserts that the first instance of the task exists in the application by checking its presence with the task name.
5. Create Task (Second Instance): Another task with the same name, description, and category is created.
6. Verify Task Creation (Second Instance): The test asserts that the second instance of the task also exists in the application by checking its presence with the task name.
7. Search Task: The task is searched for using its name.
8. Verify Number of Tasks: The test asserts that two tasks with the same name are found, verifying that the application can handle multiple tasks with identical names and that the search functionality correctly identifies both instances.