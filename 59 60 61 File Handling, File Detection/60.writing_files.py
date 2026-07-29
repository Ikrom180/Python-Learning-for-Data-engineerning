# Python writing files (.txt, .json, .csv)
import csv
import json


#Works with csv -> comma seperator value
employees = [['Name','Age','Job'],
             ['Spongebob', 30, 'Cook'],
             ['Patrick', 37, 'Unemployed'],
             ['Sandy', 27, 'Scientist']]

# print(employees[1][1])

file_path = 'employees.csv'

try:
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in employees:
            # print(row)
            writer.writerow(row)
        print(f'json created and wrote successfully')

except FileNotFoundError:
    print('File not found')
except FileExistsError:
    print('File already found')









# #Works with json
# employees = {
#     'name': 'Spongebob',
#     'age': 21,
#     'job': 'cook'
# }
#
# file_path = 'employees.json'
#
# try:
#     with open(file_path, 'w') as f:
#         json.dump(employees, f, indent=4 )
#         print(f'json created and wrote successfully')
#
# except FileNotFoundError:
#     print('File not found')
# except FileExistsError:
#     print('File already found')














# #Works with arr
# employees = ["Eugene", "Squidward", "Spongebob", "Patrick" ]
#
# file_path = 'employees.txt'
#
# try:
#     with open(file_path, 'w') as f:
#         for employee in employees:
#             f.write(employee + ' ')
#         print('File created and wrote successfully')
#
# except FileNotFoundError:
#     print('File not found')
# except FileExistsError:
#     print('File already found')







# text_data = "I like pizza !"
# file_path = "output.txt"
#
# try:
#
#     with open(file=file_path, mode='a') as f:
#         f.write( '\n' + text_data)
#         print(f'File {file_path} created')
#
# except FileExistsError:
#     print("That file already exists")
# except PermissionError:
#     print("Error: Don't have permission to write to this file")
# except OSError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Error: {e}")





