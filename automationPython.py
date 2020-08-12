from selenium import webdriver

driver = webdriver.Safari()
driver.maximize_window()
driver.get('https://www.google.com')

searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys('Hello, this is automated testing with Selenium')

searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchButton.click()

driver.close()

