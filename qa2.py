from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class YandexPictSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        driver.get('http://yandex.ru')
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        pictlink = driver.find_element_by_link_text('Картинки')
        pictlink.click()
        assert 'https://yandex.ru/images/' in driver.current_url
        arrowback = driver.find_element_by_css_selector('.b-501px-slider__arrow_dir_prev')
        try:
            wait.until(EC.visibility_of(arrowback))
        finally:
            arrowback.click()
        arrownext = driver.find_element_by_class_name('b-501px-slider__arrow_dir_next')
        ActionChains(driver).move_to_element(arrownext).click(arrownext).perform()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()