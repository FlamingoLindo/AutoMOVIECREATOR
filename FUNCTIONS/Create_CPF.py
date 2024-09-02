import random

def gera_e_valida_cpf():
    while True:
        # Generate the first 9 digits of the CPF
        cpf = [random.randint(0, 9) for _ in range(9)]
        
        # Calculate the first check digit
        soma1 = sum(x * y for x, y in zip(cpf, range(10, 1, -1)))
        digito1 = (soma1 * 10 % 11) % 10
        cpf.append(digito1)
        
        # Calculate the second check digit
        soma2 = sum(x * y for x, y in zip(cpf, range(11, 1, -1)))
        digito2 = (soma2 * 10 % 11) % 10
        cpf.append(digito2)
        
        # Validate the generated CPF
        cpf_numeros = cpf[:]
        if len(cpf_numeros) != 11:
            continue
        
        soma1_validacao = sum(x * y for x, y in zip(cpf_numeros[:9], range(10, 1, -1)))
        digito1_validacao = (soma1_validacao * 10 % 11) % 10
        if cpf_numeros[9] != digito1_validacao:
            continue
        
        soma2_validacao = sum(x * y for x, y in zip(cpf_numeros[:10], range(11, 1, -1)))
        digito2_validacao = (soma2_validacao * 10 % 11) % 10
        if cpf_numeros[10] != digito2_validacao:
            continue
        
        # Format the CPF
        cpf_formatado = ''.join(map(str, cpf))
        return cpf_formatado[:3] + '.' + cpf_formatado[3:6] + '.' + cpf_formatado[6:9] + '-' + cpf_formatado[9:]