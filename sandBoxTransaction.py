import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service('/Users/skywalker/Downloads/chromedriver')

browser = webdriver.Chrome(service=service)



browser.get("https://etherscan.io/tx/0x16bbe22c2af0602b4ab00ae5c6da5a4b5e9cbbfe19a900a204a7380e3e25b248")

with open('./transaction.html', 'w', encoding='utf8') as fp:
    fp.write(browser.page_source)
