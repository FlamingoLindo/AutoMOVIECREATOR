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
import multiprocessing
import string
import random
import pyautogui

load_dotenv()


def login(wait, email, password, driver):

    driver.execute_script("document.body.style.zoom = '0.4'")

    time.sleep(1)

    email_input = wait.until(EC.element_to_be_clickable(
        (By.NAME, 'email'))).send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable(
        (By.NAME, 'password'))).send_keys(password)

    login_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.dpkCTM'))).click()

    time.sleep(5)


def course_page(wait):
    course_page = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]'))).click()

    pack_page = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a[3]'))).click()

    
def new_pack(wait, driver, pack_amount):
    count = 3
    for i in range(pack_amount):
        new_pack_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[2]/a'))).click()
        
        time.sleep(1)
        
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\selenium_file\movie.png')
        
        name_input = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'name'))).send_keys(f'Pack {i}')
        
        description_input = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'description'))).send_keys(f'Description {i}')
        
        add_course = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div[1]/div[2]/div[2]/label/label'))).click()
        
        single_payment_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/label/div'))).click()
        
        price_input = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'paymentPrice'))).send_keys(random.randint(1,50000))
        
        acces_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/label/div/label/div/div'))).click()
        
        acces_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'//*[@id="react-select-{count}-option-0"]'))).click()
        
        add_pack = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button'))).click()
        
        create_pack = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
        
        go_back = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        count += 2

def create_course_pack(email, password, pack_amount):
    driver_path = 'selenium_file\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)

    login(wait, email, password, driver)

    course_page(wait)

    new_pack(wait, driver, pack_amount)

    time.sleep(5)

    driver.quit()


def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))

    pack_amount = int(get_user_input('How many course packs?'))

    credentials = []
    for _ in range(num_processes):
        # Capture email and password
        email = get_user_input('Email')
        password = get_user_input('Password')
        credentials.append((email, password))

    processes = []
    for email, password in credentials:
        p = multiprocessing.Process(
            target=create_course_pack, args=(email, password, pack_amount))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(u'\033[0;32mDONE!')


if __name__ == "__main__":
    main()
