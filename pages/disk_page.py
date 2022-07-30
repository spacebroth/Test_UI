import pages.selectors as _
from selenium.webdriver import Keys
from typing import List
from base.base_class import SeleniumBase
from selenium.webdriver import ActionChains


class DiskPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Понимаю, что иногда появляется подтверждение телефона, как его обойти точно не знаю. Было две мысли:
    # 1. Использовать определенные куки другой сессии и загрузить их в текущую
    # 2. Как-то замокать, сделать "заглушку" этого запроса
    def authorization_from_main_page(self):
        self.is_clickable('css', _.enter_button_selector, 'Кнопка "Войти"').click()
        self.is_clickable('css', _.mail_login_selector, 'Переключатель способа логина').click()
        self.is_clickable('css', _.login_input_selector, 'Поле ввода логина').send_keys('popotoro154', Keys.ENTER)
        self.is_clickable('css', _.password_input_selector, 'Поле ввода пароля').send_keys('ZXCasdQWE123_', Keys.ENTER)

    def go_to_disk(self):
        self.is_clickable('css', _.disk_button_in_card_menu_selector, 'Ссылка "Диск"').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def create_new_item_with_name_(self, item: str, item_name: str):
        self.is_clickable('css', _.create_button_selector, 'Кнопка "Создать"').click()
        self.get_link_by_name(item, _.creatable_items_selector).click()
        modal_input = self.is_clickable('css', _.create_item_input_selector, 'Поле ввода имени создаваемой сущности')
        modal_input.send_keys(item_name, Keys.ENTER)

    def copy_or_move_item(self, action: str, where: str):
        actions = ActionChains(self.driver)
        actions.double_click(self.get_link_by_name('Общая папка', _.listing_items_selector)).perform()
        actions.context_click(self.get_link_by_name('Файл для копирования.docx', _.listing_items_selector)).perform()
        self.get_link_by_name(action, _.context_menu_selector).click()
        self.get_link_by_name(where, _.modal_elements_selector).click()
        self.is_clickable('css', _.confirm_modal_button_selector).click()

    def go_to_folder_in_root(self, name_folder):
        actions = ActionChains(self.driver)
        actions.double_click(self.get_link_by_name(name_folder, _.listing_items_selector)).perform()

    def go_to_root(self):
        self.is_clickable('css', _.disk_root_page_selector).click()

    def delete_folder_in_root(self, folder_name):
        actions = ActionChains(self.driver)
        self.go_to_root()
        actions.context_click(self.get_link_by_name(folder_name, _.listing_items_selector)).perform()
        self.get_link_by_name('Удалить', _.context_menu_selector).click()

    def get_elements_in_current_folder(self) -> List[str]:
        element = self.get_text_webelements_list(self.get_webelements_list(_.listing_items_selector))
        return element

    def sign_out(self):
        self.is_clickable('css', _.user_header_button_selector, 'Кнопка аватар юзера').click()
        self.get_link_by_name('Выйти', _.user_menu_links_selector).click()
        self.driver.switch_to.alert.accept()
