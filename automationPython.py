from selenium import webdriver

driver = webdriver.Safari()
driver.maximize_window()
driver.get('https://www.google.com')
actualTitle = str(driver.title)
expectedTitle = "google"

searchBox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys('Hello, this is automated testing with Selenium')

searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchButton.click()

if actualTitle.lower() == expectedTitle.lower():
    print("Automation Test Successful")
else:
    print("Automation Test Failure","\n","Actual title:",actualTitle,"\n","Expected title:",expectedTitle)

driver.close()

