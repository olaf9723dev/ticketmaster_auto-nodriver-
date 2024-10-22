from undetected_chromedriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

# Using undetected-chromedriver
options = ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome driver with undetected-chromedriver
driver = Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    # Navigate to the webpage
    driver.get("https://www.carjam.co.nz/car/?plate=UA100/")
    time.sleep(10)

    # Wait for the iframe to be present and switch to it
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
    )
    driver.switch_to.frame(iframe)

    # Wait for the checkbox to be present and then interact with it
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="checkbox"]'))
    )
    time.sleep(5)

    location = pyautogui.locateOnScreen('checkbox.png', confidence=0.8)
    if location:
       center = pyautogui.center(location)
       pyautogui.click(center)
    else:
       print("Can't find location")

    # # Check if the checkbox is not already selected
    # if not checkbox.is_selected():
    #     checkbox.click()

    # print("Checkbox checked successfully")
    
    time.sleep(10)
except:
   pass
