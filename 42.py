a=float(input('Digite o primeiro segmento: '))
b=float(input('Digite o segundo segmento: '))
c=float(input('Digite o terceiro segmento: '))
if a<b+c and b<a+c and c<a+b:
    print('Esses segmentos podem formar um triângulo ',end='')
    if a==b==c:
        print('do tipo EQUILÁTERO.')
    elif a==b or a==c or b==c:
        print('do tipo ISÓSCELES.')
    else:
        print('do tipo ESCALENO.')
else:
    print('Esses segmentos NÃO formam um triângulo.')
