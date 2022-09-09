from turtle import clear
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)



time.sleep(2)
print("\n" * 100)
print(r"""

██████╗░██████╗░██╗███╗░░██╗░██████╗████████╗░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗
██╔══██╗██╔══██╗██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║
██████╦╝██████╦╝██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░██╗░██████╔╝███████║██╔████╔██║
██╔══██╗██╔══██╗██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║
██████╦╝██████╦╝██║██║░╚███║██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║
╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
                """)
print("\n" * 5)
#!loging---------------------
print('↓ please enter your account information below ↓')
print("\n" * 2)
username = input('Username:')
password = input('Password:')
print("\n" * 2)
driver.get('https://www.instagram.com/')

time.sleep(4)
driver.find_element(By.XPATH,"(//input[@name='username'])[1]").click()
driver.find_element(By.XPATH,"(//input[@name='username'])[1]").send_keys(username)
time.sleep(1)
driver.find_element(By.XPATH,"(//input[@name='password'])[1]").click()
driver.find_element(By.XPATH,"(//input[@name='password'])[1]").send_keys(password)
time.sleep(1)
try:
    driver.find_element(By.XPATH,"(//input[@name='password'])[1]").send_keys(Keys.ENTER)
except:
    print("We encounter an error. Please try signing in later or check your informations")
    exit()

#? Profile-----------------------
time.sleep(5)
try:
    driver.find_element(By.XPATH,'//img[@alt="'+username+"""'in profil resmi"]""").click()
except:
    print("We encounter an error. Please try signing in later or check your informations")
    time.sleep(4)
    exit()
time.sleep(1)
driver.find_element(By.XPATH,"""(//div[contains(@class,'-Rt5j ZUqME')])[1]""").click()
time.sleep(4)


#* Following --------------\
a= int(driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[3]").text)
print(a)
x = a/2
driver.find_element(By.XPATH,"""(//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade'])[3]""").click()
time.sleep(2)
# Following list scroll
fBody  = driver.find_element(By.CLASS_NAME,"_aano")
scroll = 0
while scroll < x: # scroll x times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(0.5)
    scroll += 1                                  
time.sleep(1)
#-----------------------              
b = driver.find_elements(By.XPATH,"(//div[contains(@class,'_ab94 _ab97 _ab9f _ab9k _ab9p _abcm')])")

fli = list()
for user in b[4:a+4]:
    fli.append(user.text)

#*------------------------------------------------------------------------------------------------------
#! Followers--------------------------------------------------------------------------------------------
driver.get('https://www.instagram.com/'+username+"/")
time.sleep(4)
k = int(driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[2]").text)
print(k)
s = k/2
driver.find_element(By.XPATH,"(//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade'])[2]").click()
time.sleep(2)
# Follower list scroll
fBody  = driver.find_element(By.CLASS_NAME,"_aano")
scroll = 0
while scroll < s: # scroll x times
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(0.5)
    scroll += 1                                  
time.sleep(1)
#-----------------------   
n = driver.find_elements(By.XPATH,"(//div[contains(@class,'_ab94 _ab97 _ab9f _ab9k _ab9p _abcm')])")

fl =list()
for user1 in n[4:k+4]:
    fl.append(user1.text)
    
   

print("\n" * 100)
print("Iɴsᴛᴀɢʀᴀᴍ ᴜsᴇʀs ᴡʜᴏ ᴅᴏɴ'ᴛ ғᴏʟʟᴏᴡ ʏᴏᴜ ʙᴀᴄᴋ")
pwdf = list()
for p in fli:
    if p in fl:
        continue
    else:
        print(p)
        pwdf.append(p)
print("\n" * 19)
with open('PWDF.txt', 'a') as f:
    for l in pwdf:
        f.write(str(l)+'\n')
