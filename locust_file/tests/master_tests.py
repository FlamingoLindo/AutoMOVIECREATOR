
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
         if MasterUser.token is None:
            MasterUser.token = self.login()
             
    def on_stop(self):
        print(u'\033[0;32mTest stoped!\033[0m')
        
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
                token = response_json.get('jwt') or response_json.get('refreshToken')
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
        return {"Authorization": f"Bearer {self.token}"}
    
    @task
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
        response = self.client.post('users', headers=headers, json=body, name='Usuario - Criar')
        print(u'\033[1;30m\033[1mMASTER ACCOUNT CREATED\033[0m')
        
    @task 
    def load_master(self):
        headers = self.get_headers()
        response = self.client.get('getUserMaster', headers=headers, name='Usuario Master - Carregar')
        print(u'\033[1;30m\033[1mMASTER ACCOUNT LOADED\033[0m')
        
    @task
    def list_all_masters(self):
        headers = self.get_headers()
        response = self.client.get('users?filters[username][$contains]=Com&populate=*', headers=headers, name ='Usuario - Carregar')
        print(u'\033[1;30m\033[1mMASTER ACCOUNTS LOADED\033[0m')
        
    @task
    def list_a_master(self):
        headers = self.get_headers()
        response = self.client.get('users/548', headers=headers, name ='Usuario - Listar')
        print(u'\033[1;30m\033[1mMASTER ACCOUNT LOADED 2\033[0m')
        
    @task
    def list_dashboard(self):
        headers = self.get_headers()
        response = self.client.get('getDashMaster', headers=headers, name ='Dashboard - Master')
        print(u'\033[1;30m\033[1mDASHBOARD LOADED\033[0m')
        
    @task
    def list_clients(self):
        headers = self.get_headers()
        response = self.client.get('getListClients/1/10', headers=headers, name ='Gestão de Clientes - Listar')
        print(u'\033[1;30m\033[1mCLIENTS LISTED\033[0m')
        
    @task
    def list_clients_names(self):
        headers = self.get_headers()
        response = self.client.get('getListClientsName/es/1/10', headers=headers, name ='Gestão de Clientes - Listar Nome')
        print(u'\033[1;30m\033[1mCLIENTS NAMES LISTED\033[0m')
        
    @task
    def list_clients_financial(self):
        headers = self.get_headers()
        response = self.client.get('getClients/1/10', headers=headers, name ='Financeiro - Listar Clientes')
        print(u'\033[1;30m\033[1mCLIENTS FINANCE\033[0m')
        
    @task
    def list_clients_financial_name(self):
        headers = self.get_headers()
        response = self.client.get('getClientsName/sp/1/2', headers=headers, name ='Financeiro - Listar por Nome')
        print(u'\033[1;30m\033[1mCLIENTS NAME FINANCE\033[0m')
        
    @task
    def list_clients_financial_name(self):
        headers = self.get_headers()
        response = self.client.get('getClientsStatus/Inadimplente/1/2', headers=headers, name ='Financeiro - Listar por Status')
        print(u'\033[1;30m\033[1mCLIENTS STATUS FINANCE\033[0m')
        
    @task
    def edit_user_permissions(self):
        body = {
            "functions": ["4", "5"]
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('users/7', headers=headers, json=body, name='Usuario - Atualizar Funções')
        print(u'\033[1;30m\033[1mMASTER ACCOUNT EDITED\033[0m')
        
    @task
    def block_user(self):
        body = {
            "blocked": True
        }
        headers = self. get_headers()
        headers["Content-Type"] = "appplication/json"
        response = self.client.put('blockedClient/104', headers= headers, json=body, name='Usuario - Bloquear')
        print(u'\033[1;30m\033[1mUSER BLOCKED\033[0m')
    
    @task
    def list_users_manegement(self):
        headers = self.get_headers()
        response = self.client.get('getListUsers/1/10', headers=headers, name ='Gestão de Usuários - Listar')
        print(u'\033[1;30m\033[1mUSERS MANAGEMENT LISTED\033[0m')
        
    @task
    def list_users_manegement_by_name(self):
        headers = self.get_headers()
        response = self.client.get('getListUsersName/es/1/5', headers=headers, name ='Gestão de Usuários - Listar Nome')
        print(u'\033[1;30m\033[1mUSERS MANAGEMENT LISTED BY NAME\033[0m')
        
    @task
    def lisst_users_funcions(self):
        headers = self.get_headers()
        response = self.client.get('functions?filters[users][id]=7', headers=headers, name ='Funções de Usuários - Listar')
        print(u'\033[1;30m\033[1mFUNCTIONS LISTED\033[0m')
        
    @task
    def login2(self):
        body = {
            "userid": "7"
        }
        headers = self. get_headers()
        headers["Content-Type"] = "appplication/json"
        response = self.client.put('loginUser', headers= headers, json=body, name='Acessar Plataforma - Usuário "LOGIN 2"')
        print(u'\033[1;30m\033[1mLOGIN 2 DONE\033[0m')
        
    @task
    def list_new_supports(self):
        headers = self.get_headers()
        response = self.client.get('getNewSupportMaster/1/2', headers=headers, name ='Novos Chamados - Listar')
        print(u'\033[1;30m\033[1mNEW SUPPORTS LISTED\033[0m')
        
    @task
    def load_new_supports(self):
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Suporte Plataforma&populate=*&filters[$and][1][user][role]=6&filters[$and][2][user][username][$containsi]=c', headers=headers, name ='Filtrar Novos Chamados - Carregar')
        print(u'\033[1;30m\033[1mNEW SUPPORTS LOADED\033[0m')
        
    @task
    def list_pending_supports(self):
        headers = self.get_headers()
        response = self.client.get('getOpenSupportMaster/1/10', headers=headers, name ='Chamados Em Aberto - Listar')
        print(u'\033[1;30m\033[1mPENDING SUPPORTS LISTED\033[0m')
        
    @task
    def load_pending_supports(self):
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Suporte Plataforma&populate=*&filters[$and][1][user][role]=6&filters[$and][2][user][username][$containsi]=c', headers=headers, name ='Filtrar Chamados Em Aberto - Carregar')
        print(u'\033[1;30m\033[1mPENDING SUPPORTS LOADED\033[0m')
        
    @task
    def list_closed_supports(self):
        headers = self.get_headers()
        response = self.client.get('getClosedSupportMaster/1/1', headers=headers, name ='Chamados Finalizados - Listar')
        print(u'\033[1;30m\033[1mCLOSED SUPPORTS LISTED\033[0m')
        
    @task
    def load_closed_supports(self):
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Suporte Plataforma&filters[$and][1][status]=Solucionado&filters[$and][3][user][role]=6&filters[$and][4][user][username][$containsi]=com&pagination[page]=1&pagination[pageSize]=1&populate=*', headers=headers, name ='Filtrar Chamados Finalizados - Carregar')
        print(u'\033[1;30m\033[1mCLOSED SUPPORTS LOADED\033[0m')
    
    @task
    def answer_support(self):
        body = {
            "supportid": "2352",
		    "message": "Alterada as permissões do usuário"
        }
        headers = self. get_headers()
        headers["Content-Type"] = "appplication/json"
        response = self.client.post('createAnswerSupport', headers= headers, json=body, name='Respostas Chamados - Criar')
        print(u'\033[1;30m\033[1mSUPPORT ANSWERED\033[0m')
        
    @task
    def list_supports_answered(self):
        headers = self.get_headers()
        response = self.client.get('answer-supports?filters[support_request][id]=1&populate=*', headers=headers, name ='Respostas Chamados - Listar')
        print(u'\033[1;30m\033[1mANSWERED SUPPORTS LISTED\033[0m')
        
    @task
    def list_account_closure_supports(self):
        headers = self.get_headers()
        response = self.client.get('getCancelSupportMaster/1/50', headers=headers, name ='Chamados de Cancelamento - Listar')
        print(u'\033[1;30m\033[1mCLOSURE SUPPORTS LISTED\033[0m')
        
    @task
    def filter_account_closure_supports(self):
        headers = self.get_headers()
        response = self.client.get('Filtrar Chamados de Cancelamento - Listar', headers=headers, name ='Filtrar Chamados de Cancelamento - Listar')
        print(u'\033[1;30m\033[1mCLOSURE SUPPORTS FILTERED\033[0m')
        
    @task
    def list_terms(self):
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=termo&populate=*', headers=headers, name ='Termo Uso - Exibir')
        print(u'\033[1;30m\033[1mTERMS LISTED\033[0m')
        
    @task
    def list_privacy(self):
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=politica&populate=*', headers=headers, name ='Termo Uso - Exibir')
        print(u'\033[1;30m\033[1mPRIVACY LISTED\033[0m')
        
    @task
    def create_plan(self):
        body = {
            "data": 
                {
                        "name": "Plaano teste 1111 ",
                        "value": 10,
                        "description": "Teste da Plataforma",
                        "title": "Teste 11111",
                        "promotion": None,
                        "externalId": None,
                        "active": True,
                        "registerDate": None,
                        "renovationAutomatic": None,
                        "discount": None,
                        "parcel": None,
                        "trialPeriod": None,
                        "contracts": None,
                        "created_by_id": "1",
                        "type_signature": "1"
                        }
        }
        headers = self. get_headers()
        headers["Content-Type"] = "appplication/json"
        response = self.client.post('plans', headers= headers, json=body, name='Plano - Criar')
        print(u'\033[1;30m\033[1mPLAN CREATED\033[0m')
        
    @task
    def load_plan(self):
        headers = self.get_headers()
        response = self.client.get('plans?filters[id][$eq]=406&pagination[page]=1&pagination[pageSize]=15&pagination[withCount]=true&populate=*', headers=headers, name ='Plano - Carregar')
        print(u'\033[1;30m\033[1mPLAN LOADED\033[0m')
        
    @task
    def list_plan(self):
        headers = self.get_headers()
        response = self.client.get('getMasterPlan', headers=headers, name ='Plano - Listar')
        print(u'\033[1;30m\033[1mPLAN LISTED\033[0m')
        
    @task
    def load_company(self):
        headers = self.get_headers()
        response = self.client.get('users?filters[role]=6&filters[$and][1][id]=7&filters[$and][2][username][$containsi]=c&fields[0]=username&fields[1]=cnpj&fields[2]=phone&[3]=email&populate[0]=photo&populate[1]=contracts.payments', headers=headers, name ='Empresa - Carregar')
        print(u'\033[1;30m\033[1mCOMANY LOADED\033[0m')
        
    @task
    def list_company_payment_hist(self):
        headers = self.get_headers()
        response = self.client.get('paymentCompanyId?userid=7&transactionId=&status=Pago&page=1&perPage=10', headers=headers, name ='Histórico Pagamento - Por Empresa Filtrando por Id')
        print(u'\033[1;30m\033[1mPAYMENT HISTORY LISTED\033[0m')