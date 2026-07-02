 #dictionary = a collection of {key:value} pairs
               # ordered and changeable . No duplicates

capitals = {"USA": "Washingtion D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(capitals.values())
# print(capitals.get("China"))  #Japan
# print(capitals.get("Russia"))  #None

# if capitals.get("Japan"):
#     print("That capital exist")
# else:
#     print("That capital does not exist")


capitals.update({"China": "New Delhi"}) # update
capitals.update({"Usa": "Detroit"}) # you can add item with upage function

print(capitals)