import math

import random

greeting = "Good morning!   "
print(len(greeting))

age = 25
text = "I am " + str(age) + " years old."
print(text)

text = "python Programming"
print(text.upper())

text = "HELLO PYTHON"
print(text.lower())

text = "learning python is fun"
print(text.capitalize())

sentence = "an apple a day keeps the doctor away"
print(sentence.find("doctor"))
print(sentence.replace("apple", "banana"))

city = "Paris"
country = "France"
message = "I visited {} in {}".format(city, country)
print(message)

#additional string methods

greeting = "good morning everyone!"
print(greeting.startswith("good"))
print(greeting.endswith("!"))

title = "   python programming built in features  "
print(title.strip())
print(title.lstrip())
print(title.rstrip())

colors = "red, blue, green, yellow"
color_list = colors.split(",")
print(color_list)

words = ["coding", "is", "awesome"]
sentences = "-".join(words)
print(sentence)

#number-related built-in features in python

print(abs(-5))

print(round(3.681288, 2))

print(min(3, 7, 14, 92, 1, 11))

print(max(3, 7, 14, 92, 1, 11))

#Returns x raised to the power y. Equivalent to x**y
print(pow(2, 5))

#Sum funktsioon vajab nurksulge 
print(sum([3, 7, 14, 92, 1, 11]))

#Converts a number or string x to an integer. base specifies the base if x is a string
print(int('10'))

#Converts a number or string x to a floating-point number

print(float(3))

print(float('3.14'))

#math module functions
#import math

print(math.floor(3.7))

print(math.ceil(5.7))

print(math.sqrt(16))

#Calculates the logarithm of x to the specified base which is optional and equal to e by default, ie. natural logarithm
print(math.log(188, 10))

#Calculates the exponential of x (e^x)
print(math.exp(2))

print(math.sin(math.pi / 2))

#Et random funktsiooni kasutada peame importima library - import random
print(random.random())

print(random.randint(15, 75))

#listist suvalise elemendi valimine

my_list_loomad = ["elevant", "kaelkirjak", "pingviin", "oppossum", "zebra"]
random.choice(my_list_loomad)
print(my_list_loomad)

my_list_2 = [6, 7, 12, 35, 2, 90]
random.choice(my_list_2)
print(my_list_2)

my_list_loomad = ["elevant", "kaelkirjak", "pingviin", "oppossum", "zebra"]
random.shuffle(my_list_loomad)
print(my_list_loomad)

#data structure built ins examples

#abs value

temperature = -5
print(abs(temperature))

#tahan teada palju mul 3 aasta pärast on kui investeerin 100 eurot (intressimääraga 2%)
#leiame lõppsumma

investment = 100
interest_rate = 0.02
years = 3
final_amount = investment * pow(1 + interest_rate, years)
print(final_amount)

#math ceil

people = 7 
pizza_needed = math.ceil(people / 3)
print(pizza_needed)

people = 7 
pizza_needed = math.ceil(people * 1.5)
print(pizza_needed)

# math sqrt 

area = 16
side_length = math.sqrt(area)
print(side_length)

#random module function
#flippin coini ja kontrollin kas see on alla või üle 0,5

flip = random.random()
print(flip)
if flip > 0.5: 
    print("heads")
else:
    print("tails")

# kui mängin lauamängu täringuga ja veeretan suvalist numbrit

dice_roll = random.randint(1,6)
print(dice_roll)

url = "https://www.eesti.ee"
domain = url.find(".ee")
print(domain)

error_message ="404 not found"
fixed_message = error_message.replace("404", "500")
print(fixed_message)

email = "agnes.hiie@gmail.com "
print(email.strip())

addresses = "Baker street, Sunset blvrd; 18 Kastani tänav"
addresses_list = addresses.split(";")
print(addresses_list)