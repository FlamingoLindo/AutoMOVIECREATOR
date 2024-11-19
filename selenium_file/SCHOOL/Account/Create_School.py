import sys
import os
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..'))
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

def create_account_1(wait):
    rand_name = create_random_name()
    password_value = '12345678'
    
    new_account_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.eIsPXx'))).click()

    name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys(rand_name)
    
    time.sleep(0.3)
    
    phone = wait.until(EC.element_to_be_clickable((By.NAME, 'phone'))).send_keys(create_phone())
    
    time.sleep(0.3)
    
    cpf_cnpj = wait.until(EC.element_to_be_clickable((By.NAME, 'cpfCnpj'))).send_keys(gera_cnpj())
    
    time.sleep(0.3)
    
    email = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(rand_name, '@gmail.com')
    
    time.sleep(0.3)
    
    password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[5]/label/input'))).send_keys(password_value)

    time.sleep(0.3)

    password_conf = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[2]/div[6]/label/input'))).send_keys(password_value)

    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bKCzQa'))).click()
    
def create_account_internal():
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)
    
    create_account_1(wait)

    internal_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div/div[1]/div/label[2]/div'))).click()
    
    create_acc_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bKCzQa'))).click()
    
    lets_go_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/a'))).click()
    
    time.sleep(3)
    
    driver.quit()
    
def create_account_external():
    driver = webdriver.Chrome()
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)
    
    create_account_1(wait)

    create_acc_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bKCzQa'))).click()
    
    lets_go_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/a'))).click()
    
    time.sleep(5)
    
    driver.quit()

def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))

    processes = []
    for _ in range(num_processes):
        rand = random.randint(1,2)
        if rand == 1:
            # Change type of account
            p = multiprocessing.Process(target=create_account_external)
        else:
            # Change type of account
            p = multiprocessing.Process(target=create_account_internal)
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
