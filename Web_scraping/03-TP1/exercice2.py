import requests
from bs4 import BeautifulSoup
import html5lib

url1 = "https://www.dominos.fr/la-carte-pizza/bacon-groovy-pbcg"
url2 = "https://www.dominos.fr/la-carte-pizza/pepperoni-party-pppa"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1'
}
data1=requests.get(url1, headers=headers)
data2=requests.get(url2, headers=headers)

Soup1 = BeautifulSoup(data1.content, 'html5lib')
Soup2 = BeautifulSoup(data2.content, 'html5lib')

print("\n")
print("LES PIZZAS DOMINOS\n")

ingredient1 = Soup1.find('p', itemprop='description').text
print("Pizza Bacon Groovy \nles ingrédients :")
print(ingredient1)

element1 = Soup1.find('li', id='size-Taille Medium Classique').find('a')
kcal1_text = element1['onclick'].split(', ')[1]
kcal1_int = int(''.join(filter(str.isdigit, kcal1_text)))
print(f"Energie (Kcal) : {kcal1_int}")

print("\n")

ingredient2 = Soup2.find('p', itemprop='description').text
print("Pizza Pepperoni Party \nles ingrédients :")
print(ingredient2)

element2 = Soup2.find('li', id='size-Taille Medium Classique').find('a')
kcal2_text = element2['onclick'].split(', ')[1]
kcal2_int = int(''.join(filter(str.isdigit, kcal2_text)))
print(f"Energie (Kcal) : {kcal2_int}")

print("\n")

pizzas={"Pizza Bacon Groovy":kcal1_int, "Pizza Pepperoni Party":kcal2_int}
print("La pizza la moins calorique est :")
if pizzas["Pizza Bacon Groovy"] < pizzas["Pizza Pepperoni Party"] :
    print(list(pizzas.keys())[0])
else :
    print(list(pizzas.keys())[1])

print("\n")