from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name = "detach", value = True)
chrome_driver = webdriver.Chrome(options = chrome_options)

#Opening LinkedIn on Chrome & Signing in
chrome_driver.get(url = "https://www.linkedin.com/jobs/search/?currentJobId=4092851967&distance=25&f_AL=true&f_E=1%2C2&f_WT=2&geoId=92000000&keywords=python%20intern&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R&spellCorrectionEnabled=true")
time.sleep(4)
continue_with_google = chrome_driver.find_element(By.XPATH, value = '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
continue_with_google.click()
email_or_phone = chrome_driver.find_element(By.XPATH, value = '//*[@id="base-sign-in-modal_session_key"]')
password = chrome_driver.find_element(By.XPATH, value = '//*[@id="base-sign-in-modal_session_password"]')
email_or_phone.send_keys("mubaris.hashimi2018@gmail.com")
password.send_keys(os.getenv("LINKEDIN_PASSWORD"))
sign_in = chrome_driver.find_element(By.XPATH, value = '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
sign_in.click()

time.sleep(10)  #Time to wait for security check-up to finish
ai_datascience = chrome_driver.find_element(By.XPATH, value = '//*[@id="ember53"]/span')
ai_datascience.click()
time.sleep(2)
next = chrome_driver.find_element(By.CSS_SELECTOR, value = 'button[aria-label = "Submit application"]')
next.click()

