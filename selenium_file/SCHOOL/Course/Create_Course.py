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
        (By.CSS_SELECTOR, '.dpkCTM'))).click()

    time.sleep(5)


def course_page(wait):
    course_page = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]'))).click()


def make_course(wait, driver, course_amount):
    chars = string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, string.digits, string.hexdigits, string.octdigits, string.punctuation
    categ_count = 2
    prof_count = 3
    test_mod_count = 13
    pay_count = 14
    
    for i in range(course_amount):
        create_new_course_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div[2]/div/a'))).click()

        time.sleep(1)

        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\movie.png')

        name_input = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys(
            'Auto course ', random.randint(1, 999999999))

        description_input = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'description'))).send_keys('Auto course ', random.randint(1, 999999999))

        tag = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/div/label/div/input')))
        tag.send_keys('Auto course ', random.randint(1, 999999999))
        tag.submit()

        course_catg_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mainForm"]/div/label[2]/div/div'))).click()
        time.sleep(1)
        course_catg_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'//div[@id="react-select-{categ_count}-listbox"]/div/div'))).click()

        course_time = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'hours'))).send_keys(random.randint(1, 250))

        continue_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[3]/button'))).click()

        module_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/div/label/div/input'))).send_keys('Module ', random.randint(1, 250))
        add_module = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[1]/button'))).click()

        profs_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/div/form[2]/label[1]/div/div'))).click()
        profs_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'//*[@id="react-select-{prof_count}-option-0"]'))).click()

        continue2_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[2]/form/button'))).click()

        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a'))).click()

        # Video
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('Video class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('Video description')

        video_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[1]/div'))).click()

        video_url = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/input'))).send_keys('https://www.youtube.com/watch?v=kzo5gxdNuyA')
        add_video = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/div/button[2]'))).click()

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        # Text
        time.sleep(1)
        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        time.sleep(1)
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('Text class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('Text description')

        text_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[2]/div'))).click()

        input_text = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea'))).send_keys(chars)

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        # Image
        time.sleep(1)
        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        time.sleep(1)
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('Image class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('Image description')

        image_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[3]/div'))).click()

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(
            r'C:\Users\josef\Desktop\AutoMOVIECREATOR\movie.png')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        # Audio
        time.sleep(1)
        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        time.sleep(1)
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('Audio class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('Audio description')

        audio_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[4]/div'))).click()

        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(
            r"C:\Users\josef\Desktop\AutoMOVIECREATOR\Lego yoda death sound.mp3")

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        # File
        time.sleep(1)
        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        time.sleep(1)
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('File class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('File description')

        file_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[5]/div'))).click()

        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(
            r"C:\Users\josef\Desktop\AutoMOVIECREATOR\movie.png")

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
        close_modal.click()

        """# Code
            time.sleep(1)
            add_class = wait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img')))
            add_class.click()
            time.sleep(1)
            class_name = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input')))
            class_name.send_keys('Code class')

            class_desc = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea')))
            class_desc.send_keys('Code description')

            code_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[6]/div'))).click()

            send_code = driver.find_element(
                By.XPATH, "//div[@id='ace-editor']/div[2]/div")
            send_code.click()

            points = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
            points.clear()
            points.send_keys('10')

            finish_class = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button')))
            finish_class.click()

            close_modal = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
            close_modal.click()"""

        # Choice
        time.sleep(1)
        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        time.sleep(1)
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('Choice class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('Choice description')

        choice_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[7]/div'))).click()

        choie_title = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input'))).send_keys('Choise')

        add_alternative = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/button')))
        add_alternative.click()
        add_alternative.click()

        alt1 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/input'))).send_keys('Right')
        alt2 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[2]/input'))).send_keys('Wrong')

        is_right = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div'))).click()

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        # Dissertative
        time.sleep(1)
        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        time.sleep(1)
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('Dissertative class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('Dissertative description')

        dissertative_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[8]/div'))).click()

        dissertative_text = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[2]/label/textarea'))).send_keys(chars)

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        # Essay
        time.sleep(1)
        add_class = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/a/img'))).click()
        time.sleep(1)
        class_name = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/label/div/input'))).send_keys('Essay class')

        class_desc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[1]/div[3]/label/div/label/textarea'))).send_keys('Essay description')

        essay_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[3]/div[2]/button[9]/div'))).click()

        essay_text = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/div/div/div/div[1]/label/div/input'))).send_keys(chars)

        points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/section/footer/label/input')))
        points.clear()
        points.send_keys('10')

        finish_class = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/header/button'))).click()

        close_modal = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

        end_class_creation = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/header/button'))).click()

        time.sleep(5)
        
        count = 1
        view_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'a[data-com="ButtonIcon"]'))).click()
        
        # Test
        test_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div[1]/nav/a[3]'))).click()
        
        new_test_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div/a/div/div'))).click()
        
        test_name = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'name'))).send_keys('Test')
        
        module_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/label/div/div'))).click()
        time.sleep(1.5)
        module_option= wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'//*[@id="react-select-{test_mod_count}-option-0"]'))).click()
        
        test_try_time = wait.until(EC.element_to_be_clickable(
            (By.NAME, 'tryQuantity'))).send_keys('5')
        
        choise_test_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/button[7]/div'))).click()
        
        choise_points = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/input'))).send_keys('10')
        
        choise_test_title = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[1]/label/div/input'))).send_keys('Test Question')
        
        add_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/button')))
        add_option.click()
        add_option.click()
        
        choise_1 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/input'))).send_keys('Right')
        
        choise_1 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[2]/input'))).send_keys('Wrong')
        
        is_right_test = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/section/div/div/div/div[2]/ul/li[1]/div[2]/label[1]/div'))).click()
        
        test_done = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/header/button'))).click()
        
        save_test = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
        
        list_test = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        general_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/nav/a[1]'))).click()
        
        anal_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/a'))).click()

        for i in range(8):
            approve_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f'//button[contains(.,"Aprovar")]'))).click()

            accept_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()

            ok_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()

            count += 1

            time.sleep(1)

        anal_test = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/nav/a[2]'))).click()
        
        approve_test_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="__next"]/main/div[2]/ul/div/ul/li/div/div/div/button[1]'))).click()
        
        accpet_test_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
        
        ok_test_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        go_back = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/ul/li[2]/a'))).click()
        
        anal_course = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a[2]'))).click()
        
        approve_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div[2]/div[11]/div/button[1]'))).click()
        
        accept_course_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div[2]/button[2]'))).click()
        
        ok_course_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        go_back3 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a[1]'))).click()

        time.sleep(1)

        edit_button = driver.find_element(By.XPATH, "//td[@data-com='TableCell']//div[@data-com='ButtonContainer']//button[1]").click()
        
        pay_on_dropdown = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/form/div/div[2]/div/label/div/div'))).click()  

        pay_on_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'//*[@id="react-select-{pay_count}-option-1"]'))).click()  
        
        price = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/form/div/div[2]/label/div/input'))).send_keys(random.randint(1,50000)) 
        
        save_course = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/form/div/button'))).click()
        
        save_course2 = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
        
        ok_course = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
        
        categ_count += 13
        prof_count += 13
        test_mod_count += 13
        pay_count += 13
        
def create_course(email, password, course_amount):
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)

    login(wait, email, password, driver)

    course_page(wait)

    make_course(wait, driver, course_amount)

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
            target=create_course, args=(email, password, course_amount))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    print(u'\033[0;32mDONE!')


if __name__ == "__main__":
    main()
