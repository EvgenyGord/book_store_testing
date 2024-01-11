#Shop: отображение страницы товара

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# my_account=driver.find_element_by_link_text('My Account').click()
# log_name=driver.find_element_by_id('username')
# log_name.send_keys('jeka21.02.81@mail.ru')
# log_password=driver.find_element_by_id('password')
# log_password.send_keys('12345ZqxwcE')
# login=driver.find_element_by_css_selector("[name='login']").click()
# shop=driver.find_element_by_link_text('Shop').click()
# book=driver.find_element_by_css_selector('.post-181>a').click()
# proverka=WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.summary.entry-summary'), 'HTML5 Forms'))
# driver.quit()




#Shop: количество товаров в категории
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# my_account=driver.find_element_by_link_text('My Account').click()
# log_name=driver.find_element_by_id('username')
# log_name.send_keys('jeka21.02.81@mail.ru')
# log_password=driver.find_element_by_id('password')
# log_password.send_keys('12345ZqxwcE')
# login=driver.find_element_by_css_selector("[name='login']").click()
# shop=driver.find_element_by_link_text('Shop').click()
# html=driver.find_element_by_link_text('HTML').click()
# test_count=driver.find_elements_by_css_selector('.products.masonry-done>li')
# assert len(test_count)==3
# driver.quit()




#Shop: сортировка товаров

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# my_account=driver.find_element_by_link_text('My Account').click()
# log_name=driver.find_element_by_id('username')
# log_name.send_keys('jeka21.02.81@mail.ru')
# log_password=driver.find_element_by_id('password')
# log_password.send_keys('12345ZqxwcE')
# login=driver.find_element_by_css_selector("[name='login']").click()
# shop=driver.find_element_by_link_text('Shop').click()
#
# selector_val=driver.find_element_by_css_selector('.orderby>[selected="selected"]')
# proverka_po_value=selector_val.get_attribute('value')
# assert proverka_po_value=='menu_order'
#
# element=driver.find_element_by_css_selector('.orderby')
# select=Select(element)
# select.select_by_value('price-desc')
#
# selector_value=driver.find_element_by_css_selector('.orderby>[selected="selected"]')
# proverka=selector_value.get_attribute('value')
# assert proverka=='price-desc'
#
# driver.quit()



#Shop: отображение, скидка товара

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# my_account=driver.find_element_by_link_text('My Account').click()
# log_name=driver.find_element_by_id('username')
# log_name.send_keys('jeka21.02.81@mail.ru')
# log_password=driver.find_element_by_id('password')
# log_password.send_keys('12345ZqxwcE')
# login=driver.find_element_by_css_selector("[name='login']").click()
# shop=driver.find_element_by_link_text('Shop').click()
#
# book_android=driver.find_element_by_css_selector('.post-169>a').click()
#
# old_cost=driver.find_element_by_css_selector('del>.woocommerce-Price-amount.amount')
# assert old_cost.text=="₹600.00"
#
# new_cost=driver.find_element_by_css_selector('ins>.woocommerce-Price-amount.amount')
# assert new_cost.text=="₹450.00"
#
# cover_book=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.woocommerce-main-image.zoom')))
# cover_book.click()
#
# cover_book_after=WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'ppt'), 'Android Quick Start Guide'))
#
# close=driver.find_element_by_class_name('pp_close').click()
#
# driver.quit()




#Shop: проверка цены в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# shop=driver.find_element_by_link_text('Shop').click()
# add_book=driver.find_element_by_css_selector('.post-182>.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
# time.sleep(20)
# proverka_item=driver.find_element_by_css_selector('.cartcontents')
# assert proverka_item.text == "1 Item"
# proverka_cost=driver.find_element_by_css_selector('.wpmenucart-contents>.amount')
# assert proverka_cost.text == "₹180.00"
# korzina=driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
# korzina.click()
# subtotal=WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal .woocommerce-Price-amount.amount'), '₹180.00'))
# total=WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'order-total'), '₹183.60'))
# driver.quit()


#Shop: работа в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get('https://practice.automationtesting.in/')
# shop=driver.find_element_by_link_text('Shop').click()
# driver.execute_script("window.scrollBy(0,300);")
# time.sleep(5)
# add_book_1=driver.find_element_by_css_selector('.post-182>.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
# time.sleep(5)
# add_book_2=driver.find_element_by_css_selector('.post-180>.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
# time.sleep(5)
# korzina=driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
# time.sleep(5)
# korzina.click()
# time.sleep(5)
# remove_1=driver.find_element_by_css_selector('.cart_item:nth-child(1)>.product-remove>.remove').click()
# undo=driver.find_element_by_link_text('Undo?').click()
# count_tov_js=driver.find_element_by_css_selector('.cart_item:nth-child(1)>.product-quantity>.quantity>.input-text.qty.text')
# count_tov_js.clear()
# count_tov_js.send_keys('3')
# update_btn=driver.find_element_by_css_selector('.actions>.button').click()
# proverka=count_tov_js.get_attribute('value')
# assert proverka=='3'
# time.sleep(5)
# apply_coupon=driver.find_element_by_css_selector("[value='Apply Coupon']")
# time.sleep(5)
# apply_coupon.click()
# test_message=WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CLASS_NAME,'woocommerce-error'), "Please enter a coupon code."))
# driver.quit()



#Shop: покупка товара

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in/')
shop=driver.find_element_by_link_text('Shop').click()
driver.execute_script("window.scrollBy(0,300);")
time.sleep(5)
add_book_1=driver.find_element_by_css_selector('.post-182>.button.product_type_simple.add_to_cart_button.ajax_add_to_cart').click()
time.sleep(5)
korzina=driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
time.sleep(5)
korzina.click()
proceed_to_checkout=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button.button.alt.wc-forward')))
proceed_to_checkout.click()
first_name=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'billing_first_name')))
first_name.click()
first_name.send_keys('Ivan')
last_name=driver.find_element_by_css_selector('#billing_last_name').send_keys('Ivanov')
email=driver.find_element_by_id('billing_email').send_keys('xxx@mail.ru')
phone=driver.find_element_by_id('billing_phone').send_keys('+79531187955')
country=driver.find_element_by_id('s2id_billing_country').click()
country_vvod=driver.find_element_by_id('s2id_autogen1_search')
country_vvod.click()
country_vvod.send_keys('Russia')
variant=driver.find_element_by_css_selector('.select2-results-dept-0.select2-result.select2-result-selectable').click()
address=driver.find_element_by_css_selector('.input-text#billing_address_1')
address.click()
address.send_keys('Krasnaya 135')
town=driver.find_element_by_css_selector('.input-text#billing_city')
town.click()
town.send_keys('Krasnodar')
state=driver.find_element_by_css_selector('.input-text#billing_state')
state.click()
state.send_keys('Russia')
postcode=driver.find_element_by_css_selector('.input-text#billing_postcode')
postcode.click()
postcode.send_keys('300200')
check_payments=driver.find_element_by_id('payment_method_cheque').click()
placeholder=driver.find_element_by_id('place_order').click()
thank_you=WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
payment_method=WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.shop_table.order_details>tfoot>tr:nth-child(3)'), "Check Payments"))
driver.quit()

























