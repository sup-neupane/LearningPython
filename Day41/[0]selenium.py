#Selenium allows to work with browsers and the drivers tells how to do so

from selenium import webdriver #type: ignore
from selenium.webdriver.common.by import By  #type:ignore

# Set the path to the ChromeDriver executable
chrome_driver_path = "chromedriver.exe"

# Create a Chrome driver instance
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(chrome_driver_path))

driver.get("https://www.daraz.com.np/products/pei-mei-natural-brightening-vitamin-c-serum-anti-acne-i174988559-s1196902943.html?scm=1007.51610.379274.0&pvid=ba6a4bdf-21d1-42f1-9551-c16fbb4db28d&search=flashsale&spm=a2a0e.tm80335409.FlashSale.d_174988559")

# price = driver.find_element(By.CSS_SELECTOR, ".notranslate.pdp-price.pdp-price_type_normal.pdp-price_color_orange.pdp-price_size_xl")
# print(price.text)



price = driver.find_element(By.XPATH, '//*[@id="module_product_price_1"]/div/div/span')
print(price.text)


#There are numerous ways to get hold of these elements like by id, x-path , class , name etc.





driver.close()   #This closes a tab
#driver.quit()  #This quits the browser


