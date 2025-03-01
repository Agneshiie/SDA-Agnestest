import math

shop_fruits = {
    "apples": 2,
    "watermelons": 4,
    "bananas": 6
}

print(shop_fruits["watermelons"])
print(shop_fruits.get("watermelons"))

# print(shop_fruits["abcd"])
print(shop_fruits.get("abcd"))

products = [
    {"id": 1, "name": "chocolate", "quantity": 5},
    {"id": 2, "name": "popcorn", "quantity":10},
    {"id": 3, "name": "peanut butter", "quantity": 20},
]

print(products[1]['quantity'])
print(products[1]['name'])

#set 

clothes = {"t-shirt", "trousers", "skirt"}
is_present = "skirt" in clothes
print(is_present)

'''Kommentaar'''
'''Elementide lisamine seti'''

clothes.add("hat")
print(clothes)

clothes.add("pants")
print(clothes)

clothes.add("socks")
print(clothes)

'''Elementide eemaldamine setist'''

clothes.remove("trousers")
print(clothes)

'''Uuendan listi'''

clothes.update(["jeans", "dress"])
print(clothes)

'''Tuple with nested dictionaries/Tuple tegemine'''
'''ID-d pole siin tegelikult vajalikud. Need on näiteks andmebaaside jaoks'''

animals = ("lion", "dog", "cat")
print(animals[1])

products = (
    {"id": 1, "name": "chocolate", "quantity": 5},
    {"id": 2, "name": "popcorn", "quantity":10},
    {"id": 3, "name": "peanut butter", "quantity": 20},
)
print(products[2]["quantity"]
      )

'''
Ex1
Create variables
1. variable for checking if user is active ir not
2. Your favorite phrase from the book/film etc
3. Number of people in the house
4. How much the dinner cost
'''

#1
active = True #that means that user is active (boolean)
#2
phrase = "i'm an angel of chaos" #string
phrase2 = "hasta la vista baby"
#3
number_of_people = 5 #integer
#4
dinner_price = 20.5 #float

print(active, phrase, phrase2, number_of_people, dinner_price)

'''
Ex2
Calculate the area of triangle
Peame looma variabled, mis näitavad b ja h väärtuseid
'''

areas = []

#loon dictionary
areas_dict = {
    "kolmnurk": 0, "ringi pildala": 0, "teine variant": 0, "trapeze": 0
}

#kolmnurk
b = 10
h = 6
area = 0.5 * b *h
print(area)
areas.append(area)
areas_dict["kolmnurk"] = area

#ringi pildala
#esimene variant
pi = 3.14
r = 4
area = pi * (r ** 2)
print(area)
areas.append(area)
areas_dict["ringi pindala"] = area

#teine variant (import math algusesse)
area = math.pi * math.pow(r, 2)
print(area)
areas.append(area)

#trapeze
a = 10
b = 5
h =3
area = 0.5 * (a + b) * h
print(area)
areas.append(area)
areas_dict["trapeze"] = area

print(areas)

'''Task: Data around python
https://journey.study/v2/learn/courses/11152/modules/35352/units/0/SOLO/66552'''

#1
title_1 = "The catcher in the rye"
print(title_1)

author_1 = "J.D. Salinger"
print(author_1)

year_1 =1951
print(year_1)

is_newer_than_2000_1 = year_1 > 2000
print(is_newer_than_2000_1)

characters_1 = ["Holden Caulfield", "Phoebe Caulfiend"]
print(characters_1)

#2
title_2 = "Harry Potter and the Sorcerer's Stone"
print(title_2)

author_2 = "J.K. Rowling"
print(author_2)

year_2 =2001
print(year_2)

is_newer_than_2000_2 = year_2 > 2000
print(is_newer_than_2000_2)

characters_2 = ["Daniel Radcliffe", "Emma Watson"]
print(characters_2)

'''
Teeme minekirja, mis sisaldab viite lemmikfilmi
'''

favourite_books = [
{"title":title_1, "author":author_1, "year":year_1, "is_newer_than_2000":is_newer_than_2000_1, "year":year_1, "characters":characters_1},
{"title":title_2, "author":author_2, "year":year_2, "is_newer_than_2000":is_newer_than_2000_2, "year":year_2, "characters":characters_2}
]
print(favourite_books[0]["title"])



