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
        (By.CSS_SELECTOR, '.kQBlvO'))).click()

    time.sleep(5)

def correct_activitie(wait):
    count = 1
    try:
        while True:
            arrow_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="__next"]/main/div/div/div/section[1]/article[1]/article/ul/li[{count}]/a'))).click()
            
            answer_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/footer/button'))).click()    
            
            text_input = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys(string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, string.digits, string.hexdigits, string.octdigits, string.punctuation)

            send_correction = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/footer/button'))).click()
            
            save = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
            
            go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

            go_back2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VolTAR"]'))).click()
            
            count += 1
            
            if count > 3:
                count = 1

            time.sleep(3)
    except:
        print('No more activites to correct!')
    
def activitie(email, password):
    driver_path = 'selenium_file\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)
    driver.get(os.getenv('PROFESSOR_URL'))
    wait = WebDriverWait(driver, 5)

    login(wait, email, password, driver)

    correct_activitie(wait)

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
        p = multiprocessing.Process(
            target=activitie, args=(email, password))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(u'\033[0;32mDONE!')


if __name__ == "__main__":
    main()
