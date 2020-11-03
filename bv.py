from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
import time
import random
import linecache
from selenium.webdriver.common.action_chains import ActionChains
from threading import Timer
import os
import sys
import socket
import _thread


#随机身份
def random_1():
	num = random.randint(1,106)
	ua = str(linecache.getline('ua.txt', num))
	print('user-agent:',ua)
	num = random.randint(1,24)
	url = str(linecache.getline('url.txt', num))
	print('url:',url)
	bil_views(ua,url)

def bil_views(ua,url):
	ip = str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))
	print('X-Forwarded-For:'+ip)
	option=ChromeOptions()
	option.add_argument('--headless')#不启动图形浏览器
	option.add_argument('disable-infobars')
	option.add_argument('disable-infobars')
	option.add_argument('user-agent='+ua)
	option.add_argument('--window-size=540,960')
	option.add_argument('wup_version=3.0')
	option.add_argument('X-Forwarded-For='+ip)
	option.add_argument('sdkVer=3.1.0')
	option.add_argument('bundleId=tv.danmaku.bili')
	option.add_argument('proId=900028525')
	option.add_argument('A37=WIFI')
	option.add_argument('A38=WIFI')
	option.add_argument("--mute-audio")
	option.add_experimental_option('excludeSwitches', ['enable-automation'])#防检测
	option.add_experimental_option('useAutomationExtension', False)#防检测
	
	# 代码
	browser = Chrome(options=option)
	browser.delete_all_cookies()
	#防检测
	browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
	Object.defineProperty(navigator, 'webdriver', {
	  get: () => undefined
	})
  """
})
	# 访问网页
	
	browser.get(url)
	time.sleep(5)
	ActionChains(browser).move_by_offset(260, 210).click().perform()
	print('播放成功')
	time.sleep(31)
	#退出
	#browser.close() # 关闭当前页面
	browser.quit() # 关闭浏览器
	

n=1
print('开始执行第： '+str(n)+'  次播放')
n=n+1
random_1()
print('播放完毕，1~3秒后重启浏览器线程')
