import random
import time
import os

def sortear_numeros():
    verificar = []
    lista_de_n = []
    contador = 0

    while contador < 5:
        numero = random.randint(1, 50)
        lista_de_n.append(numero)
        verificar.append(numero)
        contador = contador + 1

    return lista_de_n, verificar

def verificar_n_repetidos():
    contador = 0
    contador_verificacao = 0

    while contador_verificacao < 4:

        while contador < 5:
                contadorVerificar = 0
                    
                while contadorVerificar < 5:
                        
                    if verificar[contadorVerificar] == lista_de_n[contador]:
                            
                        numero = random.randint(1, 50)
                        lista_de_n[contador] = numero
                        verificar[contadorVerificar] = numero
                            
                    contadorVerificar = contadorVerificar + 1
                            
                contador = contador + 1

        contador = 4
        
        while contador >=0:
            contadorVerificar = 4
            while contadorVerificar < 0:

                    if verificar[contadorVerificar] == lista_de_n[contador]:
                        numero = random.randint(1, 50)
                        lista_de_n[contador] = numero

                    contadorVerificar = contadorVerificar-1

            contador = contador-1

        contador_verificacao = contador_verificacao +1

    return lista_de_n

def verification():
    contador = 0
    resp = []
    print('Agora, digita os números na ordem correta: ')

    while contador < 5:
        print("Digite o" , contador +1 , "° número: " , end="")
        resp_verificar = input()

        while resp_verificar.isalpha():
            print("\nValor inválido!")
            print("Digite novamente: " , end="")
            resp_verificar = input()
        
        while not resp_verificar.isnumeric():
            print("\nValor inválido!")
            print("Digite novamente: " , end="")
            resp_verificar = input()
        resp_verificar = int(resp_verificar)
        resp_verificar = round(resp_verificar,0)

        resp.append(resp_verificar)
        contador = contador +1

    return resp

def verificar_resp():
    contador = 0
    print("\nSua resposta é: " , resp)
    print("E a resposta correta é: " , lista)

    while contador < 5:

        if resp[contador]!=lista[contador]:
            contador = 7
        else:
            contador = contador+1

    if contador == 7:
        print("O computador venceu!")
        
    else:
        print("Você venceu!")

    return contador

pontos_jog  = 0
pontos_compt= 0

os.system("cls")

print('Vou sortear 5 números, e você terá que escrevê-los na ordem correta')
print("Você tem 5 segundos para decorar, então Boa sorte!")
time.sleep(4)

jogar_novamente = 2

while jogar_novamente > 1:
    resposta = 0
    lista_de_n, verificar = sortear_numeros()
    lista = verificar_n_repetidos()
    print(lista)

    time.sleep(5)
    os.system("cls")

    contagem_pontos=0
    resp = verification()
    contador = verificar_resp()

    if contador == 7:
        pontos_compt = pontos_compt +1

    elif contador == 5:
        pontos_jog = pontos_jog +1

    print("\njogador: ",pontos_jog)
    print("computador: ",pontos_compt)

    print("\nVocê quer jogar novamente?")
    resposta_jogador = input().lower()

    while resposta !=1:

        if resposta_jogador == "sim" or resposta_jogador =="s" or resposta_jogador =="nao" or resposta_jogador =="não" or resposta_jogador =="n":
            resposta = 1

        else:
            print("\nNão entendi! Digite novamente: " , end="")
            resposta_jogador = input().lower()

    if resposta_jogador == 'sim' or resposta_jogador == 's':
        jogar_novamente = jogar_novamente + 1
        print("\nOk. Então prepare-se!")
        time.sleep(2)
        os.system("cls")

    else:
        print('Ok, adeus!')
        jogar_novamente = 0
