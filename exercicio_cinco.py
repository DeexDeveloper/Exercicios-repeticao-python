'''
Faça um programa que calcule o número de dias corridos entre duas
datas, para vários pares de datas, considerando a possibilidade de
ocorrência de anos bissextos,sendo que:
• A primeira data é sempre a mais antiga
• O ano é fornecido com 4 dígitos
• A data fornecida com ZERO dias é o sinal para encerrar a entrada
de dados
'''
print("Digite a data nesse formato (00/00/2000).")
print("Para sair do programa digite o dia como 00, exemplo: 00/01/2010.\n")
play = True
while play:
    ini= list(input("Digite a data inicial: "))
    di = (int(ini[0])*10)+int(ini[1])
    mi = (int(ini[3])*10)+int(ini[4])
    ai = int(ini[6])*1000+int(ini[7])*100+int(ini[8])*10+int(ini[9])
    fin= list(input("Digite a data final: "))
    df = (int(fin[0])*10)+int(fin[1])
    mf = (int(fin[3])*10)+int(fin[4])
    af = int(fin[6])*1000+int(fin[7])*100+int(fin[8])*10+int(fin[9])
    if di == 0 or df == 0:
        play = False
        break
    auxmf = 12
    auxdf_31 = 31
    auxdf_30 = 30
    auxdf_29 = 29
    auxdf_28 = 28
    auxmi = mi
    auxdi = di
    dias = 0
    for a in range(ai,af+1):
        bissesto = False
        if a%4==0:
            bissesto = True
            if a%100==0:
                bissesto = False
                if a%400==0:
                    bissesto = True
        if a==af:
            auxmf=mf
        for m in range(auxmi,auxmf+1):
            if a == af and m == mf:
                auxdf_31 = df
                auxdf_30 = df
                auxdf_29 = df
                auxdf_28 = df
            if m in [1,3,5,7,8,10,12]:
                for d in range(auxdi,auxdf_31+1):
                    dias+=1
                auxdi=1
            if m in [4,6,9,11]:
                for d in range(auxdi,auxdf_30+1):
                    dias+=1
                auxdi=1
            if m == 2:
                if bissesto:
                    for d in range(auxdi,auxdf_29+1):
                        dias+=1
                    auxdi=1
                if not bissesto:
                    for d in range(auxdi,auxdf_28+1):
                        dias+=1
                    auxdi=1
        auxmi=1
    print("Existem %d dias entre o intervalo de %d/%d/%d a %d/%d/%d.\n"%(dias-1,di,mi,ai,df,mf,af))
    ini.clear
    fin.clear
