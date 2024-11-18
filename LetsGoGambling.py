
import random as r

def gambling():

    Win = False
    random_number = r.randint(1, 10)
    
    if random_number == 7:
        Win=True
    
    return Win

gambling()