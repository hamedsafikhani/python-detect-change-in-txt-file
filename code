import time

sfile = open("YOUR-TEXT-FILE","r")
sreadFile = sfile.readlines()
sfile.close()
currentlen = len(sreadFile)

print(currentlen)


while currentlen >= 0 :

    file = open("YOUR-TEXT-FILE","r")
    readFile = file.readlines()

    # print(len(readFile))
    time.sleep(1)

    if len(readFile) > currentlen :
        currentlen = len(readFile)
        print(readFile[-1])
        file.close()
    elif len(readFile)< currentlen:
        currentlen = len(readFile)
