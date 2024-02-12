import random
import time
import os

print('-'*30)
print('SEJA BEM-VINDO A PARTIDA DE JOKENPO')
print('-'*30)

def jokenpo_decisao(cpu, escolha):
    if cpu == 'pedra' and escolha == 'papel':
        print('-'*30)
        print(f'VOCÊ VENCEU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')
    if cpu == 'pedra' and escolha == 'tesoura':
        print('-'*30)
        print(f'VOCÊ PERDEU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')
    if cpu == 'pedra' and escolha == 'pedra':
        print('-'*30)
        print(f'EMPATOU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')

    if cpu == 'papel' and escolha == 'pedra':
        print('-'*30)
        print(f'PERDEU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')
    if cpu == 'papel' and escolha == 'tesoura':
        print('-'*30)
        print(f'VENCEU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')
    if cpu == 'papel' and escolha == 'papel':
        print('-'*30)
        print(f'EMPATOU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')

    if cpu == 'tesoura' and escolha == 'pedra':
        print('-'*30)
        print(f'VENCEU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')
    if cpu == 'tesoura' and escolha == 'tesoura':
        print('-'*30)
        print(f'EMPATOU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')
    if cpu == 'tesoura' and escolha == 'papel':
        print('-'*30)
        print(f'PERDEU !!! {nome} escolheu {escolha} e o CPU escolheu {cpu}')

nome = str(input('Digite seu nome: '))
print('-'*30)
print(f'{nome} vs CPU')

while True:
    print('INICIANDO PARTIDA DE JOKENPO')
    print('-'*30)

    jokenpo = ['pedra', 'papel', 'tesoura']
    cpu = random.choice(jokenpo)
    escolha = str(input('Faça sua escolha: pedra | papel | tesoura -> ')).lower().strip()
    if escolha not in jokenpo:
        print('-'*30)
        print('Escolha inválida ou digitada de forma incorreta, o programa será encerrado...')
        time.sleep(1)
        break

    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO')
    time.sleep(1)
    jokenpo_decisao(cpu, escolha)

    resposta = str(input('Deseja jogar novamente? (s/n): ')).strip().lower()[0]
    if resposta == 'n':
        print('-'*30)
        print('Encerrando...')
        time.sleep(1)
        break
    elif resposta == 's':
        os.system('cls')
    else:
        print('Digitou incorretamente, o programa será encerrado...')
        time.sleep(1)
        break
