import random

def gera_cnpj():
    # Gerar os primeiros 12 dígitos do CNPJ
    cnpj = [random.randint(0, 9) for _ in range(8)]
    cnpj += [0, 0, 0, 1]  # Filial padrão
    
    # Calcular o primeiro dígito verificador
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = sum(x * y for x, y in zip(cnpj, pesos1))
    digito1 = 11 - soma1 % 11
    digito1 = digito1 if digito1 < 10 else 0
    cnpj.append(digito1)
    
    # Calcular o segundo dígito verificador
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = sum(x * y for x, y in zip(cnpj, pesos2))
    digito2 = 11 - soma2 % 11
    digito2 = digito2 if digito2 < 10 else 0
    cnpj.append(digito2)
    
    # Formatar o CNPJ
    cnpj_formatado = ''.join(map(str, cnpj))
    return cnpj_formatado[:2] + '.' + cnpj_formatado[2:5] + '.' + cnpj_formatado[5:8] + '/' + cnpj_formatado[8:12] + '-' + cnpj_formatado[12:]

# Exemplo de uso