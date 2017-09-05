from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys

class YandexSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        driver.get('http://yandex.ru')
        driver.set_page_load_timeout(10)
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)

        # ждём пока элемент с ID  'text' появится в DOM и отправляем в него 'Тензор'
        try:
            input = wait.until(EC.presence_of_element_located((By.ID, 'text')))
        finally:
            input.send_keys('Тензор')

        # ждём пока элемент с классом 'suggest2' станет видимым и нажимаем Enter
        try:
            wait.until(EC.visibility_of(driver.find_element_by_class_name('suggest2')))
        finally:
            input.send_keys(Keys.ENTER)

        # ищем пока не появится элемент 'a' по  CSS селектору и определяем "первую ссылку"
        firstlink = driver.find_element_by_css_selector('li.serp-item a')
        print(firstlink.get_attribute('href'))

        # так же можно проверить налчие в первом элементе ссылки на наш сайт
        # но обычно первая ссылка рекламная и тест выдаст ошибку в таком случае:
        # assert "https://tensor.ru/" in firstlink.get_attribute('href')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()