from selenium import webdriver #type: ignore
from selenium.webdriver.common.by import By  #type:ignore
from selenium.webdriver.common.keys import Keys  #type:ignore
from time import sleep
from dotenv import load_dotenv # type: ignore
import os
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException # type: ignore



load_dotenv()  

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


# Set the path to the ChromeDriver executable
chrome_driver_path = "chromedriver.exe"

# Create a Chrome driver instance
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(chrome_driver_path))
driver.get("http://www.tinder.com")

sleep(2)
log = driver.find_element(By.XPATH, '//*[@id="q2098069830"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log.click()




sleep(2)
log_in_with_facebook = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
log_in_with_facebook.click()


sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(2)
email = driver.find_element(By.NAME, 'email')
password = driver.find_element(By.NAME, 'pass')
email.send_keys(MY_EMAIL)
password.send_keys(MY_PASSWORD)
password.send_keys(Keys.ENTER)

continue_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span'))
)
continue_button.click()

driver.switch_to.window(base_window)


#Delay by 5 seconds to allow page to load.
sleep(5)

# Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')
cookies.click()


sleep(5)
allow_location = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location.click()

# Disallow notifications
sleep(5)
notifications_button = driver.find_element(By.XPATH, '//*[@id="q369688754"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]/div')
notifications_button.click()

for n in range(100):
    # Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        # Wait for the like button to be clickable
        like_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button/span/span[1]'))
        )
        like_button.click()

    except ElementClickInterceptedException:
        try:
            # Handle the "It's a Match" popup by clicking the close button or continue button
            match_popup = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".itsAMatch a"))
            )
            match_popup.click()

        except NoSuchElementException:
            # If the popup or like button doesn't load, wait for 2 seconds before retrying
            sleep(2)



driver.close() 