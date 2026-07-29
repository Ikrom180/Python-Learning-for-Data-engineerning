#python file detection

import os

# file_path = 'C:/Users/ikromjon.b/Desktop/Python-Learning/59 60 61 File Handling, File Detection/stuff'
#
# if os.path.exists(file_path):
#     print(f"The location {file_path} exists!")
#
#     if os.path.isfile(file_path):
#         print("That is a file!")
#     elif os.path.isdir(file_path):
#         print("That is a directory!")
#
# else:
#     print(f"The location {file_path} does not exist!")
#


file = 'test.txt'

if os.path.exists(file):
    print('File exists')
    os.remove(file)
elif not os.path.exists(file):
    print('File does not exist')
    #Creating file

    with open(file, 'w') as f:
        f.write('File created')
    print('File created')