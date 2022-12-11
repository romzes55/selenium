import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def login():
   pytest.driver = webdriver.Chrome(executable_path='C:/Users/user/Desktop/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('rter@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
   yield
   pytest.driver.quit()