
import time
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)


##1
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver.find_element('xpath','//a[contains(text(),"Books")]').click()
# time.sleep(2)
# driver.find_element('xpath','(//input[@value="Add to cart"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath','(//span[@class="cart-label"])[1]').click()
# time.sleep(2)


# #2
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver.find_element('xpath', "//a[contains(text(),'Electronics')]").click()
# time.sleep(1)
# driver.find_element('xpath', "(//a[contains(text(),'Cell phones')])[4]").click()

# #3
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.find_element('xpath', "//button[text()='Start']").click()
# wait = WebDriverWait(driver, 10)
# hello_text = wait.until(
#     EC.visibility_of_element_located(('xpath', "//h4[text()='Hello World!']"))
# )

##4
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# wait = WebDriverWait(driver, 10)
# time.sleep(2)
# remove_btn = wait.until(
#     EC.element_to_be_clickable(('xpath', "//button[text()='Remove']"))
# )
# remove_btn.click()
# add_btn = wait.until(
#     EC.element_to_be_clickable(('xpath', "//button[text()='Add']"))
# )
# add_btn.click()

##5
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver.get("https://demoqa.com/select-menu")
# driver.maximize_window()
# wait = WebDriverWait(driver,10)
# dropdown = wait.until(EC.element_to_be_clickable(("id","withOptGroup")))
# dropdown.click()
# option = wait.until(EC.element_to_be_clickable(("xpath","//div[text()='Group 2, option 1']")))
# option.click()
# selected_value = driver.find_element("xpath","//div[contains(@class,'singleValue')]").text
# print("Selected Value:", selected_value)
# if selected_value == "Group 2, option 1":
#     print("Verification Passed")
# else:
#     print("Verification Failed")


##6
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# ac = ActionChains(driver)
# driver.get("https://demoqa.com/select-menu")
# time.sleep(2)
# element = driver.find_element("xpath","//select[@id='cars']")
# ac.scroll_to_element(element).perform()
# time.sleep(2)
# select = Select(element)
# select.select_by_visible_text("Volvo")
# select.select_by_visible_text("Saab")
# select.select_by_visible_text("Opel")
# options = select.all_selected_options
# for i in options:
#     print(i.text)


##7
# from selenium.webdriver.common.action_chains import ActionChains
# driver.get("https://demoqa.com/menu/")
# time.sleep(1)
# actions = ActionChains(driver)
# main_item2 = driver.find_element('xpath', "//a[text()='Main Item 2']")
# actions.move_to_element(main_item2).perform()
# sub_sub_list = driver.find_element('xpath', "//a[text()='SUB SUB LIST »']")
# actions.move_to_element(sub_sub_list).perform()
# sub_sub_item1 = driver.find_element('xpath', "//a[text()='Sub Sub Item 1']").click()

##8
# from selenium.webdriver.common.action_chains import ActionChains
# driver.implicitly_wait(10)
# driver.get("https://demoqa.com/droppable")
# drag_element = driver.find_element('id', "draggable")
# drop_element = driver.find_element('id', "droppable")
# actions = ActionChains(driver)
# actions.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
# result = driver.find_element('id', "droppable").text
# print(result)

##9
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element('xpath', "//button[text()='Click for JS Confirm']").click()
# time.sleep(1)
# alert = driver.switch_to.alert
# alert.accept()
# result = driver.find_element('id', "result").text
# print(result)

##10
# driver.get("https://the-internet.herokuapp.com/upload")
# path = r'C:\Users\KIIT\PycharmProjects\selenium_training\files\Book1 (1).xlsx'
# time.sleep(5)
# driver.find_element('id', "file-upload").send_keys(path)
# time.sleep(2)
# driver.find_element('id', "file-submit").click()
