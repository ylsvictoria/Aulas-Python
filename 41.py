from datetime import date
print('Seja bem vindo(a)! Vamos descobrir a sua categoria para o campeonato.')
ano=int(input('Qual o seu ano de nascimento: '))
atual= date.today().year
idade=atual-ano
if idade <= 9:
    print('Você tem {} anos. Você está na categoria MIRIM'.format(idade))
elif idade >9 and idade <= 14:
    print('Você tem {} anos. Você está na categoria INFANTIL'.format(idade))
elif idade >14 and idade <= 19:
    print('Você tem {} anos. Você está na categoria JÚNIOR'.format(idade))
elif idade >19 and idade <=25:
    print('Você tem {} anos. Você está na categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos. Você está na categoria MASTER'.format(idade))