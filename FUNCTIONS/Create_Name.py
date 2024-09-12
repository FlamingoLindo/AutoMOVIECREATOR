from faker import Faker

fake = Faker('pt_BR')

def create_random_name():
    name = fake.name().split(' ')[1]
    
    return name

def create_random_email():
    email = fake.email()
    
    return email