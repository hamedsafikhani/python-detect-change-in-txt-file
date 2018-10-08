


file = open('file1.txt','r').readlines()


for i in range(0,len(file)):
    i
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
