from faker import Faker

fake = Faker('pt_BR')

def gera_e_valida_cpf():
    cpf = fake.cpf()
    
    return cpf