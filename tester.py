# n cantidad de meses de los que es responsable Deborah
# k cantidad de meses consecutivos analizados
# i representa al i_esimo mes

 
import random
import math
from itertools import permutations
from colorama import Cursor, init, Fore

from solution import *

def generate_array(n): 
    mean = int(n/2)
    if n%2 !=0: #Si es impar el n\'umero de meses
        mean+=1
    mean_value = random.randrange(-100,100)
    
    months = []
    for i in range(0,n):
        value = random.randrange(-100,100)
        if i >= mean:
            months.append(mean_value)
        else:
            months.append(value)
            
    return months

def is_correct_solution(k,list_k):
    if list_k.count(k):
        return True
    return False
    
# test solution
def test_solution(months):
    n = len(months)
    list_k = []
    for k in range(1,n+1):  
        for i in range(0,n-k+1):
            result = sum(months[i:i+k])
            if result < 0: #si k no es valido
                break
            elif i + k >= n:
                list_k.append(k)
                break
    return list_k  


for i in range(1, 1000):
    print("***************************************************")
    print("CASO DE PRUEBA")
    print(i)
    months =generate_array(12)
    print(months)
    print("Solucion de fuerza bruta")
    result1 = test_solution(months)     
    print(result1) 
    print("Solucion optima")
    result2 = solution(months)
    print(result2)  

    if len(result1) == 0 and result2 == 0:
        print( Fore.GREEN  + "CORRECT ")
    elif len(result1) == 0 or result2 == 0:
        print(Fore.RED + "INCORRECT")
    else:
        print( Fore.GREEN  + "CORRECT ")
    print("**************************************************")  

        

