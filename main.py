import os

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
    with open('file1.txt') as fp: 
        data = fp.read() 

# result_path = 'Results'

# print("Saving... file to "+result_path)
# with open(result_path, 'a+') as f:
#     f.write(str(files))
