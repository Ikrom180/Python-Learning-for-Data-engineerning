import math
import math as t


friends = 5

# addition

friends = friends + 1
friends += 1
print(friends)

# subtraction

friends = friends -2
friends -= 2
print(friends)

# multiplication

friends = friends * 3
friends *= 3
print(friends)

# division

friends = friends / 2
friends /= 2
print(friends)

# exponentiation

friends = friends ** 2
friends **= 2
print(friends)

# modules

remainder = friends % 3
print(remainder)



# Math Funcitions
x = 3.4
y = 4
z = 5

# result = round(x)  #0.5 -> will 1 and  04 <- 0
# result = pow(x, y)
# result = max(x,y,z)
# result = min(x,y,z)

# print(result)



# Math lib

# x = 9.9

# print(t.pi)
# print(t.e)
# result = t.sqrt(x)
# result = math.ceil(x) #ceil will up number and round number form
# result = t.floor(x) #floor will down number and round it

# print(result)



#Finding circumference

# radius = float(input('Enter a radius: '))
# circumference = 2 * t.pi * radius
# print(f'The circumference is: {circumference}')


#Finding Area

# radius = float(input('Enter the radius: '))
# area = t.pi * pow(radius, 2)

# print(f"The area of the circle is {round(area)}")


#Finding Hypotenuse

a = float(input('Enter a number: '))
b = float(input('Enter a number: '))

c = t.sqrt(pow(a,2) + pow(b,2))
print(f'The hypotenuse is {c}.')





























