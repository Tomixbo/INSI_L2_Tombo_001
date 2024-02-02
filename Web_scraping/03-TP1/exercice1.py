import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://www.dominos.fr/la-carte/nos-pizzas"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1'
}
data=requests.get(url, headers=headers)

Soup = BeautifulSoup(data.content, 'html5lib')

menu_entries=Soup.find_all('span', class_='menu-entry')

print("\n")
print("LES PIZZAS DOMINOS\n")

print("La liste des pizzas dans le menu :\n")

menu_list=[]
for entry in menu_entries:
    if not "Menu" in entry.text :
        menu_list.append(entry.text)

for m in menu_list:
    print(m)

print("\n")