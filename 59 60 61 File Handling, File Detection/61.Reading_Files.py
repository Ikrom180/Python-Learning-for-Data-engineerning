# Python reading files (.txt, .json, .csv)
import csv
import fileinput
import json

file = 'stuff/employees.csv'


#This is for csv file
# In csv we have to iterate all over the date to get
try:
    with open(file, 'r') as f:
        content = csv.reader(f)
        for row in content:
            # print(row)
            for item in row:
                print(item, end=' ')

            print()
except FileNotFoundError:
    print(f'File not found')
except PermissionError:
    print(f'You can not access this file :{file}')
except AttributeError:
    print(f'File not found')


#This is for json file
# try:
#     with open(file, 'r') as f:
#         content = json.load(f)
#         print(content) #content['job'], name', 'age'
# except FileNotFoundError:
#     print(f'File not found')
# except PermissionError:
#     print(f'You can not access this file :{file}')
# except AttributeError:
#     print(f'File not found')


#This is for txt file
# try:
#     with open(file, 'r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print(f'File not found')
# except PermissionError:
#     print(f'You can not access this file :{file}')