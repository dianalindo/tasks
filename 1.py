def remover_duplicados (cadenas):
    no_duplicados = [ ]

    for c in cadenas:
        if c not in no_duplicados:
             no_duplicados.append(c)
       

    return no_duplicados
    


lenguajes = ['Python', 'Java', 'JavaScript', 'Java', 'Java', 'python', 'c++', 'c', 'c++']

print(lenguajes)

resultado = remover_duplicados(lenguajes)

print(resultado)