import re
import sys

cpf_usuario = input('Digite os numeros CPF: ')
cpf = re.sub(r'[^0-9]', '', cpf_usuario)

entrada_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == cpf_gerado:
    print(f'{cpf} é valido')
else:
    print('CPF invalido')


