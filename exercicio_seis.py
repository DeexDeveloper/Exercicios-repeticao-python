'''
Foi realizada uma pesquisa em Niterói, com um número desconhecido de 
pessoas. De cada entrevistado foram colhidos os seguintes dados:  
1. Qual  o  seu  clube  de  futebol  de  preferência  (1  –  Flamengo, 2  –  Vasco, 3 – Fluminense, 4 – Botafogo, 5 – Outros) 
2. Qual o seu salário 
3. Qual a sua cidade natal (1 – Niterói, 2 – Outra)  
Escreva um programa que informe: 
• Número de torcedores por clube 
• Média salarial dos torcedores de cada time
• Número  de  pessoas  nascidas  em  Niterói  e  que  não  torcem  para nenhum dos principais clubes do Rio 
• Número de pessoas entrevistadas
'''

total = []
entrevistado = []
num = 1
outros = 0
somasal = []
torcedores = []
while num == 1:
    clube = int(input("(1  –  Flamengo, 2  –  Vasco, 3 – Fluminense, 4 – Botafogo, 5 – Outros)\nQual  o  seu  clube  de  futebol  de  preferência: "))
    salario = float(input("Digite o seu salário: "))
    cidade = int(input("(1 – Niterói, 2 – Outra)\nQual a sua cidade natal: ")) 
    entrevistado = [clube,salario,cidade]
    total.append(entrevistado)
    if cidade==1 and clube==5:
        outros+=1
    num = int(input("(1 Sim e 0 Não)\nVocê deseja entrevistar mais alguém?: "))
for i in range(1,6):
    somatorce = soma=0
    for x in total:
        if x[0]==i:
            soma+=x[1]
            somatorce+=1
    somasal.append(soma)
    torcedores.append(somatorce)
print("Existem %d Flamenguistas, %d Vascainos, %d Fluminenses, %d Botafoguenses e %d outros times"%(torcedores[0],torcedores[1],torcedores[2],torcedores[3],torcedores[4]))
if somasal[0]>0:
    print("A média salarial dos torcedores do Flamengo é de %.2f"%(somasal[0]/torcedores[0]))
if somasal[1]>0:
    print("A média salarial dos torcedores do Vasco é de %.2f"%(somasal[1]/torcedores[1]))
if somasal[2]>0:
    print("A média salarial dos torcedores do Fluminense é de %.2f"%(somasal[2]/torcedores[2]))
if somasal[3]>0:
    print("A média salarial dos torcedores do Botafogo é de %.2f"%(somasal[3]/torcedores[3]))
if somasal[4]>0:
    print("A média salarial dos torcedores de outro times é de %.2f"%(somasal[4]/torcedores[4]))
print("Existem %d pessoas nascidas em Niterói que torcem para outros times fora do Rio"%outros)
print("Para essa pesquisa, foram entrevistadas %d pessoas."%len(total))
