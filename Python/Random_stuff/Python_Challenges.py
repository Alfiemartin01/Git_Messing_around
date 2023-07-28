#Times Table Grid
def Times_Table_Grid(n):
    str_grid = ""
    for i in range(1,n+1):
        for j in range(1,n+1):
            str_grid += (f"{str(i*j)}\t")
        str_grid += "\n"
    return(str_grid)

print(Times_Table_Grid(int(input("Give me an integer"))))

#Factorial
def Factorial(n):
    if n >1:
        return(n * Factorial(n-1))
    else:
        return(1)

print(Factorial(int(input("Give me another integer"))))

#Cohort List
team = ["Alfie","Akber","Alexander","Corvus","Farah","Farhana","Hawa","James","James","Kes","Mitchell","Pamela","Roberto","Ruben","Thomas","Wojciech"]
team.append("Leon")
print(team)
print(team[4])
print(team.count("Chris"))

#Rectangle Class
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return(self.width * self.height)

r1 = Rectangle(3,4)
print(f"Area = {str(r1.area())}")

#Seven not Five
snf = []
for i in range(2000,3201):
    if (i%7 == 0) and (i%5 != 0):
        snf.append(str(i))
print(", ".join(snf))

