class student:
    def __init__(self,age,group,name='student'):
        self.name = name
        self.age = age
        self.group = group

    def avg_score(self,scr1,scr2,scr3):
        print(f"{self.name} scored {(scr1+scr2+scr3)//3}")
    
athena = student(22,'AMS - Awesomely Masterful Students','Athena')
athena.avg_score(1,1133,135)
