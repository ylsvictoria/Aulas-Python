from datetime import date
atual=date.today().year
nasc=int(input('Digite o ano do seu nascimento: '))
idade=atual-nasc
saldo1=18-idade
saldo2=idade-18
print('Quem nasceu em {} tem {} anos no ano atual'.format(nasc,idade))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    print('Você ainda tem tempo para se alistar. Faltam {} anos para você se alistar. Seu alistamento será em {}'.format(saldo1, atual+saldo1))
else:
    print('Você já deveria ter se alistado há {} anos. Você se alistou em {}.'.format(saldo2, atual-saldo2))
    