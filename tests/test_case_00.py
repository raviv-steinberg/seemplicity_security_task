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
        todo_app.create_task(task_name=task_name, task_description='bla bla', category='Personal')
        assert todo_app.is_task_exist(task_name=task_name), 'Failed to verify task created'

    @pytest.mark.edit_task
    def test_edit_task(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)
        todo_app.create_task(task_name=task_name, task_description='bla bla', category='Personal')
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
        todo_app.create_task(task_name=task_name, task_description='bla bla', category='Personal')

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

        todo_app.delete_task(task_name=task_name)
        assert not todo_app.is_task_exist(task_name=task_name)

    @pytest.mark.search_task
    def test_search_task(self, initiate_driver):
        task_name = Utils.generate_random_string(length=10)
        todo_app = TodoAppPage(driver=initiate_driver)
        todo_app.create_task(task_name=task_name, task_description='bla bla', category='Personal')

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'

        todo_app.search_task(task_name=task_name)

        assert todo_app.is_task_exist(
            task_name=task_name), 'Failed to verify task created'
