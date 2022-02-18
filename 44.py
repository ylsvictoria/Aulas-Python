preco=float(input('Informe o preço do produto R$'))
tipo=int(input('Escolha: 1 para à vista dinheiro/cheque. 2 à vista cartão, 3 para 2x no cartão e 4 para mais parcelas no cartão:'))
if tipo==1:
    precofinal=preco-(preco*0.1)
    print('Você recebeu 10% de desconto. O produto era R${:.2f} e agora será R${:.2f}.'.format(preco, precofinal))
elif tipo==2:
    precofinal=preco-(preco*0.05)
    print('Você recebeu 5% de desconto. O produto era R${:.2f} e agora será R${:.2f}.'.format(preco, precofinal))
elif tipo==3:
    print('Nesta opção não há desconto. Preço final será será R${:.2f}.'.format(preco))
elif tipo==4:
    precofinal=preco+(preco*0.2)
    print('Esse formato de pagamento há juros de 20%. O produto era R${:.2f} e agora será R${:.2f}.'.format(preco, precofinal))
else:
    print('Código não reconhecido. Tente novamente.')
