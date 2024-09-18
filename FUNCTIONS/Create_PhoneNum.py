from faker import Faker

fake = Faker('pt_BR')

def create_phone():
    phone = fake.phone_number()
    
    return phone