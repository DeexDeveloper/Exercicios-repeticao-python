'''
Faça um programa que leia dois valores x e y, e calcula o valor de x
dividido por y, além do resto da divisão. Não é permitido usar as
operações de divisão e resto de divisão do Python (use apenas soma e
subtração).
'''
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
soma = vz = 0
if x>y:
    while soma <=x:
        soma+=y
        vz+=1
    if soma > x:
        soma-=y
        vz-=1
    resto = x-soma
    print("A divisão de %d por %d é %d e o seu resto é %d."%(x,y,vz,resto))
else:
    print("O valor de X tem que ser maior que Y.")
