
#integer variable
apples_amount = 10

print (apples_amount)
print(apples_amount, type(apples_amount))

#boolean variable 
adult = True
print(adult)
print(adult, type(adult))

#float variable
pi = 3.14# . not , !!!

print(pi)

#string variable
name = "Agnes"
print(name, type(name))

"""
variable "2" (it is a string because it is inside quotes)
variable2 = 2 (integer) ARE NOT THE SAME
"""
string1 = "Agnes"
string2 = "hiie"

#1
number1 = 3
number2 = 5
print(number1+number2)

#2
number1 = 3
number2 = 5
print(number1+number2) # "35"

#3
number1 = "3"
number2 = "5"
print(number1+number2)

#collection

#list
names = ["esimene", "teine", "kolmas" , "neljas"]
print(names)

#we will use indexes
print(names[1]) #teine

names.append("viies")
print(names)

"set"
"unordered and unique"
animals = {"cat", "dog", "rabgit"}
print(animals)
animals.add('cow')
print(animals)

#dictionary
person_info = {"name":"Agnes", "eyes_color":"green", "sda_student":3, "student":True}
print(person_info)
print(person_info["eyes_color"])
print(person_info["name"])

person_info["hair_color"] = "brown"
print(person_info)