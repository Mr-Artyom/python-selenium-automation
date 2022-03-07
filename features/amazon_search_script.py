from selenium import  webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome('C:/Users/pandw/OneDrive/Desktop/Coding/Careerist/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get("https://www.amazon.com")
# send text to search bar
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
# send query
driver.find_element(By.ID, 'nav-search-submit-button').click()

#test case
expected_result = '"coffee"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(actual_result)

assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"
print("Test case passed")
driver.quit()

