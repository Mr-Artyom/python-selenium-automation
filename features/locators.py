from selenium import webdriver
from selenium.webdriver.common.by import By
# init driver
driver = webdriver.Chrome('C:/Users/pandw/OneDrive/Desktop/Coding/Careerist/python-selenium-automation/chromedriver')
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fsign%2Fs%3Fk%3Dsign%2Bin%26ref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# by XPATH
driver.find_element(By.XPATH, "//a[@href='/ref=ap_frn_logo']")
# using only tag
driver.find_element(By.XPATH, "//a")
# using only attribute
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo")

