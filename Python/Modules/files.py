file = open("teams.txt","w")

for i in range(0,51):
    file.write(f"{str(i**i)}\n")

file.close

file = open("teams.txt","r")
file.readline(1)
file.readline(4)
filelist = file.readlines()
file.close()

filelist[0] = 'I\n'

file = open("teams.txt",'w')
for i in filelist:
    file.write(i)

file.close()


#1. Write a Python program to read an entire text file.
file = open('file1.txt','r')

print(file.readlines())
file.close()

#2. Write a Python program to read first n lines of a file.
file = open('teams.txt','r')

for i in range(int(input("How Many Lines?"))):
    print(file.readline())

file.close()


#3. Write a Python program to append text to a file and display the text.

file = open("teams.txt","a")

file.write('Ha lines go brrrr')

file.close()

file = open("teams.txt","r")

print(file.readlines())

file.close()

#4. Write a Python program to read last n lines of a file.

file = open("teams.txt","r")

filelist = file.readlines()
print(filelist[len(filelist)-int(input("how many lines at the end?")):])

file.close()

#10. Write a Python program to count the frequency of words in a file.

file = open('file1.txt','r')

filelist = file.readlines()

for i in range(len(filelist)):
    filelist[i] = filelist[i].replace("\n","")
    filelist[i] = filelist[i].replace(".","")
    filelist[i] = filelist[i].split(" ")

worddict = {}
for i in filelist:
    for j in i:
        if not(j in worddict):
            worddict[j] = 0
        worddict[j] += 1 

for i in worddict:
    print(f"{i} appears {worddict[i]} times")

