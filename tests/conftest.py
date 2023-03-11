import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


# @pytest.fixture
# def get_chrome_options():
#     options = chrome_options()
#     options.add_argument('--window-size=1920,1080')
#     options.add_argument('chrome')  # "--headless"
#     driver = webdriver.Chrome(options=options)
#     url = 'https://ya.ru/'


# @pytest.fixture
# def get_webdriver(get_chrome_options):
#     options = get_chrome_options
#     driver = webdriver.Chrome(options=options)
#     return driver


@pytest.fixture(scope='function')
def setup(request):
    options = chrome_options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('chrome')  # "--headless"
    driver = webdriver.Chrome(options=options, executable_path='/home/spacebroth/Projects/Test_UI/chromedriver')
    url = 'https://ya.ru/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
