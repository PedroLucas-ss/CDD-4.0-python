lista_compras =['banana','laranja','maçã']
for i in lista_compras:
    print(i)
print(1)
lista_compras.append('carro')
for i in lista_compras:
    print(i)
print(2)
lista_compras.insert(1,'carro')
for i in lista_compras:
    print(i)
print(3)
del lista_compras[3]
for i in lista_compras:
    print(i)
print(4)
item = lista_compras.pop(-1)
print(item)
print(5)
for i in lista_compras:
    print(i)
