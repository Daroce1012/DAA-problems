# n cantidad de meses de los que es responsable Deborah
# k cantidad de meses consecutivos analizados
# i representa al i_esimo mes

 
import random
import math
from itertools import permutations

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
    for k in range(1,n):    
        for i in range(0,n-k):
            result = sum(months[i:i+k])
            if result < 0: #si k no es valido
                break
            elif i + k >= n-k : #Si llegue al final
                list_k.append(k)
                break
    return list_k  

#Solution recursive de un k primer acercamiento
def solution_recursive(months,list_k,k):
    n = len(months)
    result = math.inf  # max valor positivo    
    for i in range(0,n-k):
        result = min(result,sum(months[i:i+k]))
    if result > 0 :
        return k
    return solution_recursive(months,list_k,k-1)        
    
#Solution recursive de un k segundo acercamiento
def solution_recursive(months,i,k):
    n = len(months)
    if sum(months[i:i+k])  < 0:
        return solution_recursive(months,0,k-1)
    if i + k >= n-k :
        return k        



       
#months = [-5, -4, -6, -5, 21, -5, -5, -5, -5]
months =generate_array(12)
print(months)         
print(solution(months))        

        

