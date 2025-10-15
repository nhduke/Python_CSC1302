
newfile = open(r'D:\DEV\Python_CSC1302\practice\sample.txt', 'r+')
print(newfile.read())
newfile.write('Is this the first line?\n')
newfile.write('should be the second line')

newfile.seek(0)
print(newfile.read())
