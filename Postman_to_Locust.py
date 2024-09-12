import json

# Load the Postman collection JSON
with open('Professor - Coordenador.postman_collection.json') as f:
    data = json.load(f)

# Function to replace JSON values (true/false/null) with Python equivalents (True/False/None)
def convert_json_values(body_str):
    if body_str:
        body_str = body_str.replace('true', 'True')
        body_str = body_str.replace('false', 'False')
        body_str = body_str.replace('null', 'None')
    return body_str

# Open the file to write Locust tasks
with open('professor_tests.py', 'w') as file:
    file.write("""
from locust import HttpUser, between, task
import sys
import os

func_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(func_path)

from FUNCTIONS.Create_Name import create_random_name, create_random_email
from FUNCTIONS.Create_Adress import create_address
from FUNCTIONS.Create_Card import create_card
from FUNCTIONS.Create_CNPJ import gera_cnpj
from FUNCTIONS.Create_CPF import gera_e_valida_cpf
from FUNCTIONS.Create_PhoneNum import create_phone


class ProfessorUser(HttpUser):
    wait_time = between(1, 5)
    host = 'https://moviecreator.mestresdaweb.io/api/'
    
    token = None
    
    def on_start(self):
        print(u'\\033[0;32mStarting test!\\033[0m')
        if ProfessorUser.token is None:
            ProfessorUser.token = self.login()
             
    def on_stop(self):
        print(u'\\033[0;32mTest stopped!\\033[0m')
        
    def login(self):
        body = {
            "identifier": "master@moviecreator.com",
            "password": "12345678"
        }
        try:
            response = self.client.post('auth/local', json=body, name='Login')
            if response.status_code == 200:
                response_json = response.json()
                print("\\033[1;33mLOGIN", response_json, "\\033[0m")
                token = response_json.get('jwt') or response_json.get('refreshToken')
                if token:
                    return token
                else:
                    raise Exception(u"\\033[0;31mToken not found!\\033[0m")
            else:
                print("Login failed!\\n", response.status_code)
                print(response.text)
                raise Exception(u"\\033[0;31mFailed to obtain token!\\033[0m")
        except Exception as e:
            print(u'\\033[0;31mError during "POST"\\033[0m', e)
            raise
        
    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}
""")

    # Function to extract and write request details
    def extract_request_details(items):
        for item in items:
            if 'item' in item:
                extract_request_details(item['item'])
            else:
                name = item.get('name', 'N/A').replace(' ', '_').replace('-', '_')
                request = item.get('request', {})
                method = request.get('method', 'get').lower()  # Default to 'get' if method is missing
                url = request.get('url', {}).get('raw', 'N/A')

                # Remove '{{prod}}' from the URL
                url = url.replace('{{prod}}', '')

                # Get the request body if it exists and convert JSON values to Python equivalents
                body = request.get('body', {}).get('raw', None)
                body = convert_json_values(body)
                
                # Write the Locust task method to the file
                file.write(f"""
    @task
    def {name}(self):\n""")
                
                if body:
                    # Write the body if it exists
                    file.write(f"        body = {body}\n")
                else:
                    file.write(f"        body = None\n")
                
                file.write(f"""        headers = self.get_headers()\n""")
                
                # If POST or PUT request, include body in the request
                if method in ['post', 'put']:
                    file.write(f"        headers['Content-Type'] = 'application/json'\n")
                    file.write(f"        response = self.client.{method}('{url}', headers=headers, json=body, name='{name}')\n")
                else:
                    # For GET requests, do not include the body
                    file.write(f"        response = self.client.{method}('{url}', headers=headers, name='{name}')\n")
                
                file.write(f"        print(f\"Executed {name} with status code {{response.status_code}}\")\n")

    # Start extraction
    extract_request_details(data.get('item', []))
