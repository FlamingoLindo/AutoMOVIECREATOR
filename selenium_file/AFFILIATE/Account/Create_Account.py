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

def new_acc_page(wait):
    new_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/form/div[4]/a'))).click()
    
def acc_form(wait):
    name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys(create_random_name())
    
    email = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(create_random_name(),'@gmail.com')
    
    cpf = wait.until(EC.element_to_be_clickable((By.NAME, 'cpf'))).send_keys(gera_e_valida_cpf())
    
    password = wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys('12345678')
    
    password_conf = wait.until(EC.element_to_be_clickable((By.NAME, 'confirmPassword')))
    password_conf.send_keys('12345678')
    password_conf.submit()
    
def about_me(wait):
    infor_input = wait.until(EC.element_to_be_clickable((By.NAME, 'informations'))).send_keys('This user was automatically generated')
    
    link1 = wait.until(EC.element_to_be_clickable((By.NAME, 'linkedin'))).send_keys('https://afiliado-mestreseducacao.vercel.app/register')
    
    link2 = wait.until(EC.element_to_be_clickable((By.NAME, 'instagram')))
    link2.send_keys('https://afiliado-mestreseducacao.vercel.app/register')
    link2.submit()

def schools(wait, driver):
    time.sleep(1)
    
    school_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[3]/form/div[1]/div[1]/label[4]'))).click()

    next = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div/main/div[2]/div[2]/div[3]/form/button'))).click()
    
    time.sleep(10)
    
    
    
def create_account():
    
    driver = webdriver.Chrome()
    driver.get(os.getenv('AFF_URL'))
    wait = WebDriverWait(driver, 5)
    
    new_acc_page(wait)
    
    acc_form(wait)
    
    about_me(wait)
    
    schools(wait, driver)
    
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
