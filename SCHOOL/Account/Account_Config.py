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

def login(wait, email, password, driver):
    
    driver.execute_script("document.body.style.zoom = '0.4'")
    
    time.sleep(1)
    
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(email)

    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys(password)
    
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dpkCTM'))).click()
    
    time.sleep(5)

def open_profile_configs(wait):
    gear_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/div[1]'))).click()
    
def sales_configurations(wait):
    # subscription plans
    subs_plan_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[2]'))).click()
    
    add_sub = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/a/div'))).click()
    
    sub_name = wait.until(EC.element_to_be_clickable((By.NAME, 'name'))).send_keys('Auto Subscription')
    
    sub_value = wait.until(EC.element_to_be_clickable((By.NAME, 'value'))).send_keys(random.randint(10,9999))
    
    sub_description = wait.until(EC.element_to_be_clickable((By.NAME, 'description'))).send_keys('Auto description')
    
    sub_differential = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[2]/div/label/div/input'))).send_keys('Auto differential')
    
    send_diff = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[2]/div/label/div/div/button'))).click()
    
    sub_time_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[1]/label/div/div'))).click()
    
    sub_time_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-2-option-0"]'))).click()
    
    #installment_option  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[3]/label'))).click()
    
    #installment_value  = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[1]/div[3]/div/label/input'))).send_keys(random.randint(2,12))
    
    #allow_discount_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[2]/div/label[2]/div'))).click()

    #discount_value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/div[2]/div/div/div/label/input'))).send_keys(random.randint(1,99))
    
    save_plan_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form[3]/button'))).click()
    
    confirm_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/div/button[2]'))).click()
    
    go_back_plan = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button')))
    go_back.click()
    
    # Course category
    course_category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/div/a[3]'))).click()
    
    create_course_category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/button'))).click()
    
    category_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[1]/label/div/input'))).send_keys('Auto Category Test ', random.randint(1,999999999999999999))
    
    category_on = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[2]/div/label'))).click()
    
    create_category_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[3]/button[2]'))).click()
    
    time.sleep(1)
    
    category_ok = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    time.sleep(1)
    
    open_profile_configs(wait)

def charge_discount(wait):
    # Discount_cupons
    cupons_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div/a[2]'))).click()
    
    add_coupon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/div/div/a'))).click()
    
    coupon_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/label/div/input'))).send_keys('Automatic Cupon ', random.randint(1,999999))
    
    time.sleep(0.5)
    
    cupon_value = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/label/div/input')))
    cupon_value.clear()
    cupon_value.send_keys(random.randint(1,90))
    
    cupon_time_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label[1]/div'))).click()
    
    inset_cupo_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[3]/div/label/div/input'))).send_keys('10102099')
    
    save_cupon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
    
    done_cupon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button')))
    go_back.click()

def internal(wait, driver):
    # Classes
    classes_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div/a[1]'))).click()
    
    add_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div/a'))).click()
    
    coupon_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/label/div/input'))).send_keys('Automatic Class ', random.randint(1,99999999))
    
    class_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div/label/div/input'))).send_keys('Auto Class ', random.randint(1,9999999))
    
    class_period = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/label/div/div'))).click()
    
    class_period_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-3-option-0"]'))).click()
    
    save_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/button'))).click()
    
    done_class = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button'))).click()
    
    go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/header/button')))
    go_back.click()
    
    # Kit midia
    kit_midia_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div/a[3]'))).click()

    add_midia = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/section/div[2]/div[2]/div/button'))).click()
    
    midia_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[1]/div[1]/label/div/input'))).send_keys('Auto Midia ', random.randint(1,999999))

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\movie.png')
    
    add_file = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/form/div[2]/button[2]'))).click()
    
    time.sleep(3)
    
    go_back = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div/header/button')))
    go_back.click()
    
def gamefication(wait, driver):
    # Achiviemnts
    achiv_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[5]/div[2]/a[1]'))).click()
    
    ## 1
    ach1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[1]/div/a/img'))).click()
    
    time.sleep(1)
    
    emb1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb1.click()
    
    next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    next1.click()
    
    emb2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb2.click()
    
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next2.click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')))
    name.send_keys('Auto emblem ', random.randint(1,99999999))
    
    next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next3.click()
    
    see_embs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    see_embs.click()
    
    time.sleep(2)
    
    ## 2
    ach2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[2]/div/a/img'))).click()
    
    time.sleep(1)
    
    emb1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb1.click()
    
    next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    next1.click()
    
    emb2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb2.click()
    
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next2.click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')))
    name.send_keys('Auto emblem ', random.randint(1,99999999))
    
    next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next3.click()
    
    see_embs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    see_embs.click()
    
    time.sleep(2)
    
    ## 3
    ach3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[3]/div/a/img'))).click()
    
    time.sleep(1)
    
    emb1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb1.click()
    
    next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    next1.click()
    
    emb2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb2.click()
    
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next2.click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')))
    name.send_keys('Auto emblem ', random.randint(1,99999999))
    
    next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next3.click()
    
    see_embs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    see_embs.click()
    
    time.sleep(2)
    
    ## 4
    ach4 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[4]/div/a/img'))).click()
    
    time.sleep(1)
    
    emb1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb1.click()
    
    next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    next1.click()
    
    emb2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb2.click()
    
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next2.click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')))
    name.send_keys('Auto emblem ', random.randint(1,99999999))
    
    next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next3.click()
    
    see_embs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    see_embs.click()
    
    time.sleep(2)
    
    ## 5
    ach5 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[5]/div/a/img'))).click()
    
    time.sleep(1)
    
    emb1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb1.click()
    
    next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    next1.click()
    
    emb2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb2.click()
    
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next2.click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')))
    name.send_keys('Auto emblem ', random.randint(1,99999999))
    
    next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next3.click()
    
    see_embs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    see_embs.click()
    
    time.sleep(2)
    
    ## 6
    ach6 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[6]/div/a/img'))).click()
    
    time.sleep(1)
    
    emb1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb1.click()
    
    next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    next1.click()
    
    emb2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb2.click()
    
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next2.click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')))
    name.send_keys('Auto emblem ', random.randint(1,99999999))
    
    next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next3.click()
    
    see_embs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    see_embs.click()
    
    time.sleep(2)
    
    ## 7
    ach7 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/ul/li[7]/div/a/img'))).click()
    
    time.sleep(1)
    
    emb1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb1.click()
    
    next1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button')))
    next1.click()
    
    emb2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/ul/li[2]/button')))
    emb2.click()
    
    next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next2.click()
    
    name = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[4]/div[1]/div[2]/div/label/div/input')))
    name.send_keys('Auto emblem ', random.randint(1,99999999))
    
    next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/footer/button[2]')))
    next3.click()
    
    see_embs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal-root"]/div[2]/div/div/button')))
    see_embs.click()

    time.sleep(2)
    
    gear = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/div[1]'))).click()

    # Prize Store
    prize_store_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[5]/div[2]/a[2]'))).click()
    
    new_prize_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/a'))).click()
    
    external_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[1]/div/label[1]/div'))).click()

    prize_type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[1]/div[2]/label/div/div'))).click()

    prize_type_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-2-option-0"]'))).click()
    
    prize_name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[2]/label/div/input'))).send_keys('Auto Prize', random.randint(1,9999999))
    
    prize_value_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[3]/div[1]/div/label/div/input'))).send_keys(random.randint(1,999))
    
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(r'C:\Users\josef\Desktop\AutoMOVIECREATOR\movie.png')

    prize_description_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/div[5]/label/textarea'))).send_keys('Auto Prize', random.randint(1,9999999))

    add_prize = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/form/footer/button'))).click()
    
    time.sleep(5)
    
    
def config_profile(email, password):
    driver_path = './chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s)  
    driver.get(os.getenv('SCHOOL_URL'))
    wait = WebDriverWait(driver, 5)
    
    login(wait, email, password, driver)

    open_profile_configs(wait)
    
    sales_configurations(wait)
    
    charge_discount(wait)
    
    internal(wait, driver)
    
    gamefication(wait, driver)
        
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
        p = multiprocessing.Process(target=config_profile, args=(email, password))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
