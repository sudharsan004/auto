from selenium import webdriver
import time,xlrd,xlwt
b=webdriver.Chrome(r"chromedriver")
b.maximize_window()

b.get("https://evp.ecinet.in/Account/LoginOfficial?loginType=ECI")
b.find_element_by_id("UserName").send_keys('oprs22a47n1')
b.find_element_by_id("Password").send_keys('Naresh@1978')
time.sleep(15)
b.find_element_by_xpath("//*[@id='cardbox4']/div/h3").click()
time.sleep(2)
book = xlrd.open_workbook("Test.xlsx")
sheet = book.sheet_by_index(0)
l=[]
for i in range(sheet.nrows): 
    l.append(str(sheet.cell_value(i,0)))

for element in l:
    b.find_element_by_id("epicno").send_keys(element)
    b.find_element_by_id("btnGet").click()
    #b.find_element_by_id("detail_verify").click()
    #time.sleep(0.1)
    #b.find_element_by_id("doc-no").send_keys('1')
    #b.find_element_by_id("upload").send_keys('1.jpg')
    #b.find_element_by_id("submit").click()
    b.find_element_by_id("btnRefresh").click()
    time.sleep(5)
    
    




'''for i in l:
    b.get("https://evp.ecinet.in/Account/Login")
    inputElement = driver.find_element_by_id("epicno")
    inputElement.send_keys('1')

book = xlrd.open_workbook("Test.xlsx")
sheet = book.sheet_by_index(0)

l= []

for k in range(1,sheet.nrows):
    list_j.append(str(sheet.row_values(k)[j-1]))'''
