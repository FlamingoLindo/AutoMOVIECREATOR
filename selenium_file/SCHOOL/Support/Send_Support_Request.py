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
import pyautogui

load_dotenv()

def login(wait, email, password, driver):
    
    driver.execute_script("document.body.style.zoom = '0.4'")
    
    time.sleep(1)
    
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password)
    
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dpkCTM'))).click()
    
    time.sleep(5)

def support_page(wait):
    user_config = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]'))).click()
    
    support_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/ul/a'))).click()
    
def make_support(wait, support_amount, driver):
    
    for i in range(support_amount):
        
        start_suport = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/a'))).click()
        
        time.sleep(0.5)
              
        new_support = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[2]/a') 
        new_support2 = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a')    
        
        if new_support:
            new_support_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div/div[2]/a'))).click()
            print(1)
        else:
            new_support2_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a'))).click()
            print(2)

        message_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/label/textarea'))).send_keys(f'Support {i}')
        
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\selenium_file\movie.png')
        
        send_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
        
        close_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        print(u'\033[1;32mREQUEST SENT!')
                
        go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button'))).click()
        
        time.sleep(0.5)
        
        
        
def send_support(email, password, support_amount):
    driver_path = 'selenium_file\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password, driver)

    support_page(wait)
    
    make_support(wait, support_amount, driver)
    
    driver.quit()

def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))
    
    support_amount = int(get_user_input("How many support requests?"))
    
    credentials = []
    for _ in range(num_processes):
        # Capture email and password
        email = get_user_input('Email')
        password = get_user_input('Password')
        credentials.append((email, password))

    processes = []
    for email, password in credentials:
        p = multiprocessing.Process(target=send_support, args=(email, password, support_amount))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(u'\033[0;32mDONE!')
        

if __name__ == "__main__":
    main()
