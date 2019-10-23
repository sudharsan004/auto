from selenium import webdriver
import sys,os
import time,xlrd,xlwt
from selenium.webdriver.common.keys import Keys
chromedriver = "chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
b = webdriver.Chrome(chromedriver)
#b=webdriver.Chrome(r"chromedriver")
b.maximize_window()

b.get("https://evp.ecinet.in/Account/LoginOfficial?loginType=ECI")
b.find_element_by_id("UserName").send_keys('oprs22a47n1')
b.find_element_by_id("Password").send_keys('Naresh@1978')
time.sleep(15)
#b.find_element_by_xpath("//*[@id='cardbox4']/div/h3").click()
#time.sleep(2)
book = xlrd.open_workbook("Test.xlsx")
sheet = book.sheet_by_index(0)
l=[]
for i in range(sheet.nrows): 
    l.append(str(sheet.cell_value(i,0)))

for element in l:
    b.find_element_by_id("epicno").clear()
    b.find_element_by_id("epicno").send_keys(element)
    time.sleep(1)
    b.find_element_by_id("btnGet").click()
    time.sleep(1.5)
    b.find_element_by_id("detail_verify").click()
    b.find_element_by_id("DocumentNo").send_keys('1')
    b.find_element_by_id("verification_proof_image").send_keys('/home/novice/Desktop/auto-master/1.jpg')
    b.find_element_by_id("SubmitForm").click()
    time.sleep(0.5)
    #b.get("https://evp.ecinet.in/Verification/Index")
    #time.sleep(1)

    
