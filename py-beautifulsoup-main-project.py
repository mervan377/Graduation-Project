from cgi import print_directory
from bs4 import BeautifulSoup
import mysql.connector
import requests
from xpath.renderer import to_xpath
from xpath import dsl as x
from lxml import etree
# cursor.execute("CREATE TABLE products2 (id INT AUTO_INCREMENT PRIMARY KEY, product_title VARCHAR(255), product_url VARCHAR(255), crawling_timestamp VARCHAR(255)"
# ", product_brand VARCHAR(255), product_img VARCHAR(255), retailer_name VARCHAR(255), product_data_id  VARCHAR(255), product_avabilty VARCHAR(255), product_price VARCHAR(255))")

cnx = mysql.connector.connect(user='u0528528_userABM', password='TNdp86X7KLut93B',host='94.73.147.224',database='u0528528_ABMGP')
cursor = cnx.cursor()
query = ("INSERT INTO u0528528_abmgp (product_title, product_url, crawling_timestamp, product_brand, product_img, retailer_name, product_data_id, product_avabilty, product_price) "
         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")

webpage = requests.get("https://www.trendyol.com/nike-erkek-yuruyus-ayakkabisi-x-b44-g2-c101429").text
soup = BeautifulSoup(webpage, 'lxml')
dom2 = soup.find_all("div", class_="p-card-wrppr")


print("Selam") 
print("Selam") 
print("Selam") 
print("Selam") 


for dom in dom2:
    product_title = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    product_url = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    crawling_timestamp = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    product_brand = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    product_img = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    retailer_name = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    product_data_id = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    product_avabilty = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    product_price = dom.find('span', class_="prdct-desc-cntnr-ttl").text
    cursor.execute(query, ("product_title", "product_url", "crawling_timestamp", "product_brand" ,"product_img" ,"retailer_name" ,"product_data_id", "product_avabilty" ,"product_price" ))

cnx.commit()
cursor.close()
cnx.close()