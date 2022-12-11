import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#считаем количество питомцев
def test_quantity_of_pets(login):
   descriptions = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   assert len(descriptions) == 5

#проверяем на отсутсвие незаполненных полей "Порода"
def test_breed(login):
   pytest.driver.implicitly_wait(10)#используем неявное ожидание
   breed  = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
   breed_list=[]
   for i in range(len(breed)):
      breed_list.append(breed[i].text)# делаем список из пород
   assert breed_list.count('') == 0 # если в списке есть пустое поле, то тест упадет

#проверяем на отсутсвие незаполненных полей "Имя"
def test_name(login):
   pytest.driver.implicitly_wait(10)
   name  = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
   name_list=[]
   for i in range(len(name)):
      name_list.append(name[i].text)# делаем список из имен
   assert name_list.count('') == 0 # если в списке есть пустое поле, то тест упадет

#проверяем на отсутсвие незаполненных полей "Возраст"
def test_age(login):
   pytest.driver.implicitly_wait(10)
   age  = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')
   for i in range(len(age)):
      age.append(age[i].text)# делаем список из возраста
   assert age.count('') == 0 # если в списке есть пустое поле, то тест упадет

def test_table_wait(login):
   WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, "all_my_pets"))
   )
