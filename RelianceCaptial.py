import requests 
from bs4 import BeautifulSoup

url="https://www.moneycontrol.com/india/stockpricequote/telecommunications-service/reliancecommunications/RC13"

page=requests.get(url)

soup=BeautifulSoup(page.content,"html.parser")

title = soup.title.string

xyz = soup.find(class_="value_txtfr").get_text().strip() 

print("Market capital of Reliance Communication " +xyz+ "crs")
