import random 

def dice(num):
    '''Returns an int randomly generated between 1, num inclusive'''
    return(random.randint(1,num))

if __name__ == '__main__':
    print("only runs if not imported")