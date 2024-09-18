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
import random

load_dotenv()

def login(wait, email, password, driver):
    
    driver.execute_script("document.body.style.zoom = '0.4'")
    
    time.sleep(1)
    
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password)
    
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dpkCTM'))).click()
    
    time.sleep(5)

def professor_page(wait):
    user_control_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[4]'))).click()
    
    professor_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[2]'))).click()
    
def make_professor(wait, prof_amount):
    
    for i in range(prof_amount):
        rand = random.randint(999,99999999999)
        new_professor_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="__next"]/main/div[2]/section/div[2]/div[2]/div/a'))).click()
        
        email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(f'professor{rand}@gmail.com')
        
        time.sleep(0.5)
        
        cpf_input = wait.until(EC.element_to_be_clickable((By.NAME, 'cpf'))).send_keys(gera_e_valida_cpf())
        
        time.sleep(0.5)
        
        name_input = wait.until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys(f'Professor {i}')
        
        time.sleep(0.5)
        
        password = wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys('12345678')
        
        time.sleep(0.5)
        
        password_conf = wait.until(EC.element_to_be_clickable((By.NAME, 'passwordConfirmation'))).send_keys('12345678')
        
        time.sleep(0.5)
        
        add_professor = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
        
        close_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
def create_professor(email, password, prof_amount):
    driver_path = 'selenium_file\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password, driver)

    professor_page(wait)
    
    make_professor(wait, prof_amount)
    
    driver.quit()

def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))
    
    prof_amount = int(get_user_input("How many professors?"))
    
    credentials = []
    for _ in range(num_processes):
        # Capture email and password
        email = get_user_input('Email')
        password = get_user_input('Password')
        credentials.append((email, password))

    processes = []
    for email, password in credentials:
        p = multiprocessing.Process(target=create_professor, args=(email, password, prof_amount))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(u'\033[0;32mDONE!')
        

if __name__ == "__main__":
    main()
