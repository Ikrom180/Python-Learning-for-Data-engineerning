#variable scope = where variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# 1) it will lookup local variable
# 2) enclosed
# 3) Global
# 4) Built_ini



# def func1():
#     a = 1 # -> local variable
#     print(a)
#
#
# def func2():
#     b = 2 # -> local variable
#     print(b)
#
# #They can't see each other  like func2() does not print inside func1() variable a
# func1()
# func2()

# def happy_birthday(name, age):
#     print(f"Happy Birthday dear {name}")
#     print(f'You are{age} years old')
#
# def main():
#     name = "Bro"
#     age = 21
#     happy_birthday(name, age)
#
# main()


# def func1():
#     x = 1 #-> Enclosed variable
#
#     def func2():
#         print(x)
#     func2()
#
# func1()

# 1) it will lookup local variable
# 2) enclosed
# 3) Global
# 4) Built_ini




# GLOBAL
# x = 3
#
# def func1():
#     print(x)
#
# def func2():
#     print(x)
#
# func1()
# func2()



x = 3

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()
















