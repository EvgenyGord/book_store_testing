#Home: добавление комментария

from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
scroll_600=driver.execute_script("window.scrollBy(0,600);")
selenium_ruby=driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 h3").click()
reviews=driver.find_element_by_css_selector('.reviews_tab>a').click()
star_5=driver.find_element_by_link_text('5').click()
place_review=driver.find_element_by_id('comment')
place_review.send_keys('Nice book!')
name=driver.find_element_by_id('author')
name.send_keys('Evgeny')
email=driver.find_element_by_id('email')
email.send_keys('jeka21.02.81@mail.ru')
submit=driver.find_element_by_class_name('submit').click()
driver.quit()