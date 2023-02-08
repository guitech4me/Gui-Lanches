print('1 - Big Mac R$ 10,00 ' )
print('2 - Batata Frita R$ 5,00 ' )
print('3 - Refrigerante R$ 4,00 ')
print('4 - Camisa do Corinthians R$ 250,00 ')

opcao = int(input('Digite o número da opção desejada: '))
quantidade = int(input('Digite a quantidade desejada: '))
nome = input('Digite o nome do jogador que fez o gol do Corinthians no título mundial de 2012: ')

if opcao == 1:
    print('Big Mac sendo preparando para ', nome)
    print('Tempo de espera 15 minutos ')
    total = quantidade * 10
    print('Total R$ ', total)

if opcao == 2:
    print('French Fries sendo preparando para ', nome)
    print('Tempo de espera 5 minutos ')
    total = quantidade * 5
    print('Total R$ ', total)

if opcao == 3:
    print('Refri sendo preparando para ', nome)
    print('Tempo de espera 47 minutos ')
    total = quantidade * 4
    print('Total R$ ', total)

if opcao == 4:
    print('Camisa linda chegando para ', nome)
    print('Tempo de espera 2012 minutos ')
    total = quantidade * 250
    print('Total R$ ', total)


