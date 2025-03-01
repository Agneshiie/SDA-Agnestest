#LISTS

students = ["student1", "student2", "student3", "student1"]
students.append("student4")
students.insert(1, "student5")
students.remove("student2")
remove_item = students.pop()
position = students.index("student5")
print(students)
print(remove_item)
print(position)

count = students.count("student1")
print(count)

numbers = [4, 7, 12, 92, 3, 22, 30]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

number_length = len(numbers)
print("number lenght ", number_length)

#SETS

my_set = {8, 20, 18, 9, 77, 99, 16}
#my_set = {11, "apple", 5.6, True} #set with different data types
my_set.add(98)
my_set.remove(20)
my_set.discard(77)
print(my_set)

set1 = {34, 87, 45, 17, 14}
set2 = {99, 73, 15, 84, 14}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set.difference(set2)
print(difference_set)
print(intersection_set)
print(union_set)
set1_length = len(set1)
print(set1_length)

#TUPLES

my_tuple = (24, 65, 13, 46, 19, 65, 32, 65)
print(my_tuple[2])
count_65 = my_tuple.count(65)
print(count_65)
index_of_19 = my_tuple.index(19)
print(index_of_19)

length_my_tuple = len(my_tuple)
print(length_my_tuple)

#DICTIONARIES

employee_info = {"name": "Alice", "job_title": "manager", "salary": 5000}
print(employee_info)

salary = employee_info["salary"]
print(salary)

employee_info["location"] = "New York"
employee_info["salary"] = 3000
print(employee_info)

del employee_info["location"]
print(employee_info)

keys = employee_info.keys()
print(keys)

values = employee_info.values()
print(values)

items = employee_info.items()
print(items)

len_employee_info = len(employee_info)
print(len_employee_info)

print("name" in employee_info)
print("address" in employee_info)

print(employee_info.get("name"))
print(employee_info.get("job_title"))

# loops in data structures

colors = ("red", "green", "blue")
for color in colors:
    print(color)

names = ["ilayda", "dmitri", "tiit"]
for name in names:
    print(name)

# sets example

departments = {"HR", "Finance", "Engineering"}
print(departments)

departments.add("Marketing")
print(departments)

departments.remove("Finance")
print(departments)

office1 = {"HR", "Finance", "Marketing"}
office2 = {"Engineering", "Testing", "Business Analyst"}
new_building = office1.union(office2)
print(new_building)

number_of_departments = len(new_building)
print(number_of_departments)

# tuple
# project name, budget, deadline

project = ("Pizza_launch", 2000, "2025-10-02")
print(project)

project_name = project[0]
print(project_name)

projects = ["Pizza_launch", "Pizza_launch", "app launch"]
project_count = projects.count("Pizza_launch")
print(project_count)

name, budget, deadline = project
print(name, budget, deadline)

# lists

employees = ["Alice", "Bob", "Charlie"]
employees.append("David")
employees.insert(0, "Eve")
employees.remove("Bob")
employees.pop()
employees.sort()
employees.reverse()
print(employees)

# Pizza madness task

def string_repeat(number, string):
    return string * number

print(string_repeat(2, "HawaiiPizza"))

def no_space(string):
    return string.replace(" ", "")

print(no_space("Hawaii Pizza"))

def number_to_string(number):
    return str(number)

