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
from selenium.webdriver.common.action_chains import ActionChains
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
    
    
def buy_course(wait):
    courses_page =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/ul/li[2]'))).click()

    click_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/div/div'))).click()
    
    buy_course_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/div/div/div[2]/div[1]/a'))).click()
    
    time.sleep(2)
    
    buy_now_btn =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/section/div[3]/button'))).click()
    
    buy =  wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button'))).click()
    
    time.sleep(5)
    
    home_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/section/div/a'))).click()
    
    time.sleep(3)
    
def favorite_course(wait):
    click_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/div/div'))).click()
    fav = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/div/div/div[2]/div[1]/div[1]'))).click()

def send_comment(wait, driver):
    
    add_comment_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-wrapper"]/section/div[1]/div[3]/div')))
    
    ActionChains(driver).move_to_element(add_comment_btn).perform()
    
    add_comment_btn.click()
    
    text_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-comment"]/section/textarea'))).send_keys('Comment')
    
    publish_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-comment"]/section/button'))).click()


def do_course(wait, driver):
    click_course = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div'))).click()
    open_course = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="0"]/div/div/div[2]/div[1]/button/div'))).click()
    
    time.sleep(1)

    # Video
    send_comment(wait, driver)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    # Text
    send_comment(wait, driver)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    close_achv = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    # Image
    send_comment(wait, driver)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    # Audio
    send_comment(wait, driver)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    close_achv = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    # File
    send_comment(wait, driver)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    # Choice
    send_comment(wait, driver)
    
    click_right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/div[1]')))
    ActionChains(driver).move_to_element(click_right).perform()
    click_right.click()
    
    time.sleep(1)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

    time.sleep(0.5)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    # Dissertative
    send_comment(wait, driver)
    
    text_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/textarea'))).send_keys('Auto')
    
    send = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(0.5)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    time.sleep(0.5)
    
    close_achv = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(0.5)
    
    # Essay
    send_comment(wait, driver)
    
    text_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/textarea'))).send_keys('Auto')
    
    time.sleep(0.5)
    
    send = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-wrapper"]/div[2]/div/div[2]/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(0.5)
    
    do_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/aside/div[2]/div[2]/button'))).click()
    
    time.sleep(0.5)
    
    close_achv = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(0.5)
    
    get_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(1.5)

def do_test(wait):
    test_page_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div[1]/div/a[1]/button'))).click()
    
def course(email, password):
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('STUDENT_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password, driver)
    
    buy_course(wait)
    
    favorite_course(wait)

    do_course(wait, driver)
    
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
        p = multiprocessing.Process(target=course, args=(email, password))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()

