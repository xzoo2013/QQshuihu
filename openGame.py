#!/usr/bin/env python

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
def openGame():
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
    print "click time:",'........',time.ctime()

    time.sleep(100)
    browser.close()
    time.sleep(3)
    m.click(1100,518)

openGame()




