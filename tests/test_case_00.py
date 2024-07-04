import random
import pytest
from src.managers.config_manager import ConfigManager
from src.pages.todo_app_page import TodoAppPage
from src.utils.utils import Utils

conf = ConfigManager()


class TestTodoApp:
    @pytest.mark.create_a_task
    def test_create_a_task(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)
        todo_app.create_task(
            task_name=task_name,
            task_description=Utils.generate_random_string(length=20),
            category='Personal')

        assert todo_app.is_task_exist(task_name=task_name), 'Failed to verify task created'

    @pytest.mark.edit_task
    def test_edit_task(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)
        todo_app.create_task(
            task_name=task_name,
            task_description=Utils.generate_random_string(length=20),
            category='Personal')

        todo_app.open_task_options(task_name=task_name)

        new_task_description = Utils.generate_random_string(length=10)
        todo_app.edit_task_name(task_name=new_task_description)
        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

        assert todo_app.get_task_description(
            task_name=task_name) == new_task_description, 'Failed to verify task description'

    @pytest.mark.delete_task
    def test_delete_task(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)
        todo_app.create_task(
            task_name=task_name,
            task_description=Utils.generate_random_string(length=20),
            category='Work')

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

        todo_app.delete_task(task_name=task_name)
        assert not todo_app.is_task_exist(task_name=task_name)

    @pytest.mark.search_task
    def test_search_task(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)
        todo_app.create_task(
            task_name=task_name,
            task_description=Utils.generate_random_string(length=20),
            category='Work')

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

        todo_app.search_task(task_name=task_name)

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

    @pytest.mark.same_task_name_twice
    def test_same_task_name_twice(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)

        todo_app.create_task(
            task_name=task_name,
            task_description=Utils.generate_random_string(length=20),
            category='Home')

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

        todo_app.create_task(
            task_name=task_name,
            task_description=Utils.generate_random_string(length=20),
            category='Home')

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

        todo_app.search_task(task_name=task_name)
        assert todo_app.get_number_of_tasks() == 2, 'Failed to find 2 tasks with same name'

    @pytest.mark.multiple_tasts_creation
    def test_add_randon_number_of_tasks(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)

        number = random.randint(20, 50)
        for i in range(number + 1):
            todo_app.create_task(
                task_name=task_name,
                task_description=Utils.generate_random_string(length=20),
                category='Home')
        actual_tasks = todo_app.get_number_of_tasks()
        assert actual_tasks == number + 1, f'Validation mismatch, Expected {number + 1} tasks, Found {actual_tasks}'
