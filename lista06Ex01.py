"""Faça um programa que receba um valor em horas e dê
 duas opções ao usuário, converter em minutos ou em segundos.
  A partir da escolha do usuário, o programa deverá chamar a
  função específica de conversão. A função para converter horas
  em minutos deverá receber como parâmetro a hora e retornar o
  valor em minutos. A função para converter horas em segundos
  deverá receber como parâmetro a hora e retornar o valor em
  segundos. Por fim, o programa principal imprime o valor retornado pela função. """

def hora_em_minutos(hora):
    minutos = hora * 60
    return minutos
def hora_em_segundos(hora):
    segundos = hora * 3600
    return segundos


hora = int(input('Digite a hora'))
decisao = input('Deseja ver a hora em M[minuto] ou S[segundo] ').upper()

if decisao == 'M':
     minutos = hora_em_minutos(hora)
     print('{} horas é igual a {} minutos'.format(hora, minutos))
elif decisao == 'S':
     segundos = hora_em_segundos(hora)
     print('{} horas é igual a  {} segundos'.format(hora, segundos))
else:
   print('Escolha Errada')



