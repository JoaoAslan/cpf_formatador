cpf = input('DIGITE AQUI SEU CPF:  ')

if not cpf.isdigit() or cpf.__len__() != 11:
    print('DIGITE UM VALOR VÁLIDO!')

else:
    cpf_formatado = ''
    contador = 0
    for num in cpf:
        if contador == 3 or contador == 6:
            cpf_formatado += '.'
        elif contador == 9:
            cpf_formatado += '-'
        cpf_formatado += num
        contador += 1

print(cpf_formatado)
