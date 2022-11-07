import pages.selectors as _
from selenium.webdriver import Keys
from base.base_class import SeleniumBase


class AuthPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def authorization_from_main_page(self):
        self.is_clickable('css', _.enter_button_selector, 'Кнопка "Войти"').click()
        self.is_clickable('css', _.mail_login_selector, 'Переключатель способа логина').click()
        self.is_clickable('css', _.login_input_selector, 'Поле ввода логина').send_keys('popotoro154', Keys.ENTER)
        self.is_clickable('css', _.password_input_selector, 'Поле ввода пароля').send_keys('ZXCasdQWE123_', Keys.ENTER)
