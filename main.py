import os
import string

path = '/home/cadbury/Documents/Intern/JPMC/projectReferences/avtar-test/SignFiles'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        # if '.sigml' in file:
            # print(os.path.splitext(file)[0])
            # files.append(os.path.splitext(file)[0])
        files.append(file)

files.sort()
# for i in range(len(files)):
#     print(files[i])

print(len(files))

data = []

for i in range(len(files)):
    with open('SignFiles/'+files[0]) as fp: 
        d = fp.read() 
        data.append(d.translate({ord(c): None for c in string.whitespace}))

print(type(data))

# print(data)

with open('Results.txt', mode='wt', encoding='utf-8') as myfile:
    # for lines in text:
    for i in range(len(data)):
        print('<?xml version="1.0" encoding="utf-8"?>'+data[i], file = myfile)
myfile.close


# result_path = 'Results'

# print("Saving... file to "+result_path)
# with open(result_path, 'a+') as f:
#     f.write(str(files))
