# k --- Cantidad de Cursos
# m --- Array de_ Propuestas matriz de (m x k)

def test_problem():
    
    m = [[1,2],[2,4,],[4,5]]
    return problem(m)

def problem(m):
    k = len(m[0])
    days = mark_matrix(max_matrix(k,m))
    proposals = []
    return func_proposals(m,k,days,proposals) 
    
def func_proposals(m,k,days,proposals):
    if len(proposals) == k:
        return proposals
    for prop in m:
        proposals.append(prop)
        if not_contain(days,prop) and func_proposals(m,k,mark(days,prop),proposals):
            return proposals
        proposals.remove(prop)   
            
def mark(days, proposal):
    days_ = days
    for p in proposal:
        days_[p] = True
    return days_

def not_contain(days,prop):
    for i in prop:
        if days[i]:
            return False
    return True

def max_matrix(k,m):
    max = -1
    for i in range(len(m)):
        for j in range(k):
            if m[i][j]> max:
                max = m[i][j]   
    return max            
                
def mark_matrix(max):
    list = []
    for i in range(0,max+1):
        list.append(False)
    return list                  


print(test_problem())

