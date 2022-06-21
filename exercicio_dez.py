'''
1Generalize o exercício anterior, de forma que ele calcule e mostre na tela
os quadrados de todos os números naturais menores que 1000, usando o
método da soma de ímpares.
'''
for n in range(1,1001):
    raiz = 0
    aux = 1
    for i in range(1,n+1):
        raiz+=aux
        aux+=2
    print("A raiz quadrada de %d é %d."%(n,raiz))
