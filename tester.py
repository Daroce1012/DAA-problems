# n cantidad de meses de los que es responsable Deborah
# k cantidad de meses consecutivos analizados
# i representa al i_esimo mes

 
import random
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

# first solution
def solution(months):
    n = len(months)
   
    mean = int(n/2)
    if n%2 !=0: #Si es impar el n\'umero de meses
        mean+=1
   
    k=1
    if months[mean+1]<0:
        k = mean
        
    index = 0
    while k<n:
        
        result = sum(months[index:index+k])
        index +=1
       
        if result < 0: #si k no es valido
            k+=1
            index = 0

            
        elif index + k > n-1 : #Si llegue al final
            return k




months = [-10, 3, -10, 9, -10, 6, 6, 6, 6]

#months =generate_array(12)
print(months)         
print(solution(months))        

        

