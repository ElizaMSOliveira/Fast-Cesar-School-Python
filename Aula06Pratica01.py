
def soma(num1, num2):
    return num1 + num2
def mult(num1, num2):
   return num1 * num2
def sub(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1 / num2


escolha = input('Deseja Usar a Calculadora S ou N').upper()

while escolha == 'S':
    num1 = int(input('Digite o 1° Número: '))
    num2 = int(input('Digite o 2° Número: '))
    calc = input('Escolha +(somar) X(multiplicar, /(dividir) ou -(subtrair)').upper()

    if calc == '+':
       print(soma(num1, num2))
    elif calc == 'x':
        print(mult(num1, num2))
    elif calc == '/':
        print(div(num1, num2))
    elif calc == '-':
        print(sub(num1, num2))
    else:
        print('Opção invalida')

    escolha = input('\n Você deseja fazer mais alguma operação? ').upper()
