from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests

"""options = webdriver.ChromeOptions()
options.add_argument("--incognito")"""

# Giving the path of Chrome Driver
chromedriver = "/home/santuk/Desktop/python/chromedriver"
# browser = webdriver.Chrome(chromedriver, options=options)

# starting the browser
browser = webdriver.Chrome(chromedriver)
ur = input("Enter the Flaticon url: ")

html_doc = requests.get(ur)
page = html_doc.content
soup = BeautifulSoup(page, 'html.parser')

soup = BeautifulSoup(str(soup.find("body")),'html.parser')
data = soup.select("div.overlay")

for i in range(1,len(data)):
	""" if i%10==0:
		browser.quit()
		browser = webdriver.Chrome(chromedriver, chrome_options=options) """
	browser.get(data[i].a["href"])
	button = browser.find_element_by_css_selector("#download > a")
	ActionChains(browser).move_to_element(button).click().perform()
	download_button = browser.find_element_by_css_selector("#download-free > b")
	ActionChains(browser).move_to_element(download_button).click().perform()



