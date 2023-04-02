def sumAcumulative(months):
    months_ = months.copy()
    n = len(months)-1
    for i in range(1,n+1):
        months_[n-i] += months_[n-i+1]
    return months_

def posible_k(sumAcumulative):
    n = len(sumAcumulative)
    list_posible_k =[]
    k = int(n/2)
    medium_plus = n-k #cant de elementos que no son todos necesariamente iguales 
 
    for i in range(0,medium_plus):
        if sumAcumulative[medium_plus-i] > 0: #ultimo elemento de los iguales
            list_posible_k.append(k)
        k+=1    
    return list_posible_k
    

def solution(months):
    n = len(months)
    solution = sumAcumulative(months) #Array con la suma acumulativa
    if solution[0] >= 0: # Caso base si la suma de todos los elementos es positiva
        return n
    print(solution) 
    k = int(n/2)
    #medium_plus = n-k #cant de elementos que no son todos necesariamente iguales 
    value = months[n-k]
    list_posible_k = posible_k(solution)
    
    for k in list_posible_k:
        for i in range(0,n-k+1):
            #pos = n-k-i
            if i+k<=n and solution[i] - value*(n-(i+k)) <0:
                break
            if i == n-k:
                return k
            
            #if i+k<=n and solution[pos] - value*(n-(pos+k)) <0:
            #    break
            #elif pos==0:
            #    return k

# months = [-5,-5,-5,-5,21,-5,-5,-5,-5]
# print(solution(months))