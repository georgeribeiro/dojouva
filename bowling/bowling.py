
def bowling(lista):
    soma = 0
    somarodada = 0
    spare=0
    
    for i in xrange(len(lista)):
        if spare:
            soma += lista[i][0]
            
        soma += lista[i][0] + lista[i][1]
        if  lista[i][0] + lista[i][1] == 10:
            if i == len(lista) - 1:
                soma += lista[i][2]
            spare = 1
        else:
            spare = 0
 
    return soma
