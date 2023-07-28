def grade(name,hscore,ascore,escore):
    oscore = (hscore + ascore + escore)/175
    
    if oscore <= 0.3:
        ograde = 'Fail'
    elif 0.3 < oscore < 0.75:
        ograde = "Pass"
    elif oscore > 1:
        ograde = "Cheat"
    else:
        ograde = "Distinction"

    return(f"{name} scored {hscore + ascore + escore} our of 175 getting them a {ograde}")
    

# 1. Write a Python function to find the maximum of three numbers.
def maxi(num1,num2,num3):
    return(max(num1,num2,num3))


#2. Write a Python function to sum all the numbers in a list.
def lsum(numlist):
    return(sum(numlist))



#3. Write a Python function to multiply all the numbers in a list.
def lprod(numlist):
    prod = 1
    for i in numlist:
        prod *= i
    return(prod)



#4. Write a Python program to reverse a string.

def rstr(str1):
    return("".join(list(i for i in str1)[::-1]))



#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n >1:
        return(n * factorial(n-1))
    else:
        return(1)



#6. Write a Python function to check whether a number falls within a given range

def nrange(num1,low,high):
    if num1 in range(low,high):
        return True
    return False



#7. Write a Python function that accepts a string and counts the number of upper and lower case letters.

def nuplow(str1):
    up = 0
    low = 0

    for i in str1:
        if i == i.upper() and i == i.lower():
            continue
        elif i == i.upper():
            up += 1
        else:
            low += 1
    return(f"uppercase = {up}, lowercase = {low}")



#8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def dlist(listA):
    return(list(set(listA)))



#9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def isprime(num1):
    for i in range(2,(num1//2)+1):
        if num1%i == 0:
            return("Not Prime")
    return("Prime")


#10. Write a Python program to print the even numbers from a given list.

def evenlist(listA):
    ret_list = []
    for i in listA:
        if i%2 == 0:
            ret_list.append(i)
    return(ret_list)


#11. Write a Python function to check whether a number is "Perfect" or not.

def factor_num(num1):
    factors = []
    for i in range(1,num1):
        if num1%i == 0:
            factors.append(i)
    return factors

def perf_num(num1):
    if num1 == sum(factor_num(num1)):
        return True
    return False


#12. Write a Python function that checks whether a passed string is a palindrome or not.

def ispalin(str1):
    
    str1 = (str1.replace(" ","")).lower()
    for i in range(0,len(str1)//2):
        if str1[i] != str1[-(i+1)]:
            return False
    return True


#13. Write a Python function to check whether a string is a pangram or not.

def pangram(str1):
    alphaset = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    str1 = str1.lower()
    for i in alphaset:
        if not(i in str1):
            return False
    return True
 
#14. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

def hyphensep(str1):
    str1 = str1.lower()
    listA = str1.split("-")
    listA.sort()
    return "-".join(listA)


#15. 16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).

def sqaures30():
    squares = []
    for i in range(1,31):
        squares.append(i**2)
    return(squares)












