def remover_duplicados (cadenas):
    no_duplicados = [ ]

    for c in cadenas:
        if c not in no_duplicados:
             no_duplicados.append(c)
       

    return no_duplicados
    


lenguajes = ['a','b','c','d','e','a','g','h','i','b','b','c','c','h',]

print(lenguajes)

resultado = remover_duplicados(lenguajes)

print(resultado)