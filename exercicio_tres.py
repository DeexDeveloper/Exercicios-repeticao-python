'''
Elabore um programa que leia n valores e mostre a soma de seus
quadrados.         
'''
rodar = True
lista=[]
while rodar:
    n = int(input("\nDigite o valor de n: "))
    lista.append(n)
    rodar = int(input("0 - Não / 1 - Sim\nDeseja inserir mais um número?: "))
for i in lista:
    print("A soma dos quadrados de %d é %d."%(i,i**2+i**2))
