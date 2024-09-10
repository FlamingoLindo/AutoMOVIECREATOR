import sys
import os
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','..'))
sys.path.append(path_to_add)

from FUNCTIONS.Get_User_Input import *
from FUNCTIONS.Create_Name import *
from FUNCTIONS.Create_PhoneNum import *
from FUNCTIONS.Create_CPF import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import multiprocessing

load_dotenv()

def make_account(wait, driver):
    rand_name = create_random_name()
    password_value = '12345678'
    
    create_acc_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/div/a'))).click()
    
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(create_random_name(),'@gmail.com')
    
    name_input = wait.until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(create_random_name())
    
    phone_input = wait.until(EC.element_to_be_clickable((By.NAME, 'phone'))).send_keys(create_phone())
    
    cpf_input = wait.until(EC.element_to_be_clickable((By.NAME, 'cpf'))).send_keys(gera_e_valida_cpf())
    
    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password_value)
    
    pass_conf_input = wait.until(EC.element_to_be_clickable((By.NAME, 'confirm_password')))
    pass_conf_input.send_keys(password_value)
    pass_conf_input.submit()
    
    time.sleep(1)
    
    active_pages = driver.find_elements(By.CSS_SELECTOR, 'li.page-item')
    active_pages_count = len(active_pages)

    amount_school = active_pages_count * 5
    
    i = 1
    school_count = 0 
    while school_count < amount_school:
        join_school_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__next"]/main/main/div/div[3]/div[{i}]/button'))).click()
        
        school_count += 1 
        
        if i % 5 == 0:
            next_page = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__next"]/main/main/div/div[4]/ul/li[5]/a/img'))).click()
            i = 1  
        else:
            i += 1  
            
    create = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/main/div/div[5]/button'))).click()
    
    time.sleep(1)     

def create_account():
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('STUDENT_URL'))
    wait = WebDriverWait(driver, 5)
    
    make_account(wait, driver)
    
    time.sleep(3)
    
    driver.quit()
    

def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))

    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=create_account)
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
