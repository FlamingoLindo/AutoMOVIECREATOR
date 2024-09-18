import sys
import os
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from FUNCTIONS.Get_User_Input import *
from FUNCTIONS.Create_Name import *
from FUNCTIONS.Create_PhoneNum import *
from FUNCTIONS.Create_CNPJ import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import random
import multiprocessing

load_dotenv()

def form(wait, driver, form_amount):
    driver.execute_script("document.body.style.zoom = '0.4'")
    
    for i in range(form_amount):
        name_input = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Auto name')
        
        email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(f'email{i}@gmail.com')
        
        ddd_input = wait.until(EC.element_to_be_clickable((By.NAME, 'ddd'))).send_keys('11')
        
        phone_input = wait.until(EC.element_to_be_clickable((By.NAME, 'phone')))
        phone_input.send_keys(random.randint(111111111,999999999))
        time.sleep(1234)
        phone_input.submit()
    
def send_form(form_amount):
    driver_path = 'selenium_file\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('LANDING_URL'))
    wait = WebDriverWait(driver, 5)
    
    form(wait, driver, form_amount)

    time.sleep(5)
    
    driver.quit()

def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))
    
    form_amount = int(get_user_input('How many forms?'))
    
    processes = []
    for _ in range(num_processes):
        # Change type of account
        p = multiprocessing.Process(target=send_form, args=(form_amount,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
