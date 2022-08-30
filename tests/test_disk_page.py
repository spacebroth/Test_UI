import time
import pytest
from pages.disk_page import DiskPage


@pytest.mark.usefixtures('setup')
class TestDiskPage:

    @pytest.mark.parametrize('folder_name', ['АвтоПапка',
                                             'АвтоПапка2Лооооооооооооооооооооооооооооооооооооооооооооооооооооооооонг'])
    def test_create_folder_and_copy_file(self, folder_name):
        page = DiskPage(self.driver)
        page.authorization_from_main_page()
        page.go_to_disk()
        page.create_new_item_with_name_('Папку', folder_name)
        page.copy_or_move_item('Копировать', folder_name)
        page.go_to_root()
        page.go_to_folder_in_root(folder_name)
        assert 'Файл для копирования.docx' in page.get_elements_in_current_folder()
        page.delete_folder_in_root(folder_name)
        page.sign_out()
        time.sleep(2)  # Просто визуально убедиться, что разлогинились
