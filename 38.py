num1=int(input('Digite aqui o primeiro número: '))
num2=int(input('Digite aqui o segundo número: '))
if num1>num2:
    print('O primeiro valor é maior. O número {} é MAIOR que o número {}'.format(num1, num2))
elif num2>num1:
    print('O segundo valor é maior. O número {} é MAIOR que o número {}'.format(num2, num1))
elif num1==num2:
    print('Não existe valor maior. Os dois valores são iguais. {} = {}'.format(num1, num2))