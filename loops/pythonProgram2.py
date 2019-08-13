
fh1 = open("file1.txt", 'w+')

prod = 1
for i in range(1,6):
    prod=prod*i

fh1.write("The factorial is %d" % prod)

fh1 = open("file1.txt", 'r')
fh2 = open("file2.txt",'w+')

if fh1.mode == 'r':
    line = fh1.read()
    fh2.write(line)

fh2.close()
