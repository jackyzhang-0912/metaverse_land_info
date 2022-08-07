import requests

url = "https://www.investing.com/crypto/ethereum/eth-usd-historical-data"

response = requests.get(url).text

# print(response.text)

with open('./test.html', 'w', encoding='utf8') as fp:
    fp.write(response)