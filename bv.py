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
	num = random.randint(1,106)
	ua = str(linecache.getline('ua.txt', num))
	print('user-agent:',ua)
	num = random.randint(1,24)
	url = str(linecache.getline('url.txt', num))
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
	time.sleep(31)
	#退出
	#browser.close() # 关闭当前页面
	browser.quit() # 关闭浏览器

bil_views()


#requests.get('https://sc.ftqq.com/SCU121122T1cc8d68fe0566217f16362970e6a55875f98d59eab0e3.send?text=哔哩哔哩播放50次完毕')
