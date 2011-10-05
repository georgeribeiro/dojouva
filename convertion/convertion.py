
def convert(numero, sistema1, sistema2):
    if sistema1 == "numerico":
        sobra = int(numero) % 5
        inteiro = int(numero) / 5
        return "/" * sobra + "\\" * inteiro
    else:
        i = 0
        for barra in numero:
            if barra == "/":
                i += 1
            else:
                i += 5
              
        return str(i)
        
        
