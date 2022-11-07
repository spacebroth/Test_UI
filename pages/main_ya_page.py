import pages.selectors as _
from base.base_class import SeleniumBase


class MainYaPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def go_to_disk(self):
        self.is_clickable('css', _.user_header_button_selector).click()
        self.get_link_by_name('Диск', _.user_menu_links_selector).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
