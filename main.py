import requests
from bs4 import BeautifulSoup
from sender import send_email
#set variabile iniziale
lat=None
#set connection headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
#get response
def response(url="https://www.ecodelchisone.it/sezioni/val-pellice"):
  response=requests.get(url,headers=headers)
  if response.status_code == 200:
    print("pagina ottenuta")
    return(response)
  else:
    print("Error", response.status_code)
#get data from csv
def get_lat():
  with open("data.csv","r") as split_data:
    lines=split_data.readlines()
    for line in lines:
      return(line.split(","))
#update data from csv with new latest
def updata(lat,em):
  with open("data.csv","r+") as split_data:
    split_data.truncate()
    split_data.close()
    with open("data.csv","w+") as split_data:
      lines=split_data.readlines()
      for line in lines:
        split_data.write(line)
      split_data.write(f"{em},{lat}")
#loop for latest article
email,latest=get_lat()

while True:
  soup=BeautifulSoup(response().content, "html.parser")
  latest_article=soup.find("div", class_="views-row views-row-1 views-row-odd views-row-first")
  link="https://www.ecodelchisone.it"+latest_article.find("a").get("href")
  if(link!=latest):
    print("new article")
    latest=link
    send_email(link,email)
    updata(link,email)
  print(link)
  break