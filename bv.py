from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
import time
import random
import linecache
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
import socket
import requests

def bil_views():
	#随机行
	num = random.randint(1,len(open(r"ua.txt",'rU').readlines()))
	print(str(num))
	ua = str(linecache.getline('ua.txt', num))
	print('user-agent:',ua)
	'''
	num = random.randint(1,len(open(r"url.txt",'rU').readlines()))
	print(str(num))
	url = str(linecache.getline('url.txt', num))
	print('url:',url)
	'''
	with open('url.txt', 'r') as x:
		for line in x:
			url = line.replace('\n', '')
			play(ua,url)
def play(ua,url):
	ip = str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))
	print('X-Forwarded-For:'+ip)
	option=ChromeOptions()
	option.add_argument('--headless')#不启动图形浏览器
	option.add_argument('--no-sandbox')
	option.add_argument('disable-infobars')
	option.add_argument('user-agent='+ua)
	option.add_argument('--window-size=540,960')
	option.add_argument('X-Forwarded-For='+ip)
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
	time.sleep(random.randint(30,75))
	#退出
	#browser.close() # 关闭当前页面
	browser.quit() # 关闭浏览器

bil_views()


#requests.get('https://sc.ftqq.com/你的server酱SCKEY.send?text=哔哩哔哩播放50次完毕')
