# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. No duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster


# fruit = "apple"
# fruits = ["apple", "banana", "sherry", "eoconut"]
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-1])

# print(dir(fruits)) # it will show what function it can
# print(help(fruits)) # it will shows all of the functions with description
# print(type(fruits))
# print("apple" in fruits) # it will return boolean
# print("pineapple" in fruits)
# print(len(fruits))

# adding or changing list value
# fruits[0] = "pineapple"
# fruits[1] = "orange"
# fruits[4] = "orange" #it will return error bc we do not have 4 index
# fruits.append("pineapple") # add to list value
# fruits.remove("apple") # remove apple
# fruits.insert(0, "cococooo")

# ***********************************************************
# in order to reverse anpha 1 reverse alpfa then reverse it
# fruits.sort() #  sort like a alpha
# fruits.reverse() # reverve based on list order

# ***********************************************************
# fruits.clear() # remove all oh the value
# print(fruits.index("apple")) finding index looking by value
# print(fruits.count("apple")) # it will show how many values has in one list


# for x in fruits:
#     print(x , end=" ")


#SET

# fruits = {"apple", "banana", "sherry", "coconut"}

# we can`t find values with searching indexes
# print(fruits)
# fruits.add("pinapple")
# fruits.remove("apple")
# fruits.pop() # pop will remove last element of array
# print(help(fruits))
# print(fruits)
# print(dir(fruits))
# print(fruits)

# print(fruits[0]) # it will return error
# for fruit in fruits:
#     print(fruit)




#Tuple
# fruits = ("apple", "banana", "sherry", "coconut")
# print(fruits[0])





fruits = ("apple", "orange", "banana", "coconut")


print(dir(fruits))
# ✅ Access elements (reading is fine)
print(fruits[0])           # "apple"
print(fruits[-1])          # "coconut"

# ✅ Slicing (creates a NEW tuple)
new_tuple = fruits[1:3]    # ("orange", "banana")

# ✅ Check if something exists
if "apple" in fruits:
    print("Yes!")

# ✅ Count occurrences
print(fruits.count("coconut"))  # 2

# ✅ Find index
print(fruits.index("banana"))   # 2

# ✅ Loop through it
for fruit in fruits:
    print(fruit)














