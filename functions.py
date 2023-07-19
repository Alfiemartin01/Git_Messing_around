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
    
print(grade("Athena",12,27,60))


# 1. Write a Python function to find the maximum of three numbers.
def maxi(num1,num2,num3):
    return(max(num1,num2,num3))

print(maxi(1,4.7,4.5))

#2. Write a Python function to sum all the numbers in a list.
def lsum(numlist):
    return(sum(numlist))

print(lsum([1,2,3,4,5]))

#3. Write a Python function to multiply all the numbers in a list.
def lprod(numlist):
    prod = 1
    for i in numlist:
        prod *= i
    return(prod)

print(lprod([1,4,8]))

#4. Write a Python program to reverse a string.

def rstr(str1):
    return("".join(list(i for i in str1)[::-1]))

print(rstr('Hello_World'))

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n >1:
        return(n * factorial(n-1))
    else:
        return(1)

print(factorial(5))

#6. Write a Python function to check whether a number falls within a given range

def nrange(num1,low,high):
    if num1 in range(low,high):
        return True
    return False

print(nrange(10,3,7))

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

print(nuplow("Hello World....."))





