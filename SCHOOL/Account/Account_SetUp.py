import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

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
import multiprocessing

load_dotenv()

CARD_NUM = '5377606230012427'
EXP_DATE = '0426'
CVV = '307'

ACC_NUM = '0205105-2'
AGENCY = '2380'

def login(wait, email, password):
    
    time.sleep(1)
    
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password)
    
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dpkCTM'))).click()
    
    time.sleep(5)

def profile_options(wait):
    dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.euYZjb'))).click()
    
    profile_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/div[3]/ul/li[1]'))).click()

def add_adress(wait):
    

    adress_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[4]'))).click()
    
    new_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a'))).click()
        
    cep_input = wait.until(EC.element_to_be_clickable((By.NAME, 'zipcode'))).send_keys('01001-000')
    
    time.sleep(1)
    
    num_input = wait.until(EC.element_to_be_clickable((By.NAME, 'number'))).send_keys('1')
    
    save_adress_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
    
    done_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(5)
    
def add_payment_options(wait):
    payment_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[3]'))).click()
    
    # CARD
    add_card_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/div[1]/a'))).click()
    
    add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/a/div'))).click()
    
    input_card_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('autocard')
    
    input_card_number = wait.until(EC.element_to_be_clickable((By.NAME, 'cardNumber'))).send_keys(CARD_NUM)
    
    input_card_exp_date = wait.until(EC.element_to_be_clickable((By.NAME, 'validity'))).send_keys(EXP_DATE)
    
    input_card_cvv = wait.until(EC.element_to_be_clickable((By.NAME, 'cvv'))).send_keys(CVV)
    
    input_card_cnpj = wait.until(EC.element_to_be_clickable((By.NAME, 'cpfcnpj'))).send_keys(gera_cnpj())
    
    finish_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
    
    card_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    go_back_payment = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/header/button')))
    go_back_payment.click()
    
    # BANK
    add_bank_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/div[2]/a'))).click()
    
    add_bank = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div/a'))).click()
    
    bank_name_input = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('autobank')
    
    agency_input = wait.until(EC.element_to_be_clickable((By.NAME, 'agency'))).send_keys(AGENCY)
    
    acc_num_input = wait.until(EC.element_to_be_clickable((By.NAME, 'code'))).send_keys(ACC_NUM)
    
    input_bank_cnpj = wait.until(EC.element_to_be_clickable((By.NAME, 'cpfcnpj'))).send_keys(gera_cnpj())
    
    bank_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div/div[2]/div/label/div/div'))).click()
    
    bank_type_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="react-select-2-option-0"]'))).click()
    
    finish_bak = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
    
    bank_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(4)
    
    go_back_payment2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/header/button'))).click()
    
def buy_plan(wait):
    buy_plan_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/a'))).click()
    
    see_all_plans = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div/div/div/a'))).click()
    
    time.sleep(1)
    
    first_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]'))).click()
    
    contract_plan_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/button'))).click()
    
    buy_now = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[@id="modal-root"]/div[2]/div/div/div/button'))).click()
    
    confirm_purchase_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]'))).click()
    
    time.sleep(1)
    
    go_to_plans_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
def set_up_acount(email, password):
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password)

    profile_options(wait)

    add_adress(wait)
    
    add_payment_options(wait)
    
    buy_plan(wait)
    
    time.sleep(5)
    
    driver.quit()

def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))

    credentials = []
    for _ in range(num_processes):
        # Capture email and password
        email = get_user_input('Email')
        password = get_user_input('Password')
        credentials.append((email, password))

    processes = []
    for email, password in credentials:
        p = multiprocessing.Process(target=set_up_acount, args=(email, password))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
