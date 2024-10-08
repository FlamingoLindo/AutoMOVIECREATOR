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
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from dotenv import load_dotenv
import os
import multiprocessing

load_dotenv()

found = False

def login(wait, email, password, driver):
    global found
    driver.execute_script("document.body.style.zoom = '0.4'")
    time.sleep(1)
    
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    password_input.send_keys(password)
    password_input.submit()
    
    time.sleep(1)
     
    # Define o email que você está procurando
    email_to_find = "abc3@gmail.com"

    # Loop para navegar pelas páginas e encontrar o elemento
    while True:
        try:
            # Localiza o contêiner que contém o email específico
            container = wait.until(EC.presence_of_element_located(
                (By.XPATH, f'//div[@class="sc-kpDprT iHjUIZ"]//div[contains(text(), "{email_to_find}")]')
            ))
            # Localiza o botão "Acessar" dentro do contêiner
            acessar_button = container.find_element(By.XPATH, './following-sibling::button[@data-com="Button"]')
            acessar_button.click()
            break
        except (NoSuchElementException, TimeoutException):
            # Caso o elemento não seja encontrado, clique na próxima página
            try:
                next_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[contains(@class, "nav-next")]/a')))
                print('Not found, next page!')
                next_page.click()
            except TimeoutException:
                print("Não há mais páginas para navegar.")
                break  # Sai do loop se não houver mais páginas
    
    
def buy_pack(wait):
    course_pack_page =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/ul/li[4]'))).click()

    first_pack =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/a[1]'))).click()

    time.sleep(1.5)

    buy_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button'))).click()

    time.sleep(1.5)

    credit_opt =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/section/div[2]/div/div[1]/div/label/label'))).click()

    time.sleep(1.5)

    buy_now_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/section/div[3]/button'))).click()

    time.sleep(1.5)

    buy2 =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button'))).click()

    time.sleep(5)
    

def pack(email, password):
    driver_path = 'selenium_file\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('STUDENT_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password, driver)
    
    buy_pack(wait)
    
    time.sleep(3)
    
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
        p = multiprocessing.Process(target=pack, args=(email, password))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()

