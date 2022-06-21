'''
O quadrado de um numero natural n é dado pela soma dos n primeiros
números impares consecutivos. Por exemplo, 12=1, 22=1+3, 32=1+3+5,
42=1+3+5+7, etc. Escreva um programa que dado um número n, calcule
seu quadrado usando a soma de ímpares ao invés de produto.
'''
n = int(input("Digite o valor de n: "))
raiz = 0
aux = 1
for i in range(1,n+1):
    raiz+=aux
    aux+=2
print("A raiz quadrada de %d é %d."%(n,raiz))
