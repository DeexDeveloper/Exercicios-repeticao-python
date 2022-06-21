'''
Faça um programa que simula uma calculadora que aceita as seguintes
operações: soma, subtração, divisão e multiplicação. O programa inicia
pedindo para o usuário escolher uma opção do menu
• Somar
• Subtrair
• Dividir
• Multiplicar
• Sair
Ao escolher a opção, o programa solicita os dois números a serem
operados (exceto se a opção escolhida for a 5), efetua a operação, mostra
o resultado na tela e volta para o menu para que o usuário escolha outra
opção.
'''
n = 0
while n != 5:
    print("\nExemplos: a+b, a-b, a*b e a/b\n")
    n = int(input("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair\nEscolha uma das opções: "))
    if n != 5 :
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        if n == 1:
            print("\nA soma de a + b é %.2f"%(a+b))
        if n == 2:
            print("\nA subtração de a - b é %.2f."%(a-b))
        if n == 3:
            print("\nA multiplicação de a x b é %.2f."%(a*b))
        if n == 4:
            print("\nA divisão de a/b é %.2f."%(a/b))   
