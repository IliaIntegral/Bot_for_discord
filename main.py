import random
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Ctreating_Data import *
from time import sleep
from random import uniform

X_PATHNEW = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/main/form/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div'
def define_driver():
    path_to_driver = 'C:\\Users\\ilya_\\PycharmProjects\\chromedriver.exe'
    options = webdriver.ChromeOptions()
    return webdriver.Chrome(executable_path=path_to_driver, options=options)

def send_message(text, textbox):
    textbox.send_keys(text)
    textbox.send_keys(Keys.ENTER)
driver = define_driver()
driver.get('https://discord.com/login')
#mail = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input")
#mail.send_keys("Ilya_komarov_2003@bk.ru")
input()

for i in range(len(DS.ds)):
    try:
        textbox = driver.find_element(By.XPATH, X_PATHNEW)
        sleep(90)
        send_message(DS.ds[i], textbox)
    except:
        print('mistake')
"""while True:
    try:
        textbox = driver.find_element(By.XPATH, X_PATH)
        sleep(5 + uniform(0, 3))
        send_message(MESSAGES_DS[random.randint(0, len(MESSAGES_DS)-1)], textbox)
    except selenium.common.exceptions.ElementNotInteractableException:
        print('huevo')
        input()"""