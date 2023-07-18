i=5
while i > 0:  
    i-=1
    print(f"{str(input('Please Enter a name'))} is awesome!")

#Loops and prints numbers from 10 to 21 with a step of 2.
for i in range(10, 21, 2):
    print(i)
#output: 10 12 14 16 18 20    


### w3resources ###

# 1. Write a Python program to find those numbers 
# which are divisible by 7 and multiples of 5, 
# between 1500 and 2700 (both included).
fands = []
for i in range(1500,2701):
    if i%5 == 0 and i%7 == 0:
        fands.append(str(i))
print(", ".join(fands))

#2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Expected Output :
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius

temp = str(input("Please give a temp with either f or c depending"))

if temp[-1] == 'f':
    conv_temp = (float(temp[0:-2])-32)* (5/9)
    print(f"{temp} is converted to {conv_temp}c")
elif temp[-1] == 'c':
    conv_temp = (float(temp[0:-2]) * (9/5)) + 32
    print(f"{temp} is converted to {conv_temp}f")
else:
    print('follow the instructions!')

#3. Write a Python program to guess a number between 1 and 9.

import random as r
num = r.randint(1,10)
while int(input("Please Guess a number")) != num:
    print("Try Again!")
print("Well Guessed!")


#4. Write a Python program to construct the following pattern, using a nested for loop.
pmid = []
for i in range(1,int(input("Give me an integer"))+1):
    pmid.append('*'*i)
print("\n".join(pmid) + "\n" + "\n".join(pmid[len(pmid)-1:0:-1]) + "\n*")

#5. Write a Python program that accepts a word from the user and reverses it.

print(list(i for i in str(input("Give a word")))[::-1])

#6. Write a Python program to count the number of even and odd numbers in a series of numbers
odd = 0
even = 0
nums = (1,2,3,4,5,6,7,8,9)
for i in nums:
    if i%2 == 0:
        even+=1
    else:
        odd+=1
print(f"odd = {odd} , even = {even}")

#7. Write a Python program that prints each item and its corresponding type from the following list.
junk = [1,"a",[12,43]]
junk_still = []
for i in junk:
    print(f'{i} has type: {type(i)}')

