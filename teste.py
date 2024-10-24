from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://movie-creator-empresa.netlify.app/')



element_locator = (By.XPATH, '//*[@id="__next"]/main/div/main/form/div[1]/h2')  # Replace with your element's selector

# Wait until the element is visible
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(element_locator))
    print("Element is visible!")
except Exception:
    print("Element not found within the given time.")
    
print('adada')
driver.quit()
    