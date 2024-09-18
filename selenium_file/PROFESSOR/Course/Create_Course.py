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
        (By.CSS_SELECTOR, '.kQBlvO'))).click()

    time.sleep(5)

def course_page(wait):
    course_page = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header/div/div[1]/nav/a[2]'))).click()
    
def create_course(wait, driver, course_amount):
    chars = string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, string.digits, string.hexdigits, string.octdigits, string.punctuation
    categ_count = 2
    prof_count = 3
    test_mod_count = 13
    
    for i in range(course_amount):
        add_course_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section/article[1]/a'))).click()
        
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\selenium_file\movie.png')
        
        name_input = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys(f'Auto professor course {i}')
        
        desc_input = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys(f'Auto professor description {i}')
        
        tag_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/article[2]/article/div[2]/div[2]/input')))
        tag_input.send_keys('Professor tag')
        tag_input.submit()
        
        hrs_input = wait.until(EC.element_to_be_clickable((By.NAME, 'hours'))).send_keys(random.randint(1, 200))
        
        catg_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/article[2]/article/div[1]/label/div/div'))).click()
        
        catg_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-{categ_count}-option-0"]'))).click()
        
        next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
        
        mod_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/form[1]/div[2]/div/input')))
        mod_input.send_keys(f'Module {i}')
        mod_input.submit()
        
        prof_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/form[1]/div[3]/label[1]/div/div'))).click()
        prod_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-{prof_count}-option-0"]'))).click()
        
        next_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/form[2]/button'))).click()
        
        # Video
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Video Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor Video Description')
        
        video_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[1]/div'))).click()
        
        video_url = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[2]/input'))).send_keys('https://youtu.be/ZFHSyKDpgB4?t=11')
        
        video_search = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[2]/div/button[2]'))).click()
        
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        # Text
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Text Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor Text Description')
        
        text_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[2]/div'))).click()
        
        text_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[2]/label/textarea'))).send_keys(chars)
    
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        # Image
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Image Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor Image Description')
        
        image_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[3]/div'))).click()
        
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\selenium_file\movie.png')
        
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        # Audio
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Audio Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor Audio Description')
        
        audio_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[4]/div'))).click()
        
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\selenium_file\Lego yoda death sound.mp3')
        
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        # File
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor File Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor File Description')
        
        file_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[5]/div'))).click()
        
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\selenium_file\movie.png')
        
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        # Choice
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Choice Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor Choice Description')
        
        choice_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[7]/div'))).click()
        
        choice_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[1]/label/div/input'))).send_keys('Choice')
        
        add_choice = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/button')))
        add_choice.click()
        add_choice.click()
        
        right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[2]/ul/li[1]/input'))).send_keys('Right')
        wrong = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[2]/ul/li[2]/input'))).send_keys('Wrong')
        
        is_right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div'))).click()
        
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        # Dissertative
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Text Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor Text Description')
        
        diss_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[8]/div'))).click()
        
        text_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[2]/label/textarea'))).send_keys(chars)
    
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        # Essay
        add_class_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section[2]/ul/article/img'))).click()
        
        class_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Text Class')
        
        class_desc = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Professor Text Description')
        
        essay_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[3]/div[2]/button[9]/div'))).click()
        
        text_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/div/div/div/div[1]/label/div/input'))).send_keys(chars)
    
        points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')
        
        finish_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/header/div/div[3]/button'))).click()
        
        conclude_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        save_coursen_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header[2]/div/div[3]/button'))).click()
        
        save_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
        
        time.sleep(5.3)
        
        go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button[2]'))).click()
        
        time.sleep(1)
        
        # Test
        eye_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//img[contains(@src, "eyer")]'))).click()
        
        tests_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[1]/nav/button[3]'))).click()
        
        add_test_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/section/article/article/a'))).click()
        
        test_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Professor Test')
    
        test_module_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[1]/label/div/div'))).click()
        test_module_option = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="react-select-{test_mod_count}-option-0"]'))).click()
        
        test_tries = wait.until(EC.element_to_be_clickable((By.NAME, 'tryQuantity'))).send_keys('5')
        
        # Choice
        choice_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[4]/button[7]/div'))).click()
        
        choice_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[2]/section/div/div/div/div[1]/label/div/input'))).send_keys('Choice Test')
        
        add_choice = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[2]/section/div/div/div/button')))
        add_choice.click()
        add_choice.click()
        
        right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[2]/section/div/div/div/div[2]/ul/li[1]/input'))).send_keys('Right')
        wrong = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[2]/section/div/div/div/div[2]/ul/li[2]/input'))).send_keys('Wrong')
        
        is_right = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div'))).click()
        
        test_points = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/input')))
        test_points.clear()
        test_points.send_keys('10')
        
        create_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/header/div/div[3]/button'))).click()
        
        end_test = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
        
        time.sleep(4)
        
        close_modal = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        time.sleep(5.5)
        
        go_back2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="VolTAR"]'))).click()
        
        categ_count += 12
        prof_count += 12
        test_mod_count += 12

        time.sleep(1)
        
        
        
def course(email, password, course_amount):
    driver_path = 'selenium_file\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)
    driver.get(os.getenv('PROFESSOR_URL'))
    wait = WebDriverWait(driver, 5)

    login(wait, email, password, driver)

    course_page(wait)
    
    create_course(wait, driver, course_amount)

    time.sleep(5)

    driver.quit()


def main():
    # Define o número de processos que você quer rodar em paralelo
    num_processes = int(get_user_input("How many users to simulate?"))

    course_amount = int(get_user_input('How many courses?'))

    credentials = []
    for _ in range(num_processes):
        # Capture email and password
        email = get_user_input('Email')
        password = get_user_input('Password')
        credentials.append((email, password))

    processes = []
    for email, password in credentials:
        p = multiprocessing.Process(
            target=course, args=(email, password, course_amount))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(u'\033[0;32mDONE!')


if __name__ == "__main__":
    main()
