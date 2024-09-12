"""
# Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            print(f"Sucesso: {response.json()}")
        else:
            # Em caso de erro, imprime o status e o corpo da resposta
            print(f"Erro: {response.status_code}")
            print(f"Detalhes do erro: {response.text}")
"""

#from tests.school_tests import SchoolUser

from tests.master_tests import MasterUser

