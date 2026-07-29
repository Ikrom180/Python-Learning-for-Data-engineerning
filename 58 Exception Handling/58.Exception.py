# Exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except 3.finally


# 1 / 0   -> Zero devision error
# 1 + '1' -> TypeError
# int('pizza') -> ValueError

# #scelton is stand always like that
# try:
#     #Try some code
# except Exception:
#     #Handle an Exception
# finally:
#     #Do some clean up

try:
    number = int(input("Enter a number: "))
    print( 1 / number )
    print("Hello")

except ZeroDivisionError:
    print("You can't divide by zero IDIOT !")
except ValueError:
    print("Enter only numers please")
except Exception:
    print("Something went wrong !")
finally:
    print("Goodbye")