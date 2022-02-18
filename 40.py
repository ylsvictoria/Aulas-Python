nota1=float(input('Digite a primeira nota do aluno: '))
nota2=float(input('Digite a segunda nota do aluno: '))
media= (nota1 + nota2)/2
if media < 5:
    print('A sua média foi {} e infelizmente você foi REPROVADO'.format(media))
elif media >= 5 and media <7:
    print('A sua média foi {} e você está na RECUPERAÇÃO.'.format(media)) 
else:
    print('A sua média foi {}. Parabéns, você foi APROVADO POR MÉDIA!'.format(media))