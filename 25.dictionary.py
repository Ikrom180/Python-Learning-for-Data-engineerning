 #dictionary = a collection of {key:value} pairs
               # ordered and changeable . No duplicates

capitals = {"USA": "Washingtion D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(capitals.values()) # it will return array

# print(capitals.get("China"))  #Japan
# print(capitals.get("Russia"))  #None

# if capitals.get("Japan"):
#     print("That capital exist")
# else:
#     print("That capital does not exist")


# capitals.update({"China": "New Delhi"}) # update
# capitals.update({"Usa": "Detroit"}) # you can add item with upage function

# capitals.pop("China") # it will remove china key and value
# capitals.popitem() # this will remove last value from dictionary


# keys = capitals.keys() # it will return lists of keys these are iterable
# for key in keys:
#     print(f"{key}: {capitals[key]}")
# print(keys) # dict_keys(['USA',....])

# or we can write like this

#for value in capitals.values(): # This is key
#      print(value)

# capitals.clear()
# print(capitals)

