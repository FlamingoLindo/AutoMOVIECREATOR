import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

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
    
def request_page(wait):
    profile_options =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]'))).click()
    
    time.sleep(0.5)
    
    support_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/ul/a'))).click()

def new_support(wait, driver, sup_ammount):
    for i in range(sup_ammount):
        new_sup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a'))).click()
        
        input_text = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/label/textarea'))).send_keys(f'Auto Support {i}')
        
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\movie.png')
        
        send_sup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
        
        close_modal = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        print(u'\033[0;34mSupport "', i,'" sent!')
    print(u'\033[0;32mALL SUPPORTS SENT!')
    

def send_request(email, password, sup_ammount):
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('STUDENT_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password, driver)

    request_page(wait)
    
    new_support(wait, driver, sup_ammount)
    
    driver.quit()
    

def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))
    
    sup_ammount = int(get_user_input('How many supports?'))
    
    credentials = []
    for _ in range(num_processes):
        # Capture email and password
        email = get_user_input('Email')
        password = get_user_input('Password')
        credentials.append((email, password))

    processes = []
    for email, password in credentials:
        p = multiprocessing.Process(target=send_request, args=(email, password, sup_ammount))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()

