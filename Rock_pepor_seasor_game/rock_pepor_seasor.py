# a simple rock pepor seasor Game : 
from colorama import Fore 
import random 

def Rock_pepor_seasor( p1 : str  , p2:str): 
        if p1== p2 : 
                return Fore.CYAN, 'tie'
        elif p1 == 'rock ' and p2 == 'seasor': 
                return Fore.GREEN , "you ",'win ' 
        
        elif p1 ==' seasor' and p2 == 'rock ': 
                return Fore.RED , 'computer ' ,  'win ' ,  'you losse '
        elif p1 == 'peper' and p2 == 'rock   ': 
                return Fore.GREEN , "you ",'win ' 
        
        elif p1 == 'rock' and p2 == 'peper' : 
                return Fore.RED , "you ",'loose  ', 'computer win : ' 
        elif p1 == 'seasor' and p2 == 'peper  ': 
                return Fore.GREEN , "you ",'win ' 
        elif p1 == 'peper ' and p2 == 'seasor ': 
                return Fore.RED  , "you ",'loose  ', 'computer win ' 
        else : 
                print('invalid input : ')

if __name__ == "__main__ ": 
        p1= str(input('enter your move  , 1.rock \n 2. peper \n 3. seasor '))
        a= ['rock ', 'peper','seasor ']
        p2= random.choices(a)
        print(Rock_pepor_seasor(p1, p2 ))
                