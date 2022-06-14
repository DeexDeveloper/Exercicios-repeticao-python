'''
Escreva um programa que imprime na tela os n primeiros números
perfeitos. Um número perfeito é aquele que é igual à soma dos seus
divisores.Por exemplo,6=1+2+3.
'''
n = int(input("Digite o intervalo desejado: "))
for i in range(1,n+1):
    soma=0
    for x in range(1,i):
        if i%x==0:
            soma+=x
    if soma == i:
        print(i)
