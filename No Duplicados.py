def longitud (total: str) -> str:
    letras = len(total)
    cofre = set()
    inicio1 = inicio2 = 0
    resultado = ""

    while inicio2 < letras:
        if total[inicio2] not in cofre:
            cofre.add(total[inicio2])
            inicio2 += 1
            if len(cofre) > len(resultado):
                resultado = total[inicio1:inicio2]
        else:
            cofre.remove(total[inicio1])
            inicio1 += 1

    return resultado
cadena = "aaaaaaaaaaaaaaaafaaafaaafaaafaaafaaafaaafaafaafafaaaaaaaaaaaaaazqlñaaaaaaaaaaaaaaaaaa"
resultado = longitud(cadena)
print(resultado)