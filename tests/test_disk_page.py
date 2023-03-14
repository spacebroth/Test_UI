import time
import pytest
from pages.auth_page import AuthPage
from pages.disk_page import DiskPage
from pages.main_ya_page import MainYaPage


@pytest.mark.usefixtures('setup')
class TestDiskPage:

    @pytest.mark.parametrize('folder_name', ['AutoFolder',
                                             'AutoFolder2Looooooooooooooooooooooooooooooooooooooooooooooooooooooooong'])
    def test_create_folder_and_copy_file(self, folder_name):
        page = DiskPage(self.driver)
        main_page = MainYaPage(self.driver)
        auth_page = AuthPage(self.driver)
        auth_page.authorization_from_main_page()
        main_page.go_to_disk()
        page.create_new_item_with_name_('Папку', folder_name)
        page.copy_or_move_item('Копировать', folder_name)
        page.go_to_root()
        page.go_to_folder_in_root(folder_name)
        assert 'Файл для копирования.docx' in page.get_elements_in_current_folder()
        page.delete_folder_in_root(folder_name)
        page.sign_out()
        time.sleep(2)  # Просто визуально убедиться, что разлогинились
