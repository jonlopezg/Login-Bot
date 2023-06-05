from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import info
# make sure this path is correct
PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

Xima = "http://xima:9080/web/realtime-displays/realtime-wallboards"


driver.get(Xima)
driver.maximize_window()

emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mat-input-0"))
             )
emailField.send_keys(info.email)




emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mat-input-1"))
             )
emailField.send_keys(info.password)

wait = WebDriverWait(driver, 10)
atcBtn = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-login-layout/app-login/div/mat-card/form/button')))
atcBtn.click()


delay = WebDriverWait(driver, 10)
atcBtn2 = delay.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home-container/app-home/mat-sidenav-container/mat-sidenav-content/div/div/app-realtime-displays-container/app-realtime-displays/mat-sidenav-container/mat-sidenav-content/div/div/app-realtime-wallboards-container/app-realtime-wallboards/div/div[2]/app-realtime-wallboards-item[2]/div/div[1]/mat-card/mat-card-content/div[2]/div/div[2]/button/span[1]/mat-icon')))
atcBtn2.click()

delay = WebDriverWait(driver, 10)
atcBtn3 = delay.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[4]/div/div/div/div/button[1]')))
atcBtn3.click()

delay = WebDriverWait(driver, 10)
atcBtn4 = delay.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-wallboard-preview-container/app-wallboard-preview/div/mat-toolbar/app-fullscreen-btn/button/span[1]')))
atcBtn4.click()

