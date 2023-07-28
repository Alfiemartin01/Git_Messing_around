class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __add__(self,other) -> object:
        if self.width == other.width:
            return Rectangle(self.width, self.height + other.height)
        elif self.height == other.height:
            return Rectangle(self.width + other.width, self.height)
        else:
            print("Please input 2 valid rectangles with matching heights or widths")        
    
    def _str__(self) -> str:
        ascii = []
        for height in range(self.height):
            ascii.append('\n')
            for width in range(self.width):
                if (height == 0) or (height == self.height - 1):
                    ascii.append('-')
                elif (width == 0) or (width == self.width -1):
                    ascii.append('|')
                else: 
                    ascii.append(' ')
        return("".join(ascii))

    

    def __eq__(self, other) -> bool:
        if(self.height == other.width and other.height == self.width)or(self.height == other.height and self.width == other.width): 
            return True
        return False
    
    def __gt__(self,other) -> bool:
        if self.width *self.height > other.width * other.height:
            return True
        return False

    def __le__(self,other) -> bool:
        return not (self > other)
    
    def __ge__(self,other) -> bool:
        if self == other or self > other:
            return True
        return False
    
    def __lt__(self,other) -> bool:
        return not(self >= other)

r1 = Rectangle(10,3)
print(srt(r1))
