from faker import Faker

fake = Faker('pt_BR')

def gera_cnpj():
    cnpj = fake.cnpj()
    
    return cnpj