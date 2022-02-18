numero=int(input('Digite um número INTEIRO qualquer: '))
base=int(input('Escolha 1 para binário, 2 para octal ou 3 para hexadecimal '))
binario=format (numero,"b")
octal=format (numero,"o")
hexa=format (numero,"x")
if base==1:
    print('Você escolheu BINÁRIO. O número {} em base binário é {}'.format(numero, binario))
elif base==2:
    print('Você escolheu OCTAL. O número {} em base octal é {}'.format(numero, octal))
elif base==3:
    print('Você escolheu HEXADECIMAL. O número {} em base hexadecimal é {}'.format(numero, hexa))
else: 
    print('Volte ao início do programa e escolha um código para saber a base de conversão')