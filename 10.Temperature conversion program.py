unit = input("Is this temperature is Celsius or Farenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C" or unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'The temperature in Farenheit is {temp}F')
elif unit == "F" or unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f'The temperature in Celsius is {temp}C')
else:
    print(f'The unit {unit} is not valid')