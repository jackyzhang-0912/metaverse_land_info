import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service('/Users/skywalker/Downloads/chromedriver')

browser = webdriver.Chrome(service=service)



browser.get("https://opensea.io/collection/sandbox/activity")

with open('./test.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)

# print(browser.page_source)