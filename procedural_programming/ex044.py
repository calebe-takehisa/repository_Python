"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-À vista dinheiro/cheque: (10% de desconto)
-À vista no cartão: (5% de desconto)
-Em até 2x no cartão: (Preço normal)
-3x ou mais no cartão: (20% de juros)
SAÍDA:
============ LOJAS WHATEVER ============
Preço das compras: R$XXXX.XX
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção?
Quantas parcelas?

[1], [2]
Sua compra de R$XXXX.XX vai custar R$XXXX.XX no final.

[3], [4]
Sua compra será parcelada em 10x de R$YYY.YY COM JUROS.
Sua compra de R$XXXX.XX vai custar R$XXXX.XX no final.

"""
print('============ LOJAS WHATEVER ============')
while True:
    try:
        price = float(input('Preço das compras: R$'))
        print('FORMAS DE PAGAMENTO\n'
              '[ 1 ] À vista dinheiro/cheque\n'
              '[ 2 ] À vista cartão\n'
              '[ 3 ] 2x no cartão\n'
              '[ 4 ] 3x ou mais no cartão')
        while True:
            option = input('Qual é a opção? ')
            if option == '1' or option == '2' or option == '3' or option == '4':
                if option == '1':
                    final_price = price * 0.9
                    print(f'Sua compra de R${price:.2f} vai custar R${final_price:.2f} no final.')
                    break
                elif option == '2':
                    final_price = price * 0.95
                    print(f'Sua compra de R${price:.2f} vai custar R${final_price:.2f} no final.')
                    break
                elif option == '3':
                    final_installment = price / 2
                    print(f'Sua compra será parcelada em 2x de R${final_installment:.2f} SEM JUROS.')
                    print(f'Sua compra de R${price:.2f} vai custar R${price:.2f} no final.')
                    break
                elif option == '4':
                    while True:
                        try:
                            installment = int(input('Quantas parcelas? '))
                            final_price = price * 1.2
                            final_installment = final_price / installment
                            print(f'Sua compra será parcelada em {installment}x de R${final_installment:.2f} COM JUROS.')
                            print(f'Sua compra de R${price:.2f} vai custar R${final_price:.2f} no final.')
                            break
                        except:
                            continue
                else:
                    continue
            else:
                continue
            break
        break
    except:
        continue