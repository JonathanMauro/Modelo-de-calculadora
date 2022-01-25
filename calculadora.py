def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return(valor)
        except ValueError:
            pass

n1=converte_numero(input('Digite o primeiro valor: '))
n2=converte_numero(input('Digite o segundo valor: '))
opçao = 0
while opçao !=5:
    print('''Escolha uma das bases para conversão:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa''')
    opçao = int(input('Sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}'.format(n1,n2,soma))
    elif opçao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))

    elif opçao == 4:
        print('Informe os números novamente')
        n1=int(input('Digite o primeiro valor: '))
        n2=int(input('Digite o segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente..')
    print('=-=' * 10)
print('Fim do programa. Volte sempre!')