peso=float(input('Informe o seu peso em KG: '))
altura=float(input('Informe a sua altura em metros: '))
imc= peso / (altura**2)
print('Este é o seu ÍNDICE DE MASSA CORPÓREA(IMC): {:.1f}'.format(imc))
if imc < 18.5:
    print('De acordo com o seu IMC, você está ABAIXO DO PESO')
elif imc > 18.5 and imc < 25:
    print('De acordo com o seu IMC, você está no peso IDEAL')
elif imc>=25 and imc < 30:
    print('De acordo com o seu IMC, você está SOBREPESO')
elif imc >=30 and imc < 40:
    print('De acordo com o seu IMC, você está com OBESIDADE')
else:
    print('De acordo com o seu IMC, você está com OBESIDADE MÓRBIDA')