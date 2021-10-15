import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

url = "https://www.acfic.org.cn/zt_home/2020qglh/2020qglh_qlta/index.html"

response = requests.get(url, verify=False)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')

table_for_link = soup.find('div', class_="gu-diCon")




for tr in table_for_link.find_all("li"):
    final = []
    final.append(tr.text)
    final.append("https://www.acfic.org.cn/zt_home/2020qglh/2020qglh_qlta" + tr.a["href"].lstrip('.'))
    try:
        response1 = requests.get("https://www.acfic.org.cn/zt_home/2020qglh/2020qglh_qlta" + tr.a["href"].lstrip('.'), verify=False)
        response1.encoding = response1.apparent_encoding
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        text = soup1.find("div", class_="TRS_Editor")
        final.append(text.text)
        print(final)
        Result = pd.DataFrame([final])
        Result.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\acfic\Result.csv", mode='a', index=False, header=None,
                      encoding="utf-8_sig")
    except Exception as e:
        print(e)
        pass
