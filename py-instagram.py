from email import charset
import mysql.connector
import requests
from lxml import html
import datetime
import json 

url = 'https://www.instagram.com/mervan37/followers/'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'sec-ch-ua-platform': 'macOS',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
res = requests.get(url, headers=header)
dom = html.fromstring(res.content.decode(encoding='utf-8'))

print(dom)