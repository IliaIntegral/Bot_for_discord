from selenium.webdriver.chrome.service import Service
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Ctreating_Data import *
from time import sleep
"doesn'n work"
X_PATHNEW = '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/main/form/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div'

def send_message(text, textbox):
    textbox.send_keys(text)
    textbox.send_keys(Keys.ENTER)
s = Service("C:\\Users\\ilya_\\PycharmProjects\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://discord.com/login')

input()

for i in range(len(DS.ds)):
    try:
        textbox = driver.find_element(By.XPATH, X_PATHNEW)
        sleep(90)
        send_message(DS.ds[i], textbox)
    except:
        print('mistake')