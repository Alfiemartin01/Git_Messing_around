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

