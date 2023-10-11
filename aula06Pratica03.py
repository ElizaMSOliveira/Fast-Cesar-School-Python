def media(num1, num2):
    result = (num1 + num2) / 2
    return result


def status(result):
    if result > 6:
        return 'Aprovado'
    elif 4 <= result <= 6:
        return 'Veriricaçao Suplementar'
    else:
        return 'Reprovado'


num1 = int(input('Digite o 1° Numero'))
num2 = int(input('Digite o 2° Numero'))

resultado = media(num1, num2)
print(status(resultado))
