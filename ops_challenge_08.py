#!/usr/bin/env python3

# Author: Jamie Giannini

# Objectives: Create a Python script that includes the following:
# [X] Assign to a variable a list of ten string elements.
# [X] Print the fourth element of the list.
# [X] Print the sixth through tenth element of the list.
# [X] Change the value of the seventh element to “onion”.
# Extra:
# [X] Use Python methods against your list to manipulate the elements in your list.
# [X] Include Tupple and Dictionary

# List items are ordered, changeable, and allow duplicate values. Ordered means the items have a defined order, and that order will not change.
# Any new items added to a list get added to the end of the list. 
# List items can be of any data type: string, int, bool

carList = ["Porsche", "Jaguar", "Mercedes", "Lotus", "Nissan", "Audi", "Subaru", "Lexus", "Ferrari", "Lamborghini"]
mayTheFourthBeWithYou=carList[4] 
print("The 4th element is:", mayTheFourthBeWithYou) #Prints 4th element
print("\n")

sixToTen=carList[5:10] #Prints sixth through 10th element
print("The 6th-10th items in the list are:", sixToTen)
print("\n")

changedValue=carList[6]="Onion" #Change 7th element of the list
print("The changed value is:", changedValue)
print("New list is:")
print(carList) #Print changed list
print("\n")

### Append ###
print("APPEND")
carList.append("Ford") #Adds an element on to the end of the list
print(carList)
print("\n")

### Clear ###
print("CLEAR")
fruitList = ["Pineapple", "Mango", "Strawberry"]
print(fruitList)
fruitList.clear() #Clears the list array
print("Now the list looks like this: ")
print(fruitList)
print("\n")

#### Copy ###
print("COPY")
print("Copied List: ")
newCarList=carList.copy() #Copies original list (does not include any changes we made to the original list)
print(newCarList)
print("\n")

### Count ###
print("COUNT")
carType="Audi"
print(f"{carType} appears this many times in the list:", carList.count(carType)) #Counts number of times an element appears in a list
print("\n")

### Extend ###
print("EXTEND")
countries = ["New Zealand", "Italy"]
countries_add = ["Spain", "Japan"]

countries.extend(countries_add) #appending countries_add elements to countries
print("Countries I want to visit:", countries) #prints the appended list
print("\n")

### Index ###
print("INDEX")
#Returns the index of the specified element in the list
index=carList.index("Audi",0, 9)
print("The index of Audi is:", index)
print("\n")

### Insert ###
print("INSERT")
carList.insert(2,"Mazda") #Inserts a new element at the specified position and shifts everything in the list over to the right
print(carList)
print("\n")

### Pop ###
print("POP")
pop_out=carList.pop(0)#Removes the item at the given index from the list and returns the removed item
print("The popped item in the 0 index is:" , pop_out)
print("\n")

### Remove ###
print("REMOVE")
print("Remove Lotus:")
carList.remove("Lotus")
print(carList)
print("\n")

### Reverse ### 
print("REVERSE")
carList.reverse()
print("Reversed list:", carList)
print("\n")

### Sort ###
print("SORT")
carList.sort() #Sorts in alphabetical order for strings / ascending order
print("Sorted list ascending order: ", carList)
carList.sort(reverse=True)
print("Sorted list descending order: ", carList)
print("\n")

### TUPLE ###
#A tuple is a collection that is ordered and unchangeable. They can contain items with the same value though.
print("TUPLE")
myTuple = ("Linux", "Windows", "Mac", "Raspberry Pi")
print(myTuple)
print("\n")

### DICTIONARY ###
# Dictionaries are used to store data values in key:value pairs. A dictionary is a collection that is ordered, changeable and does not allow duplicates.
print("DICTIONARY")
stormtrooperData =	{
    "title": "Stormtrooper",
    "nickname": "Bucketheads",
    "leader": "Darth Vader",
    "weapon": "E-11 blaster"
}
print(stormtrooperData)
print("Weapon type is", stormtrooperData["weapon"]) #Prints a selection from our dictionary
print("\n")


