from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import List


def get_element_by_text_from_list(elements: List[WebElement], name: str) -> WebElement:
    name = name.lower()
    return [element for element in elements if element.text.lower() == name][0]


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 10)

    """Методы для поиска элементов на странице"""

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'name': By.NAME,
                    'class': By.CLASS_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(EC.element_to_be_clickable((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(EC.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    """Методы для работы со списками элементов"""

    def get_webelements_list(self, selector: str) -> List[WebElement]:
        webelements = self.are_present('css', selector, 'Список веб-элементов')
        return webelements

    def get_link_by_name(self, name: str, selector: str) -> WebElement:
        elements = self.get_webelements_list(selector)
        element = get_element_by_text_from_list(elements, name)
        return element

    def get_text_webelements_list(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]
