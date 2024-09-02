import string
import random

def create_random_name():
    rand = random.randint(1, 10)

    letters = ''.join(random.choice(string.ascii_letters) for _ in range(rand))

    num = random.randint(0,999)
    
    name = f"{letters}{num}".lower()
    
    return name
