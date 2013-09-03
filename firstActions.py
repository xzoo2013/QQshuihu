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
   
##########################
def clickShengChenGang():#生辰纲
    m.click(835,228)

def clickPrize():#奖励
    m.click(1104,226)

#####
### on the top left
def clickJingMai():
    m.click(389,400)

def clickMine():
    m.click(398,371)

def clickWuJiang():
    m.click(398,351)

def clickRefresh():
    m.click(398,324)
### 主建筑
def clickXiuLianGuan():#修炼馆
    m.click(810,751)
    
def clickDianJiangTai():#点将台    
    m.click(841,552)
    
def clickZhaoXianGuan():#招贤馆
    m.click(669,657)
    
def clickTieJiangPu():#铁匠铺
    m.click(966,601)
    
def clickZhaiXingLou():# 摘星楼
    m.click(1112,391)
    
def clickJiShi():#集市
    m.click(1143,514)

def clickNongChang():#农场
    m.click(946,398)
    
### the ones on the right bottom
#猎魂
def clickLieHun():
    m.click(1156,756)
#征战   
def clickZhengZhan():
    m.click(925,729)

#布阵
def clickBuZhen():
    m.click(1060,731)
    
#回家
def goBack():
    m.click(925,718)

####################### 主操作
##每日团战
def mcsTuan():
    for i in range(3):
        m.click(1128,277)#开始团战
        time.sleep(5)
        for j in range(4):
            m.click(1052,489)#快速加入
            time.sleep(0.5)
        time.sleep(5)
        m.click(1201,725)#结束
        time.sleep(5)
        m.click(892,649)#关闭
    m.click(1118,296)#关闭

def hmsTuan():
    for i in range(4):
        m.click(1092,392)#开始团战
        time.sleep(5)
        for j in range(5):
            m.click(1058,502)#快速加入
            time.sleep(0.5)
        time.sleep(5)
        m.click(1201,725)#结束
        time.sleep(5)
        m.click(892,649)#关闭
    m.click(1118,296)#关闭

def ygxTuan():
    for i in range(5):
        m.click(502,590)#开始团战
        time.sleep(5)
        for j in range(9):
            m.click(1058,502)#快速加入
            time.sleep(0.5)
        time.sleep(5)
        m.click(1201,725)#结束
        time.sleep(5)
        m.click(892,649)#关闭
    m.click(1118,296)#关闭


def everydayZZ():
    clickZhengZhan()
    time.sleep(15)
    ygxTuan()#阳谷县
    time.sleep(5)
    m.click(831,692)
    time.sleep(5)
    hmsTuan()#黄门山
    time.sleep(5)
    m.click(870,697)
    time.sleep(5)
    mcsTuan()#芒常山
    time.sleep(5)
    m.click(768,697)#回黄门山
    time.sleep(5)
    m.click(749,703)#回阳谷县
    time.sleep(5)
    goBack()
##############################################

## 领取奖励
def getPrize():
    clickPrize()
    time.sleep(5)
    m.click(951,322)#在线好礼
    time.sleep(8)
    m.click(1016,331)#演武奖励
    time.sleep(8)
    loginPrize()
    time.sleep(2)
    m.click(1237,600)
    
def loginPrize():
    m.click(1078,307)
    time.sleep(6)
    for j in range(3):
      m.click(924,512)#center
      time.sleep(6)
    m.click(1112,296)#关闭
##每日摘星楼
def everydayZX():
    clickZhaiXingLou()
    time.sleep(8)
    m.click(1080,542)#重置
    time.sleep(8)
    m.click(765,552)#确定
    time.sleep(3)
    m.click(997,537)#自动挑战
    time.sleep(2)
    m.click(899,598)#开始
    time.sleep(15)
    m.click(919,599)
    time.sleep(3)
    m.click(1150,287)#关闭

## 每日修炼
def everydayXL():
    clickXiuLianGuan()
    time.sleep(24)
    for i in range(5):
        m.click((399+(i+1)*90),680)
        time.sleep(3)
        m.click(794,630)
    m.click(857,683)#修炼第六人
    time.sleep(3)
    m.click(754,560)#确定
    time.sleep(3) 
    m.click(805,641)#开始修炼
    time.sleep(5)
    m.click(796,731)#返回家园
## 每日运货
def everydayYH():
    clickShengChenGang()
    time.sleep(20)
    m.click(1027,613)#开始运货
    time.sleep(8)
    m.click(788,736)#回家
 ## 每日农场
def everyNC():
    clickNongChang()

## 每日征收
def clickChargePopup():
    m.click(745,443)
    
def clickCharge():
    time.sleep(5)
    m.click(1165,233)
    time.sleep(5)
    for i in xrange(10):
        clickChargePopup()
        time.sleep(2)
    m.click(948,368)#关闭
## 每日挑战
def everydayTZ():
    for k in range(2):
        clickBuZhen()#布阵
        time.sleep(10)
        m.press(778,577)#按住天授
        time.sleep(2)
        m.move(588,459)#移动
        time.sleep(2)
        m.release(588,459)#释放
        time.sleep(2)
        m.move(1234,333)#点边缘陌生
        time.sleep(1)
        m.click(1035,351)#点陌生
        time.sleep(2)
        m.click(1248,269)#点刷新
        time.sleep(2)
        m.press(590,464)#点天授
        time.sleep(2)
        m.move(778,577)#上阵
        time.sleep(2)
        m.release(778,577)
        time.sleep(2)
        m.move(1234,333)#点边缘陌生
        
        
        for i in range(10):
            time.sleep(3)
            m.click(1239,(319+i*34))
        time.sleep(15)
        m.click(1202,717)#结束战斗
        time.sleep(5)
        m.click(888,647)#关闭

        m.click(1112,282)#关闭
        time.sleep(2)
    
#### 打开游戏窗口   
url="http://ui.ptlogin2.qq.com/cgi-bin/login?link_target=blank&daid=153&appid=614008604&hide_title_bar=1&s_url=http://game.108.qq.com/logined.html&target=self&qtarget=self&css=http://imgcache.qq.com/ptcss/qqsh/614008604/login.css&runtime=1305272225684"
browser = webdriver.Firefox() # Get local session of firefox
browser.maximize_window()
browser.get(url)
number=browser.find_element_by_id("u")
psw=browser.find_element_by_id("p")
number.send_keys("") # here is the QQ number
psw.send_keys("") # here is the password

button = browser.find_element_by_id("login_button")
button.click()

time.sleep(80)
###### 开始行动
clickCharge() #征收 n
time.sleep(5)

getPrize()    #奖励 n
time.sleep(5)

everydayZZ()  #征战 
time.sleep(5)

everydayZX()  #摘星
time.sleep(5)

everydayYH()  #运货 n
time.sleep(5)

everydayTZ()  #挑战陌生人 
time.sleep(5)

everydayXL()  #修炼

browser.close()#关闭窗口

time.sleep(3)
m.click(1100,518)

