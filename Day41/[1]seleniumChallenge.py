#Selenium allows to work with browsers and the drivers tells how to do so

from selenium import webdriver #type: ignore
from selenium.webdriver.common.by import By  #type:ignore
from selenium.webdriver.support.ui import WebDriverWait  #type:ignore
from selenium.webdriver.support import expected_conditions as EC #type:ignore
from selenium.webdriver.common.keys import Keys  #type:ignore
import time 

# Set the path to the ChromeDriver executable
chrome_driver_path = "chromedriver.exe"

# Create a Chrome driver instance
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(chrome_driver_path))

driver.get("https://en.wikipedia.org/wiki/Main_Page")



# number = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/ul/li[1]/a')
# number.click()    #Click on this tag


# link = driver.find_element(By.LINK_TEXT, "English")   #Find element by link text
# link.click()

# Wait for the input field to be clickable
search_bar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "search"))
)
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)  #Press enter key


# Pause the script for 5 seconds
time.sleep(10)



driver.close() 
