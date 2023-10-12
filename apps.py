from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

lab_name = []
ada_email = 0
no_email = 0
ada_nomor = 0
no_nomor = 0

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pyapp.unhas.ac.id/laboratorium")
time.sleep(2)

fakultas = driver.find_element(By.XPATH, '//*[@val=6]')
fakultas.click()
time.sleep(2)

content = driver.find_element(By.XPATH, '//*[@id="fak_content"]/ul')
time.sleep(2)

labs = content.find_elements(By.TAG_NAME, 'a')

for lab in labs:
    name = lab.text
    lab_name.append(name)

for  i in range(len(lab_name)):
    scroll_to_text = lab_name[i]
    elem = driver.find_element(By.PARTIAL_LINK_TEXT, scroll_to_text)
    driver.execute_script("arguments[0].scrollIntoView();", elem)
    time.sleep(2)

    go = driver.find_element(By.PARTIAL_LINK_TEXT, lab_name[i])
    go.click()
    time.sleep(2)

    # Cek Email dan Nomor
    contact_info = driver.find_element(By.XPATH, '//*[@id="main_content"]/div/div/div[2]/div[2]/div[2]/ul[1]/li')
    contact = contact_info.text

    # Cek jika ada email 
    if "@" in contact:
        ada_email += 1
    else:
        no_email += 1
    
    # Cek jika ada nomor
    if "08" in contact:
        ada_nomor += 1
    else:
        no_nomor += 1

    time.sleep(2)

    button = driver.find_element(By.CLASS_NAME, 'ml-auto')
    driver.execute_script("arguments[0].scrollIntoView();", button)
    time.sleep(2)
    button.click()
    time.sleep(1)

if no_email == 0:
    print("Semua laboratium sudah menginput email")
else:
    print("Terdapat", no_email, "laboratorium yang belum menginput alamat email")

if no_nomor == 0:
    print("Semua laboratium sudah menginput nomor WA")
else:
    print("Terdapat", no_nomor, "laboratorium yang belum menginput nomor WA")

