#indexing = accessing elemets of a sequence using [](indexing operator)
#           [start: end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4]) # it will show from 1 to 4
# print(credit_number[5:9])# 5 to 8
# print(credit_number[5:])# 5 to the end
# print(credit_number[-1]) # it will shows last sym
# print(credit_number[::3]) # it shows all numbers to the end but it will count every 3 character

# last_digits = credit_number[-4:]
# print(f'xxxx-xxxx-xxxx-{last_digits}')

# last_name  = credit_number.split('-')[:] # split make string go arrayv '-'-> mean till this 0 key value
# print(last_name[0])

credit_number = credit_number[::-1] # reverse counting
print(credit_number)




