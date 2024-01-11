#Registration_login: регистрация аккаунта
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# my_account=driver.find_element_by_link_text('My Account').click()
# reg_email=driver.find_element_by_id('reg_email')
# reg_email.send_keys('jeka21.02.81@mail.ru')
# reg_password=driver.find_element_by_id('reg_password')
# reg_password.send_keys('12345ZqxwcE')
# btn_register=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='register']")))
# btn_register.click()
# driver.quit()

#Registration_login: логин в систему

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
my_account=driver.find_element_by_link_text('My Account').click()
log_name=driver.find_element_by_id('username')
log_name.send_keys('jeka21.02.81@mail.ru')
log_password=driver.find_element_by_id('password')
log_password.send_keys('12345ZqxwcE')
login=driver.find_element_by_css_selector("[name='login']").click()
logout=WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.LINK_TEXT, 'Logout'),'Logout')) ########хз может until_not и invisibility_of_element_located
driver.quit()


