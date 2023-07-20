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


