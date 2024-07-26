import os

print('D̲r̲i̲v̲e̲F̲o̲o̲d̲\n')
print('1. Cadastrar restaurante\n2. Listar restaurantes\n3. Ativar restaurante\n4. Sair do app\n')
opcao_escolhida = int(input('Escolha uma opção: '))

def encerrando_apps():
    os.system('cls')
    print('encerrando app\n')

if opcao_escolhida == 1:
    print('Insira as informações abaixo para iniciarmos\n.')
elif opcao_escolhida == 2:
    print('Confira abaixo a listagem dos restaurantes\n')
elif opcao_escolhida == 3:
    print('Insira as informações abaixo para ativarmos seu restaurante\n') 
else: 
    encerrando_apps





