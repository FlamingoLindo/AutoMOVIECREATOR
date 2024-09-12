
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
        print(u'\033[0;32mStarting test!\033[0m')
        if ProfessorUser.token is None:
            ProfessorUser.token = self.login()
             
    def on_stop(self):
        print(u'\033[0;32mTest stopped!\033[0m')
        
    def login(self):
        body = {
            "identifier": "master@moviecreator.com",
            "password": "12345678"
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
                    raise Exception(u"\033[0;31mToken not found!\033[0m")
            else:
                print("Login failed!\n", response.status_code)
                print(response.text)
                raise Exception(u"\033[0;31mFailed to obtain token!\033[0m")
        except Exception as e:
            print(u'\033[0;31mError during "POST"\033[0m', e)
            raise
        
    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    @task
    def Login(self):
        body = {
	"identifier":"master@moviecreator.com",
	"password":"12345678"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('auth/local', headers=headers, json=body, name='Login')
        print(f"Executed Login with status code {response.status_code}")

    @task
    def RefreshToken(self):
        body = {
    "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzcyLCJpYXQiOjE3MTEwMzAzOTQsImV4cCI6MTcxMTExNjc5NH0.qdusPqLiQ7_WdD9f-ZswynmrTgX_rl4v5S9MryDLwhU" 
  
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('auth/refresh-token', headers=headers, json=body, name='RefreshToken')
        print(f"Executed RefreshToken with status code {response.status_code}")

    @task
    def Login___Atualizar_DateAcess(self):
        body = {	
	"dateAcess": "2023-01-13"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/8', headers=headers, json=body, name='Login___Atualizar_DateAcess')
        print(f"Executed Login___Atualizar_DateAcess with status code {response.status_code}")

    @task
    def Usuario___Criar(self):
        body = {
		"username": "Sub Teste1",
		"email": "teste_sub1@gmail.com",
        "password": "12345678",
	    "functions": ["4", "5"],
	    "role": "8",
	    "created_by_id": "1"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('users', headers=headers, json=body, name='Usuario___Criar')
        print(f"Executed Usuario___Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Master(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Master')
        print(f"Executed Salvar_Foto___Master with status code {response.status_code}")

    @task
    def Deletar_Foto___Master(self):
        body = {
    "data": {
        "user": 1
    }
}
        headers = self.get_headers()
        response = self.client.delete('upload/files/41', headers=headers, name='Deletar_Foto___Master')
        print(f"Executed Deletar_Foto___Master with status code {response.status_code}")

    @task
    def Usuario_Master___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getUserMaster', headers=headers, name='Usuario_Master___Carregar')
        print(f"Executed Usuario_Master___Carregar with status code {response.status_code}")

    @task
    def Usuario___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('users?filters[username][$contains]=Com&populate=*', headers=headers, name='Usuario___Carregar')
        print(f"Executed Usuario___Carregar with status code {response.status_code}")

    @task
    def Usuario___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('users/111', headers=headers, name='Usuario___Listar')
        print(f"Executed Usuario___Listar with status code {response.status_code}")

    @task
    def Dashboard___Master(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getDashMaster', headers=headers, name='Dashboard___Master')
        print(f"Executed Dashboard___Master with status code {response.status_code}")

    @task
    def Gestão_de_Clientes___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getListClients/1/10', headers=headers, name='Gestão_de_Clientes___Listar')
        print(f"Executed Gestão_de_Clientes___Listar with status code {response.status_code}")

    @task
    def Gestão_de_Clientes___Listar_Nome(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getListClientsName/es/1/10', headers=headers, name='Gestão_de_Clientes___Listar_Nome')
        print(f"Executed Gestão_de_Clientes___Listar_Nome with status code {response.status_code}")

    @task
    def Financeiro___Listar_Clientes(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getClients/1/10', headers=headers, name='Financeiro___Listar_Clientes')
        print(f"Executed Financeiro___Listar_Clientes with status code {response.status_code}")

    @task
    def Financeiro___Listar_por_Nome(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getClientsName/sp/1/2', headers=headers, name='Financeiro___Listar_por_Nome')
        print(f"Executed Financeiro___Listar_por_Nome with status code {response.status_code}")

    @task
    def Financeiro___Listar_por_Status(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getClientsStatus/Inadimplente/1/2', headers=headers, name='Financeiro___Listar_por_Status')
        print(f"Executed Financeiro___Listar_por_Status with status code {response.status_code}")

    @task
    def Usuario___Atualizar_Funções(self):
        body = {
    "functions": ["4", "5"]
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/7', headers=headers, json=body, name='Usuario___Atualizar_Funções')
        print(f"Executed Usuario___Atualizar_Funções with status code {response.status_code}")

    @task
    def Alterar_Senha___Usuário(self):
        body = {
	"userid": "7",
	"currentPassword": "12345678",
	"newPassword": "1234567",
	"repeatNewPassword": "1234567"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('masterChangeUserPassword', headers=headers, json=body, name='Alterar_Senha___Usuário')
        print(f"Executed Alterar_Senha___Usuário with status code {response.status_code}")

    @task
    def Usuario___Bloquear(self):
        body = {
    "blocked": False
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('blockedClient/104', headers=headers, json=body, name='Usuario___Bloquear')
        print(f"Executed Usuario___Bloquear with status code {response.status_code}")

    @task
    def Gestão_de_Usuários___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getListUsers/1/10', headers=headers, name='Gestão_de_Usuários___Listar')
        print(f"Executed Gestão_de_Usuários___Listar with status code {response.status_code}")

    @task
    def Gestão_de_Usuários___Listar_Nome(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getListUsersName/es/1/5', headers=headers, name='Gestão_de_Usuários___Listar_Nome')
        print(f"Executed Gestão_de_Usuários___Listar_Nome with status code {response.status_code}")

    @task
    def Funções_de_Usuários___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('functions?filters[users][id]=7', headers=headers, name='Funções_de_Usuários___Listar')
        print(f"Executed Funções_de_Usuários___Listar with status code {response.status_code}")

    @task
    def Acessar_Plataforma___Usuário(self):
        body = {
	"userid": "7"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('loginUser', headers=headers, json=body, name='Acessar_Plataforma___Usuário')
        print(f"Executed Acessar_Plataforma___Usuário with status code {response.status_code}")

    @task
    def Novos_Chamados___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getNewSupportMaster/1/2', headers=headers, name='Novos_Chamados___Listar')
        print(f"Executed Novos_Chamados___Listar with status code {response.status_code}")

    @task
    def Filtrar_Novos_Chamados___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Suporte Plataforma&populate=*&filters[$and][1][user][role]=6&filters[$and][2][user][username][$containsi]=c', headers=headers, name='Filtrar_Novos_Chamados___Carregar')
        print(f"Executed Filtrar_Novos_Chamados___Carregar with status code {response.status_code}")

    @task
    def Chamados_Em_Aberto___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getOpenSupportMaster/1/10', headers=headers, name='Chamados_Em_Aberto___Listar')
        print(f"Executed Chamados_Em_Aberto___Listar with status code {response.status_code}")

    @task
    def Filtrar_Chamados_Em_Aberto___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Suporte Plataforma&filters[$or][1][status]=Em analise&filters[$or][2][status]=Pendente&filters[$and][3][user][role]=6&filters[$and][4][user][username][$containsi]=com&pagination[page]=1&pagination[pageSize]=5&populate=*', headers=headers, name='Filtrar_Chamados_Em_Aberto___Carregar')
        print(f"Executed Filtrar_Chamados_Em_Aberto___Carregar with status code {response.status_code}")

    @task
    def Chamados_Finalizados___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getClosedSupportMaster/1/1', headers=headers, name='Chamados_Finalizados___Listar')
        print(f"Executed Chamados_Finalizados___Listar with status code {response.status_code}")

    @task
    def Filtrar_Chamados_Finalizados___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Suporte Plataforma&filters[$and][1][status]=Solucionado&filters[$and][3][user][role]=6&filters[$and][4][user][username][$containsi]=com&pagination[page]=1&pagination[pageSize]=1&populate=*', headers=headers, name='Filtrar_Chamados_Finalizados___Carregar')
        print(f"Executed Filtrar_Chamados_Finalizados___Carregar with status code {response.status_code}")

    @task
    def Respostas_Chamados___Criar(self):
        body = {
	    "supportid": "15",
		"message": "Alterada as permissões do usuário"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createAnswerSupport', headers=headers, json=body, name='Respostas_Chamados___Criar')
        print(f"Executed Respostas_Chamados___Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Resposta_Chamado(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Resposta_Chamado')
        print(f"Executed Salvar_Foto___Resposta_Chamado with status code {response.status_code}")

    @task
    def Respostas_Chamados___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('answer-supports?filters[support_request][id]=1&populate=*', headers=headers, name='Respostas_Chamados___Listar')
        print(f"Executed Respostas_Chamados___Listar with status code {response.status_code}")

    @task
    def Chamados_de_Cancelamento___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCancelSupportMaster/1/50', headers=headers, name='Chamados_de_Cancelamento___Listar')
        print(f"Executed Chamados_de_Cancelamento___Listar with status code {response.status_code}")

    @task
    def Filtrar_Chamados_de_Cancelamento___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Cancelamento&filters[$and][2][user][role]=6&filters[$and][3][user][username][$containsi]=Company&pagination[page]=1&pagination[pageSize]=10&populate=*', headers=headers, name='Filtrar_Chamados_de_Cancelamento___Listar')
        print(f"Executed Filtrar_Chamados_de_Cancelamento___Listar with status code {response.status_code}")

    @task
    def Filtrar_Chamados_de_Cancelamento_Finalizados___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[type]=Cancelamento&filters[$and][1][externalUser][$containsi]=Company&pagination[page]=1&pagination[pageSize]=10&populate=*', headers=headers, name='Filtrar_Chamados_de_Cancelamento_Finalizados___Listar')
        print(f"Executed Filtrar_Chamados_de_Cancelamento_Finalizados___Listar with status code {response.status_code}")

    @task
    def Excluir_Conta(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deleteUser/197', headers=headers, name='Excluir_Conta')
        print(f"Executed Excluir_Conta with status code {response.status_code}")

    @task
    def Excluir_Conta___Recusada(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('deleteRefused/13', headers=headers, json=body, name='Excluir_Conta___Recusada')
        print(f"Executed Excluir_Conta___Recusada with status code {response.status_code}")

    @task
    def Confirmar_Cancelamento_Plano(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('confirmCancelPlan/410', headers=headers, name='Confirmar_Cancelamento_Plano')
        print(f"Executed Confirmar_Cancelamento_Plano with status code {response.status_code}")

    @task
    def Confirmar_Cancelamento_Plano___Recusada_Copy(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('refusedCancelPlanCompany/129', headers=headers, json=body, name='Confirmar_Cancelamento_Plano___Recusada_Copy')
        print(f"Executed Confirmar_Cancelamento_Plano___Recusada_Copy with status code {response.status_code}")

    @task
    def arquivo___baixar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('fileDownload?fileId=5737', headers=headers, name='arquivo___baixar')
        print(f"Executed arquivo___baixar with status code {response.status_code}")

    @task
    def Salvar_Foto___Termo_de_Uso(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Termo_de_Uso')
        print(f"Executed Salvar_Foto___Termo_de_Uso with status code {response.status_code}")

    @task
    def Termo_Uso___Exibir(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=termo&populate=*', headers=headers, name='Termo_Uso___Exibir')
        print(f"Executed Termo_Uso___Exibir with status code {response.status_code}")

    @task
    def Termo_Uso___Editar(self):
        body = {
    "data": {
        
        "name": "termo",
        "description": "dvadsvadva"
        
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('terms/1', headers=headers, json=body, name='Termo_Uso___Editar')
        print(f"Executed Termo_Uso___Editar with status code {response.status_code}")

    @task
    def Salvar_Foto___Politica_de_Privacidade(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Politica_de_Privacidade')
        print(f"Executed Salvar_Foto___Politica_de_Privacidade with status code {response.status_code}")

    @task
    def Politica_Privacidade___Exibir(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=politica&populate=*', headers=headers, name='Politica_Privacidade___Exibir')
        print(f"Executed Politica_Privacidade___Exibir with status code {response.status_code}")

    @task
    def Politica_Privacidade___Editar(self):
        body = {
    "data": {
        
        "name": "termo",
        "description": "dvadsvadva"
        
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('terms/2', headers=headers, json=body, name='Politica_Privacidade___Editar')
        print(f"Executed Politica_Privacidade___Editar with status code {response.status_code}")

    @task
    def Plano___Criar(self):
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

        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('plans', headers=headers, json=body, name='Plano___Criar')
        print(f"Executed Plano___Criar with status code {response.status_code}")

    @task
    def Plano___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('plans?filters[id][$eq]=2&pagination[page]=1&pagination[pageSize]=15&pagination[withCount]=true&populate=*', headers=headers, name='Plano___Carregar')
        print(f"Executed Plano___Carregar with status code {response.status_code}")

    @task
    def Plano___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getMasterPlan', headers=headers, name='Plano___Listar')
        print(f"Executed Plano___Listar with status code {response.status_code}")

    @task
    def Plano___Atualizar(self):
        body = { 
    "data": 
    {
    "nome": "Anual",
    "value": 275,
    "description": "ççlç",
    "createdAt": "2023-07-16T15:09:18.026Z",
    "updatedAt": "2023-07-16T15:09:31.865Z",
    "publishedAt": "2023-07-16T15:09:31.486Z",
    "title": "ll",
    "promotion": "ll",
    "active": True
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('plans/1', headers=headers, json=body, name='Plano___Atualizar')
        print(f"Executed Plano___Atualizar with status code {response.status_code}")

    @task
    def Plano___Excluir(self):
        body = {
    "data": {
        "id": 1,
        "active": False
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('plans/1', headers=headers, json=body, name='Plano___Excluir')
        print(f"Executed Plano___Excluir with status code {response.status_code}")

    @task
    def Plano___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deletePlanMaster?planId=255', headers=headers, name='Plano___Excluir')
        print(f"Executed Plano___Excluir with status code {response.status_code}")

    @task
    def Regras_Inadimplentes__Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('rule-suspensions?filters[id]=1', headers=headers, name='Regras_Inadimplentes__Listar')
        print(f"Executed Regras_Inadimplentes__Listar with status code {response.status_code}")

    @task
    def Teste(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('test', headers=headers, name='Teste')
        print(f"Executed Teste with status code {response.status_code}")

    @task
    def Regras_Inadimplentes___Editar(self):
        body = {
    "data": {
        "id": 1,
        "value": 30,
        "active": True
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('rule-suspensions/1', headers=headers, json=body, name='Regras_Inadimplentes___Editar')
        print(f"Executed Regras_Inadimplentes___Editar with status code {response.status_code}")

    @task
    def Empresa___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('users?filters[role]=6&filters[$and][1][id]=7&filters[$and][2][username][$containsi]=c&fields[0]=username&fields[1]=cnpj&fields[2]=phone&[3]=email&populate[0]=photo&populate[1]=contracts.payments', headers=headers, name='Empresa___Carregar')
        print(f"Executed Empresa___Carregar with status code {response.status_code}")

    @task
    def Histórico_Pagamento___Por_Empresa_Filtrando_por_Id(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('paymentCompanyId?userid=7&transactionId=&status=Pago&page=1&perPage=10', headers=headers, name='Histórico_Pagamento___Por_Empresa_Filtrando_por_Id')
        print(f"Executed Histórico_Pagamento___Por_Empresa_Filtrando_por_Id with status code {response.status_code}")

    @task
    def Histórico_Pagamento___Por_Empresa(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('paymentCompany/147/1/10', headers=headers, name='Histórico_Pagamento___Por_Empresa')
        print(f"Executed Histórico_Pagamento___Por_Empresa with status code {response.status_code}")

    @task
    def Download_Pagamento(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('generatePaymentInformation?transactionId=8469', headers=headers, name='Download_Pagamento')
        print(f"Executed Download_Pagamento with status code {response.status_code}")
