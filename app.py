import os
import random
import string

def exibir_nome_do_programa():
    print('Gerador de senha')

def gerar_senha():
    print('')
    QTDdeLETRA =  int(input('Qual a quantidade de Letras: '))
    QTDdeNUMB = int(input('Qual a quantidade de numeros: '))

    numeros_aleatorios = []
    letras_aleatorias = []


    for _ in range(QTDdeNUMB):
        numero = random.randint(0, 9)
        numeros_aleatorios.append(numero)

    for _ in range(QTDdeLETRA):
        letra = random.choice(string.ascii_letters)
        letras_aleatorias.append(letra)

    senha_gerada = numeros_aleatorios + letras_aleatorias
    random.shuffle(senha_gerada)

    senha_gerada_legível = ' '.join(map(str, senha_gerada))

    print(f'A senha gerada aleatoriamente e: {senha_gerada_legível}')

def exibir_opcao():
    print('1. Gerar uma senha aleatoria')
    print('2. Limpa o terminal')
    print('3. Finaliza o app')

def opcao_invalida():
    print('Opcao invalida!')
    voltar_ao_menu_principal()

try:
    def escolher_opcao():
        opcao_escolhida = int(input('Escolha uma opcao: '))
        if opcao_escolhida == 1:
            gerar_senha()
        elif opcao_escolhida == 2:
            limpa_terminal()
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
except:
    opcao_invalida()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def limpa_terminal():
    os.system('cls')
    main()

def finalizar_app():
    print('Finalizar a aplicativo...')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()

if __name__ == '__main__':
    main()