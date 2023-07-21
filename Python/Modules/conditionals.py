mark = int(input("Please input a mark between 0 and 100"))


if mark > 100:
    print("Some cheatery is afoot")
elif mark > 85:
    print("Distiction")
elif 65 <= mark <= 85:
    print("Pass")
else:
    print("Fail")


if mark > 85:
    print("Distiction")
if 65 <= mark <= 85:
    print("Pass")
if mark > 100:
    print("Some cheatery is afoot")
if mark < 65:
    print("Fail")