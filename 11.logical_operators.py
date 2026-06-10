#logical operators = evaluate multiple conditions (or, and not)
#                    or = at least one condition must be true
#                    and = both conditions must be True
#                    not = inverts the condition (not False, not True)

# temp = 20
# is_raining = True
#
# if temp > 35 or temp < 0 or is_raining:
#     print('Outside cancelled')
# else:
#     print('Outside is still scheduled')

temp = float(input("Enter the temperature: "))


is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside ")
    print("It is sunny ")
elif temp <= 0 and is_sunny:
    print("It is Cold inside ")
    print("It is sunny ")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside ")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot inside ")
    print("It is cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold inside ")
    print("It is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside ")
    print("It is cloudy")