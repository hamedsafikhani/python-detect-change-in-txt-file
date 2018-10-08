


file = open('file1.txt','r').readlines()


i = len(file) - 1
print(file[i])



filebk = open('backup.txt','r')

if file[i] == filebk.readline():
    print("Not changed")

else:
    print("Changed")



filebk.close()
filebk = open('backup.txt','w')
filebk.write(file[i] )
filebk.close()
