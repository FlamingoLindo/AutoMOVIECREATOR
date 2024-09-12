from faker import Faker

fake = Faker('pt_BR')

def create_phone():
    phone = fake.date_of_birth()
    
    return phone