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

CARD_NUM = '5543451621296316'
EXP_DATE = '0126'
CVV = '827'

def login(wait, email, password, driver):
    global found
    
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
    
    
def set_up_account(wait, driver):
    time.sleep(1)

    profile_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]')))
    profile_btn.click()   
    
    set_up_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/ul/li[4]'))).click() 
    
    time.sleep(1)
    
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(r'V:\..DevApp\AutoMOVIECREATOR\movie.png')
    
    """adresses_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[4]'))).click()
    
    cep_input = wait.until(EC.element_to_be_clickable((By.NAME, 'zipcode'))).send_keys('01001-000')
    
    time.sleep(1)
    
    num_input = wait.until(EC.element_to_be_clickable((By.NAME, 'number'))).send_keys('1')
    
    save_adress_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/button'))).click()
    
    time.sleep(3.2)"""
    
    payment_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[3]'))).click()
    
    add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a/div'))).click()
    
    time.sleep(1)
    
    finish_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/button'))).click()
    
    name = driver.find_element(By.NAME, 'name')
    driver.execute_script(f"arguments[0].value = 'autocard';", name)
    
    time.sleep(0.5)
    
    cvv = driver.find_element(By.NAME, 'cvv')
    driver.execute_script(f"arguments[0].value = '{CVV}';", cvv)

    time.sleep(0.5)
    
    cpf = driver.find_element(By.NAME, 'cpf')
    driver.execute_script(f"arguments[0].value = '{gera_e_valida_cpf()}';", cpf)
    
    time.sleep(0.5)
    
    num = driver.find_element(By.NAME, 'cardNumber')
    driver.execute_script(f"arguments[0].value = '{CARD_NUM}';", num)

    time.sleep(0.5)

    exp = driver.find_element(By.NAME, 'validity')
    driver.execute_script(f"arguments[0].value = '{EXP_DATE}';", exp)
    
    time.sleep(0.5)
    
    card_done = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
    
    time.sleep(1)
    
    ok_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(10)
    
    profile_btn.click()   
    
    plan_btn_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/ul/li[3]'))).click() 
    
    see_plans_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/div/div/button'))).click() 
    
    plan1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[1]/div[1]/div'))).click()
    
    save_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button[2]'))).click()
    
    buy_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button'))).click()
    
    confirm_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]'))).click()
    
    time.sleep(6)

def config_profile(email, password):
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('STUDENT_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password, driver)
    
    set_up_account(wait, driver)
    
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
        p = multiprocessing.Process(target=config_profile, args=(email, password))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()

