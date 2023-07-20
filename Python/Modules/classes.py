class student:
    def __init__(self,name,age,group):
        self.name = name
        self.age = age
        self.group = group

    def avg_score(self,scr1,scr2,scr3):
        print(f"{self.name} scored {(scr1+scr2+scr3)//3}")
    
athena = student('Athena',22,'AMS - Awesomely Masterful Students')
athena.avg_score(1,1133,135)
