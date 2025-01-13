from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_setting = webdriver.ChromeOptions()
chrome_setting.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options = chrome_setting)


chrome_driver.get(url = "http://orteil.dashnet.org/experiments/cookie/")


slicker_button = chrome_driver.find_element(By.ID, value = "cookie")
slicker_button.click()