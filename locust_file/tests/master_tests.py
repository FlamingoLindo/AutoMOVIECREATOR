
from locust import HttpUser, between, task
import sys
import os

func_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
sys.path.append(func_path)

from FUNCTIONS.Create_Name import create_random_name, create_random_email

class MasterUser(HttpUser):
    wait_time = between(1,5)
    host = 'https://moviecreator.mestresdaweb.io/api/'
    
    token = None
    
    def on_start(self):
         print(u'\033[0;32mStarting test!\033[0m')
         if not MasterUser.token:
             MasterUser.token = self.login()
             
    def on_stop(self):
        print(u'\033[0;32mTeste stoped!\033[0m')
        
    def login(self):
        body = {
            "identifier":"master@moviecreator.com",
	        "password":"12345678"
        }
        try:
            response = self.client.post('auth/local', json=body, name='Login')

            if response.status_code == 200:
                response_json = response.json()
                print("\033[1;33mLOGIN", response_json, "\033[0m")
                token = response_json.get('jwt') or response_json.get('refreshToken')  # Corrigido
                if token:
                    return token
                else:
                    raise Exception(u"\033[0;31mToken não encontrado!!!\033[0m")
            else:
                print("Falha ao fazer login!\n", response.status_code)
                print(response.text)
                raise Exception(u"\033[0;31mFalha ao obter o token!\033[0m")
        except Exception as e:
            print(u'\033[0;31mErro durante a "GET"\033[0m', e)
            raise
        
    def get_headers(self):
        return{"Authorization": f"Bearer {self.token}"}
    
    """@task
    def create_user(self):
        body = {
            "username": f"{create_random_name()}",
            "email": f"{create_random_email()}",
            "password": "12345678",
            "functions": ["4", "5"],
            "role": "8",
            "created_by_id": "1"
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('users', json=body, name='Usuario - Criar')"""
        
        
    @task 
    def load_master(self):
        headers = self.get_headers()
        response = self.client.get('getUserMaster', name='Usuario Master - Carregar')
        
        