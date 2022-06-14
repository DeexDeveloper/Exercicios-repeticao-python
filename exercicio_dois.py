'''
Um número inteiro é considerado triangular se este for o produto de 3
números inteiros consecutivos, como, por exemplo, 120 = 4 x 5 x 6.
Elabore um programa que,após ler um número n do teclado,verifique se
N é triangular.
'''
n = int(input("Digite um número para saber se ele é triangular: "))
t = False
for i in range(1,n):
    triangular = i*(i+1)*(i+2)
    if triangular == n:
        print("O %d é triangular, pois %d x %d x %d = %d."%(n,i,i+1,i+2,n))
        t = True
if not t:
    print("%d não é um número triangular!"%n)
