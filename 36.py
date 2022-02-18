casa=float(input('Qual o valor do imóvel desejado? R$'))
salario=float(input('Quanto você recebe mensalmente? R$'))
anos=int(input('Em quantos anos você deseja quitar o imóvel?'))
maximo=salario * 0.3
prestacao=casa / (anos*12)
print('A prestação da casa custará {:.2f} e você pode pagar no máximo {:.2f}'.format(prestacao, maximo))
if prestacao <= maximo:
    print('Você está apto para financiar o imóvel!')
else: 
    print('Infelizmente, você não pode financiar o imóvel.')
