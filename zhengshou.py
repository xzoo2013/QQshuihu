#!/usr/bin/python2.7
#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard


m = PyMouse()
k = PyKeyboard()


#  open Game window with open---close ----open

## 每日征收
def clickChargePopup():
    m.click(745,443)
    
def clickCharge():
    time.sleep(5)
    m.click(1165,233)
    print time.ctime()
    for i in xrange(10):
        time.sleep(2)
        clickChargePopup()

    m.click(948,368)#关闭

    
def clickShengChenGang():#生辰纲
    m.click(835,228)
## 每日运货
def everydayYH():
    clickShengChenGang()
    time.sleep(20)
    m.click(1027,613)#开始运货
    time.sleep(8)
    m.click(788,736)#回家
    
            


            
url="http://ui.ptlogin2.qq.com/cgi-bin/login?link_target=blank&daid=153&appid=614008604&hide_title_bar=1&s_url=http://game.108.qq.com/logined.html&target=self&qtarget=self&css=http://imgcache.qq.com/ptcss/qqsh/614008604/login.css&runtime=1305272225684"
browser = webdriver.Firefox() # Get local session of firefox
browser.maximize_window()
browser.get(url)
number=browser.find_element_by_id("u")
psw=browser.find_element_by_id("p")
number.send_keys("")# here is the QQ number
psw.send_keys("")# here is the password

button = browser.find_element_by_id("login_button")
button.click()
time.sleep(100)

clickCharge()
time.sleep(3)
everydayYH()
time.sleep(3)
browser.close()

time.sleep(3)
m.click(1100,518)



