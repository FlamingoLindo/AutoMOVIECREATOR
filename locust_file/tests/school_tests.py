from locust import HttpUser, task,between
import sys
import os

# Adicione o caminho correto ao sys.path
path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print(f"Adding path: {path_to_add}")
sys.path.append(path_to_add)

from FUNCTIONS.Create_Name import create_random_name
from FUNCTIONS.Create_CPF import gera_e_valida_cpf 

class SchoolUser(HttpUser):
    wait_time = between(1, 5)
    
    # Variável para armazenar o token globalmente
    token = None
    
    def on_start(self):
        # Verifica se o token já foi obtido; caso contrário, faz login e armazena o token
        if not SchoolUser.token:
            SchoolUser.token = self.login()
    
    def login(self):
        try:
            response = self.client.post("auth/local", 
                                        json={"identifier": "abc2@gmail.com", "password": "12345678"})
            if response.status_code == 200:
                response_json = response.json()
                print(f"Response JSON: {response_json}")
                token = response_json.get('jwt') or response_json.get('refreshToken')
                if token:
                    return token
                else:
                    raise Exception("Token JWT não encontrado na resposta.")
            else:
                print(f"Falha ao fazer login: {response.status_code}")
                print(f"Erro: {response.text}")
                raise Exception("Falha ao obter token JWT")
        except Exception as e:
            print(f"Erro durante a solicitação: {e}")
            raise

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    @task
    def create_company(self):
        body = {
            "username": f"{create_random_name()}",
            "email": f"{create_random_name()}@gmail.com",
            "cpf": f"{gera_e_valida_cpf()}",
            "password": "12345678",
            "phone": "(11) 91234-5678",
            "visible": True
        }
        response = self.client.post("createCompany", json=body, name='Criar conta')
        
    @task
    def list_plans(self):
        headers = self.get_headers()
        response = self.client.get("verifyPlanCompany", headers=headers, name="Listar planos da empresa")
        
    @task
    def forgot_password(self):
        body = {
            "email": "flamingolindo@aaathats3as.com"
        }
        headers = self.get_headers()
        response = self.client.post("auth/forgot-password", json=body, headers=headers, name='Esqueci a senha')

    @task
    def load_school(self):
        body = {
            "id": 7,
            "username": "Company Teste",
            "email": "company@gmail.com",
            "phone": "null"
        }
        headers = self.get_headers()
        response = self.client.get('users?filters[id]=104&populate[0]=company&populate[1]=role', json=body, headers=headers, name='Carregar Empresa')
    
    @task
    def update_bank_account(self):
        body = {
            "bank": {
            "nameAccount": "Livia Empresa",
            "document": "09197577000100",
            "agency": "0160",
            "account": "41004-9",
            "bank": "341"
            }
        }
        headers = self.get_headers()
        response = self.client.put('updateBankData', json=body, headers=headers, name='Atualizar conta bancária')
        
    @task 
    def get_bank_data(self):
        body = {
            "bank": {
                "nameAccount": "Michael Afton",
                "document": "90785906029",
                "agency": "0231",
                "account": "0980701-2",
                "bank": "237"
            }
        }
        headers = self.get_headers()
        response = self.client.get('clients?filters[user]=147', json=body, headers=headers, name='Pegar dados bancários')
        
    @task
    def add_adress(self):
        body = {
            "addressName": "Rua João Ribeiro",
            "number": 45,
            "postalCode": "08810-220",
            "district": "Vila Suissa",
            "city": "Mogi das Cruzes",
            "state": "SP"
        }
        headers = self.get_headers()
        response = self.client.post('createAddressCompany', json=body, headers=headers, name='Cadastrar endereço')
        
    @task
    def load_adress(self):
        headers = self.get_headers()
        response = self.client.get('addresses?filters[company][userCompany]=276&populate=*', headers=headers, name='Mostrar endereço')
        
    @task
    def update_adress(self):
        body = {
            "addressName": "Rua João Ribeiro",
            "number": 2,
            "postalCode": "08810-220",
            "district": "Vila Suissa",
            "city": "Mogi das Cruzes",
            "state": "SP"
        }
        headers = self.get_headers()
        response = self.client.put('updatedAddressCompany', json=body, headers=headers, name='Atualizar endereço')
        
    @task
    def list_credit_card(self):
        headers = self.get_headers()
        response = self.client.get('myCards', headers=headers, name='Listar cartões')
        
    @task
    def fav_card(self): 
        headers = self.get_headers()
        response = self.client.put('setFavoriteCards/392', headers=headers, name='Favorite a card')
        
    @task
    def insert_plan_cart(self): 
        body = {
            "data": {
                "plan":    
                {
                    "id": 257
                }
                    }
        }
        headers = self.get_headers()
        response = self.client.post('insertTransactionItemCompany', headers=headers, name='Insert plan in cart')
        
        
    @task
    def show_bought_items(self):
        headers = self.get_headers()
        response = self.client.get('getMyExtract?page=1&perPage=10', headers=headers, name='Get bought items')
        
    @task
    def get_transactions(self):
        headers = self.get_headers()
        response = self.client.get('transactions?filters[user}=147', headers=headers, name='Get transactions')
