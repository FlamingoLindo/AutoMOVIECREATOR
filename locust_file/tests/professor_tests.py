
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
    def Empresa___Registrar(self):
        body = {

		"username": "EscolaMaster2",

		"email": "escola_braba4@gmail.com",

        "cpf": "None",

		"cnpj": "38426999000108",

        "password":"12345678",

        "phone": "(11) 91234-5678",

        "visible": True

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createCompany', headers=headers, json=body, name='Empresa___Registrar')
        print(f"Executed Empresa___Registrar with status code {response.status_code}")

    @task
    def Login(self):
        body = {
    "identifier": "fernanditos@gmail.com",
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
    def Login___Change_Password(self):
        body = {
	"currentPassword":"123457",
	"passwordConfirmation":"123456",
	"password":"123456"
	
}

        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('auth/change-password', headers=headers, json=body, name='Login___Change_Password')
        print(f"Executed Login___Change_Password with status code {response.status_code}")

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
    def Verifica___Plano_Empresa(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('verifyPlanCompany', headers=headers, name='Verifica___Plano_Empresa')
        print(f"Executed Verifica___Plano_Empresa with status code {response.status_code}")

    @task
    def Esqueci_a_Senha(self):
        body = {
	"email":"fabio@mestresdaweb.com.br"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('auth/forgot-password', headers=headers, json=body, name='Esqueci_a_Senha')
        print(f"Executed Esqueci_a_Senha with status code {response.status_code}")

    @task
    def Reset_Senha(self):
        body = {
    "code":"42c64711184ba3000ec80c6ee0abe28ef781738a8818139d6a396eaa693792e5972cdcd40b91bb55edfd6b818deaec487390d4ce43b612381899fda824810209",
    "password": "123456789",
    "passwordConfirmation": "123456789"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('auth/reset-password', headers=headers, json=body, name='Reset_Senha')
        print(f"Executed Reset_Senha with status code {response.status_code}")

    @task
    def Criar_Cliente___Pagarme(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createClient', headers=headers, json=body, name='Criar_Cliente___Pagarme')
        print(f"Executed Criar_Cliente___Pagarme with status code {response.status_code}")

    @task
    def Salvar_Foto___Empresa(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Empresa')
        print(f"Executed Salvar_Foto___Empresa with status code {response.status_code}")

    @task
    def Deletar_Foto___Empresa(self):
        body = {

    "data": {

        "user": 1

    }

}
        headers = self.get_headers()
        response = self.client.delete('upload/files/2', headers=headers, name='Deletar_Foto___Empresa')
        print(f"Executed Deletar_Foto___Empresa with status code {response.status_code}")

    @task
    def Usuario_Empresa___Carregar(self):
        body = {

	"id": 7,

	"username": "Company Teste",

	"email": "company@gmail.com",

	"phone": None

}
        headers = self.get_headers()
        response = self.client.get('users?filters[id]=104&populate[0]=company&populate[1]=role', headers=headers, name='Usuario_Empresa___Carregar')
        print(f"Executed Usuario_Empresa___Carregar with status code {response.status_code}")

    @task
    def Alterar_Senha___Usuário(self):
        body = {
	"currentPassword": "12345678",
	"newPassword": "1234567",
	"repeatNewPassword": "1234567"
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('changeUserPassword', headers=headers, json=body, name='Alterar_Senha___Usuário')
        print(f"Executed Alterar_Senha___Usuário with status code {response.status_code}")

    @task
    def Usuário_Empresa___Atualizar(self):
        body = {

    "phone": None

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('updateUser', headers=headers, json=body, name='Usuário_Empresa___Atualizar')
        print(f"Executed Usuário_Empresa___Atualizar with status code {response.status_code}")

    @task
    def Dados_Bancários___Cadastrar(self):
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
        headers['Content-Type'] = 'application/json'
        response = self.client.put('updateBankData', headers=headers, json=body, name='Dados_Bancários___Cadastrar')
        print(f"Executed Dados_Bancários___Cadastrar with status code {response.status_code}")

    @task
    def Dados_Bancários___listar(self):
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
        response = self.client.get('clients?filters[user]=147', headers=headers, name='Dados_Bancários___listar')
        print(f"Executed Dados_Bancários___listar with status code {response.status_code}")

    @task
    def Endereço___Criar(self):
        body = {

				"addressName": "Rua João Ribeiro",

				"number": 45,

				"postalCode": "08810-220",

				"complement": None,

				"district": "Vila Suissa",

				"city": "Mogi das Cruzes",

				"state": "SP"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createAddressCompany', headers=headers, json=body, name='Endereço___Criar')
        print(f"Executed Endereço___Criar with status code {response.status_code}")

    @task
    def Endereço___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('addresses?filters[company][userCompany]=276&populate=*', headers=headers, name='Endereço___Carregar')
        print(f"Executed Endereço___Carregar with status code {response.status_code}")

    @task
    def Endereço___Carregar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('addresses/77', headers=headers, name='Endereço___Carregar_Copy')
        print(f"Executed Endereço___Carregar_Copy with status code {response.status_code}")

    @task
    def Endereço___Atualizar(self):
        body = {


				"number": 15


}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('updatedAddressCompany', headers=headers, json=body, name='Endereço___Atualizar')
        print(f"Executed Endereço___Atualizar with status code {response.status_code}")

    @task
    def Cartão___Criar(self):
        body = {

	    "name": "Tony Stark", 

		"externalID": "token_mBoe8XFgwtxKe293",

		"lastDigits": "9480",

		"brand": "Mastercard",

		"expirationYear": "2024",

		"expirationMonth": "12"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createCard', headers=headers, json=body, name='Cartão___Criar')
        print(f"Executed Cartão___Criar with status code {response.status_code}")

    @task
    def Cartão___Criar_pagarme(self):
        body = {

	"card": {

        "cvv": 581,

        "exp_month": 6,

        "exp_year": 25,

        "holder_document": "36527420013",

        "holder_name": "Teste",

        "number": "5146739326511067"

    },

    "type": "card"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('https://api.pagar.me/core/v5/tokens?appId=pk_test_e0byZ6zIqiWZ5qwG', headers=headers, json=body, name='Cartão___Criar_pagarme')
        print(f"Executed Cartão___Criar_pagarme with status code {response.status_code}")

    @task
    def Cartão___Criar_Copy(self):
        body = {

	    "name": "Empresa teste sete", 

		"externalID": "token_xGXnpGJuAuNk3eYl",

		"lastDigits": "5229",

		"brand": "Mastercard",

		"expirationYear": "24",

		"expirationMonth": "11"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createCard', headers=headers, json=body, name='Cartão___Criar_Copy')
        print(f"Executed Cartão___Criar_Copy with status code {response.status_code}")

    @task
    def Cartão___Criar_pagarme_Copy(self):
        body = {

	"card": {

        "cvv": "651",

        "exp_month": "1",

        "exp_year": "30",

        "holder_document": "51779735065",

        "holder_name": "Tony Stark",

        "number": "4000000000000010"

    },

    "type": "card"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('https://api.pagar.me/core/v5/tokens?appId=pk_test_e0byZ6zIqiWZ5qwG', headers=headers, json=body, name='Cartão___Criar_pagarme_Copy')
        print(f"Executed Cartão___Criar_pagarme_Copy with status code {response.status_code}")

    @task
    def Cartão___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('myCards', headers=headers, name='Cartão___Listar')
        print(f"Executed Cartão___Listar with status code {response.status_code}")

    @task
    def Cartão___Favoritar(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('setFavoriteCards/206', headers=headers, json=body, name='Cartão___Favoritar')
        print(f"Executed Cartão___Favoritar with status code {response.status_code}")

    @task
    def Cartão___Delete(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('cards/206', headers=headers, name='Cartão___Delete')
        print(f"Executed Cartão___Delete with status code {response.status_code}")

    @task
    def Transação___Empresa___antigo(self):
        body = {

    "data":{

        "code": "AB231208121293CBR",

        "userStudent": "73"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('transactions', headers=headers, json=body, name='Transação___Empresa___antigo')
        print(f"Executed Transação___Empresa___antigo with status code {response.status_code}")

    @task
    def Carrinho___Inserir_Item(self):
        body = {

    "data": {

        "plan":    

        {

            "id": 257

        },

		"transaction":         

        {

            "id": None  
        }

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('insertTransactionItemCompany', headers=headers, json=body, name='Carrinho___Inserir_Item')
        print(f"Executed Carrinho___Inserir_Item with status code {response.status_code}")

    @task
    def Atualizar_Transação(self):
        body = {

	"data": {

        "coupon": None,

        "paymentMethod": "1",

        "portion": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('transactions/9', headers=headers, json=body, name='Atualizar_Transação')
        print(f"Executed Atualizar_Transação with status code {response.status_code}")

    @task
    def Selecionar_Transação___Empresa(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('setSelectedTransaction/10', headers=headers, json=body, name='Selecionar_Transação___Empresa')
        print(f"Executed Selecionar_Transação___Empresa with status code {response.status_code}")

    @task
    def Carrinho_Item_Selecionado___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getTransaction', headers=headers, name='Carrinho_Item_Selecionado___Listar')
        print(f"Executed Carrinho_Item_Selecionado___Listar with status code {response.status_code}")

    @task
    def Compras___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getTransactions', headers=headers, name='Compras___Listar')
        print(f"Executed Compras___Listar with status code {response.status_code}")

    @task
    def Carrinho___Solicitar_Cancelamento(self):
        body = {

    "data":{

        "status": "Cancelar"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('transactions/1', headers=headers, json=body, name='Carrinho___Solicitar_Cancelamento')
        print(f"Executed Carrinho___Solicitar_Cancelamento with status code {response.status_code}")

    @task
    def Carrinho___Pagamento(self):
        body = {

    "id": 9589,

    "payment_method": 1, 

    "tokenCard": "card_Bxj8JLOTKHxzlYNd",

    "portion": "1" 

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('paymentTransaction', headers=headers, json=body, name='Carrinho___Pagamento')
        print(f"Executed Carrinho___Pagamento with status code {response.status_code}")

    @task
    def Extrato___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getMyExtract?page=1&perPage=10', headers=headers, name='Extrato___Listar')
        print(f"Executed Extrato___Listar with status code {response.status_code}")

    @task
    def Listar_todas_transações(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('transactions?filters[user}=147', headers=headers, name='Listar_todas_transações')
        print(f"Executed Listar_todas_transações with status code {response.status_code}")

    @task
    def Curso___Criar_Tags(self):
        body = {

    "data": {

        "name": "teste",

        "course": "6",

        "publishedAt": "2023-12-06T13:59:51.147Z"

    }

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('tags', headers=headers, json=body, name='Curso___Criar_Tags')
        print(f"Executed Curso___Criar_Tags with status code {response.status_code}")

    @task
    def Curso___Criar_Tags_Copy(self):
        body = {

	"data": 

		{

				"name": "Teste",

				"description": "\\zxbnm,.hgfdsa",

				"code": "251236",

				"module": "1",

				"forums": None,

                "fileClasses": None,

                "textLessons": None,

                "wordingLessons": None

        }

    }
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('tags/1', headers=headers, json=body, name='Curso___Criar_Tags_Copy')
        print(f"Executed Curso___Criar_Tags_Copy with status code {response.status_code}")

    @task
    def Modulo___Criar(self):
        body = {

	"data": 

		{

				"name": "Introdução",

				"course": "1",

				"lessons": ["1"],

				"exams": None,

				"userProfessors": ["1"],

                "valueOrder": 1

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('modules', headers=headers, json=body, name='Modulo___Criar')
        print(f"Executed Modulo___Criar with status code {response.status_code}")

    @task
    def Modulo___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('modules', headers=headers, name='Modulo___Carregar')
        print(f"Executed Modulo___Carregar with status code {response.status_code}")

    @task
    def Modulo___Editar(self):
        body = {

	"data": 

		{

			"id": 2,

            "course": "6",

            "exams": None,

            "user": "73",

            "valueOrder": 1

		}

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('modules/2', headers=headers, json=body, name='Modulo___Editar')
        print(f"Executed Modulo___Editar with status code {response.status_code}")

    @task
    def Modulo___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deleteModule?moduleId=2357', headers=headers, name='Modulo___Excluir')
        print(f"Executed Modulo___Excluir with status code {response.status_code}")

    @task
    def Alterar_Ordem___Aulas_do_Modulo(self):
        body = {

    "lessonOrder": ["4","3"]

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('listLessons/2', headers=headers, json=body, name='Alterar_Ordem___Aulas_do_Modulo')
        print(f"Executed Alterar_Ordem___Aulas_do_Modulo with status code {response.status_code}")

    @task
    def Arquivo_da_Aula___Criar(self):
        body = {

  "data": {

    "type": "written",

    "title": "Quem se importa?",

    "description": "Você está pronto!",

    "lesson": "5",

    "scoreFile": 10,

    "score": "10",

    "question": "291",

    "valueOrder": "5"

  }

} 
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('lesson-files', headers=headers, json=body, name='Arquivo_da_Aula___Criar')
        print(f"Executed Arquivo_da_Aula___Criar with status code {response.status_code}")

    @task
    def Arquivo_da_Aula___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('lesson-files', headers=headers, name='Arquivo_da_Aula___Listar')
        print(f"Executed Arquivo_da_Aula___Listar with status code {response.status_code}")

    @task
    def Arquivo_da_Aula___Editar(self):
        body = {

	"data": {

        "type": "video",

        "title": "teste2",

        "description": "Você está pronto!",

        "linkFile": "https://www.youtube.com/watch?v=h1Kp9x_ADZwg",

        "lesson": "5",

        "scoreFile": 10,

        "score": None,

        "question": None,

        "valueOrder": "4"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('lesson-files/11', headers=headers, json=body, name='Arquivo_da_Aula___Editar')
        print(f"Executed Arquivo_da_Aula___Editar with status code {response.status_code}")

    @task
    def Arquivo_da_Aula___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('lesson-files/1', headers=headers, name='Arquivo_da_Aula___Excluir')
        print(f"Executed Arquivo_da_Aula___Excluir with status code {response.status_code}")

    @task
    def Salvar_Arquivo___Aula(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Arquivo___Aula')
        print(f"Executed Salvar_Arquivo___Aula with status code {response.status_code}")

    @task
    def Deletar_Arquivo___Aula(self):
        body = {

    "data": {

        "user": 1

    }

}
        headers = self.get_headers()
        response = self.client.delete('upload/files/1', headers=headers, name='Deletar_Arquivo___Aula')
        print(f"Executed Deletar_Arquivo___Aula with status code {response.status_code}")

    @task
    def Texto_Aula___Criar(self):
        body = {

	"data": 

		{

            "type": "text",

            "title": "fdshklç",

            "description": "Você está pronto!",

            "scoreFile": 12,

            "valueOrder": "1"

        }

    }
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('file-classes', headers=headers, json=body, name='Texto_Aula___Criar')
        print(f"Executed Texto_Aula___Criar with status code {response.status_code}")

    @task
    def Texto_Aula___Editar(self):
        body = {

	"data": {

        "type": "text",

        "title": "fdshklç",

        "description": "Você está pronto!",

        "scoreFile": 12,

        "valueOrder": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('file-classes/11', headers=headers, json=body, name='Texto_Aula___Editar')
        print(f"Executed Texto_Aula___Editar with status code {response.status_code}")

    @task
    def Texto_da_Aula___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('file-classes/1', headers=headers, name='Texto_da_Aula___Excluir')
        print(f"Executed Texto_da_Aula___Excluir with status code {response.status_code}")

    @task
    def Salvar_Arquivo___Aula(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Arquivo___Aula')
        print(f"Executed Salvar_Arquivo___Aula with status code {response.status_code}")

    @task
    def Deletar_Arquivo___Aula(self):
        body = {

    "data": {

        "user": 1

    }

}
        headers = self.get_headers()
        response = self.client.delete('upload/files/1', headers=headers, name='Deletar_Arquivo___Aula')
        print(f"Executed Deletar_Arquivo___Aula with status code {response.status_code}")

    @task
    def Alternativas_de_Questão___Criar(self):
        body = {

    "data": {

            "description": "Questão 1 ",

            "isCorrect": True

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('alternatives', headers=headers, json=body, name='Alternativas_de_Questão___Criar')
        print(f"Executed Alternativas_de_Questão___Criar with status code {response.status_code}")

    @task
    def Questões___Criar(self):
        body = {

    "data": {

            "title": "Questão 1 ",

            "description": "aHJHGSFDS",

            "linkMaterial": None,

            "alternatives": ["1"]

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('questions', headers=headers, json=body, name='Questões___Criar')
        print(f"Executed Questões___Criar with status code {response.status_code}")

    @task
    def Bloco_de_Questão___Criar(self):
        body = {

	"data": 

		{

            "type": "question",

            "title": "fdshklç",

            "description": "Você está pronto!",

            "scoreFile": 12,

            "valueOrder": "1"

        }

    }
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('file-classes', headers=headers, json=body, name='Bloco_de_Questão___Criar')
        print(f"Executed Bloco_de_Questão___Criar with status code {response.status_code}")

    @task
    def Bloco_de_Questão___Editar(self):
        body = {

	"data": {

        "type": "text",

        "title": "fdshklç",

        "description": "Você está pronto!",

        "question": "1",

        "scoreFile": 12,

        "valueOrder": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('file-classes/11', headers=headers, json=body, name='Bloco_de_Questão___Editar')
        print(f"Executed Bloco_de_Questão___Editar with status code {response.status_code}")

    @task
    def Bloco_de_Questão___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('file-classes/1', headers=headers, name='Bloco_de_Questão___Excluir')
        print(f"Executed Bloco_de_Questão___Excluir with status code {response.status_code}")

    @task
    def Aula___Criar(self):
        body = {

	"data": {

        "name": "Aula Teste",

        "description": "Aprensentação e configuração de projeto",

        "duration": "20",

        "module": "29",

        "forums": None,

        "fileClasses": None,

        "creatorName": "Movie Creator"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('lessons', headers=headers, json=body, name='Aula___Criar')
        print(f"Executed Aula___Criar with status code {response.status_code}")

    @task
    def Aula___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('lessons/5?populate=*', headers=headers, name='Aula___Carregar')
        print(f"Executed Aula___Carregar with status code {response.status_code}")

    @task
    def Aula___Carregar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('lessons/5?populate=*', headers=headers, name='Aula___Carregar_Copy')
        print(f"Executed Aula___Carregar_Copy with status code {response.status_code}")

    @task
    def Aulas___Pendentes(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('lessons?filters[module][id]=2&filters[status][$containsi]=pendente&populate=*', headers=headers, name='Aulas___Pendentes')
        print(f"Executed Aulas___Pendentes with status code {response.status_code}")

    @task
    def Aulas___Pendentes_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('lessons?filters[module][id]=2&filters[status][$containsi]=pendente&populate=*', headers=headers, name='Aulas___Pendentes_Copy')
        print(f"Executed Aulas___Pendentes_Copy with status code {response.status_code}")

    @task
    def Aulas___Pendentes_Copy_2(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('lessons?filters[module][id]=2&filters[status][$containsi]=pendente&populate=*', headers=headers, name='Aulas___Pendentes_Copy_2')
        print(f"Executed Aulas___Pendentes_Copy_2 with status code {response.status_code}")

    @task
    def Blocos_da_Aula___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('listFilesLessons/1', headers=headers, name='Blocos_da_Aula___Listar')
        print(f"Executed Blocos_da_Aula___Listar with status code {response.status_code}")

    @task
    def Aula___Editar(self):
        body = {

	"data": {

        "id": 6,

        "name": "Conclusão",

        "description": "Formatura!!! Você não precisa mais de nada!",

        "fileClasses": [11]

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('lessons/6', headers=headers, json=body, name='Aula___Editar')
        print(f"Executed Aula___Editar with status code {response.status_code}")

    @task
    def Alterar_Ordem___Arquivos_Aula(self):
        body = {

    "fileClassOrder": ["2","1","4","3"]

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('listFilesLesson/5', headers=headers, json=body, name='Alterar_Ordem___Arquivos_Aula')
        print(f"Executed Alterar_Ordem___Arquivos_Aula with status code {response.status_code}")

    @task
    def Aula___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('lessons/8', headers=headers, name='Aula___Excluir')
        print(f"Executed Aula___Excluir with status code {response.status_code}")

    @task
    def Alternativas_de_Questão___Criar(self):
        body = {

    "data": {

            "description": "Questão 1 ",

            "isCorrect": True

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('alternatives', headers=headers, json=body, name='Alternativas_de_Questão___Criar')
        print(f"Executed Alternativas_de_Questão___Criar with status code {response.status_code}")

    @task
    def Questões___Criar(self):
        body = {

    "data": {

            "title": "Questão 1 ",

            "description": "aHJHGSFDS",

            "linkMaterial": None,

            "alternatives": ["1"],

            "comment": None

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('questions', headers=headers, json=body, name='Questões___Criar')
        print(f"Executed Questões___Criar with status code {response.status_code}")

    @task
    def Bloco_de_Questão___Criar(self):
        body = {

	"data": 

		{

            "type": "text",

            "title": "fdshklç",

            "description": "Você está pronto!",

            "question": "1",

            "scoreFile": 12,

            "valueOrder": "1"

        }

    }
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('file-classes', headers=headers, json=body, name='Bloco_de_Questão___Criar')
        print(f"Executed Bloco_de_Questão___Criar with status code {response.status_code}")

    @task
    def Bloco_de_Questão___Editar(self):
        body = {

	"data": {

        "type": "text",

        "title": "fdshklç",

        "description": "Você está pronto!",

        "question": "1",

        "scoreFile": 12,

        "valueOrder": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('file-classes/11', headers=headers, json=body, name='Bloco_de_Questão___Editar')
        print(f"Executed Bloco_de_Questão___Editar with status code {response.status_code}")

    @task
    def Bloco_de_Questão___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('file-classes/1', headers=headers, name='Bloco_de_Questão___Excluir')
        print(f"Executed Bloco_de_Questão___Excluir with status code {response.status_code}")

    @task
    def Texto_Aula___Criar(self):
        body = {

	"data": 

		{

            "type": "text",

            "title": "fdshklç",

            "description": "Você está pronto!",

            "scoreFile": 12,

            "valueOrder": "1"

        }

    }
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('file-classes', headers=headers, json=body, name='Texto_Aula___Criar')
        print(f"Executed Texto_Aula___Criar with status code {response.status_code}")

    @task
    def Texto_Aula___Editar(self):
        body = {

	"data": {

        "type": "text",

        "title": "fdshklç",

        "description": "Você está pronto!",

        "scoreFile": 12,

        "valueOrder": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('file-classes/11', headers=headers, json=body, name='Texto_Aula___Editar')
        print(f"Executed Texto_Aula___Editar with status code {response.status_code}")

    @task
    def Texto_da_Aula___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('file-classes/1', headers=headers, name='Texto_da_Aula___Excluir')
        print(f"Executed Texto_da_Aula___Excluir with status code {response.status_code}")

    @task
    def Salvar_Arquivo___Aula(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Arquivo___Aula')
        print(f"Executed Salvar_Arquivo___Aula with status code {response.status_code}")

    @task
    def Deletar_Arquivo___Aula(self):
        body = {

    "data": {

        "user": 1

    }

}
        headers = self.get_headers()
        response = self.client.delete('upload/files/1', headers=headers, name='Deletar_Arquivo___Aula')
        print(f"Executed Deletar_Arquivo___Aula with status code {response.status_code}")

    @task
    def Provas___Criar(self):
        body = {

            "name": "Prova Teste 2",

            "score": 10,

            "status": "Em análise",

            "numberAttempts": 1,

            "module": "1819",

            "examBlocks": ["1","2"],

            "userCompany": 147

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('exams', headers=headers, json=body, name='Provas___Criar')
        print(f"Executed Provas___Criar with status code {response.status_code}")

    @task
    def Prova___Publicar(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('activeExam?examId=361', headers=headers, json=body, name='Prova___Publicar')
        print(f"Executed Prova___Publicar with status code {response.status_code}")

    @task
    def Prova___Anular(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('cancelExam?examId=154', headers=headers, json=body, name='Prova___Anular')
        print(f"Executed Prova___Anular with status code {response.status_code}")

    @task
    def Provas___Alterar(self):
        body = {

    "data": {

            "name": "Prova 1",

            "score": 1000,

            "status": "Em aberto",

            "numberAttempts": 3,

            "registerDate": None,

            "module": "1",

            "questions": ["1","2"],

            "userProfessor": "1"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('exams/1', headers=headers, json=body, name='Provas___Alterar')
        print(f"Executed Provas___Alterar with status code {response.status_code}")

    @task
    def Prova___Corrigir(self):
        body = {

    "note": 10

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('correctExam?takeTestId=318', headers=headers, json=body, name='Prova___Corrigir')
        print(f"Executed Prova___Corrigir with status code {response.status_code}")

    @task
    def Prova___Corrigir_Questão(self):
        body = {

    "data": {

        "correct": True

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('answer-questions/221', headers=headers, json=body, name='Prova___Corrigir_Questão')
        print(f"Executed Prova___Corrigir_Questão with status code {response.status_code}")

    @task
    def Provas___Pendentes(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('exams?filters[userCompany]=3&filters[status][$containsi]=pendente&populate=*', headers=headers, name='Provas___Pendentes')
        print(f"Executed Provas___Pendentes with status code {response.status_code}")

    @task
    def Provas___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('exams/42?populate[1]=take_tests.answerQuestions&populate[2]=take_tests.user.photo', headers=headers, name='Provas___Carregar')
        print(f"Executed Provas___Carregar with status code {response.status_code}")

    @task
    def Respostas_da_questão(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('answer-questions/3?populate=*', headers=headers, name='Respostas_da_questão')
        print(f"Executed Respostas_da_questão with status code {response.status_code}")

    @task
    def Respostas_da_questão_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('exams?populate=take_tests.answerQuestions, take_tests.user', headers=headers, name='Respostas_da_questão_Copy')
        print(f"Executed Respostas_da_questão_Copy with status code {response.status_code}")

    @task
    def Respostas_da_questão_Copy_2(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('take-tests/117?populate=*', headers=headers, name='Respostas_da_questão_Copy_2')
        print(f"Executed Respostas_da_questão_Copy_2 with status code {response.status_code}")

    @task
    def Provas___Curso(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getExamsCompany?courseId=946&name=&page=1&perPage=10', headers=headers, name='Provas___Curso')
        print(f"Executed Provas___Curso with status code {response.status_code}")

    @task
    def Provas___Carregar_do_curso(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('exams?filters[module][course]=518&populate=*', headers=headers, name='Provas___Carregar_do_curso')
        print(f"Executed Provas___Carregar_do_curso with status code {response.status_code}")

    @task
    def Provas_dos_Cursos___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('modules?populate=exams.take_tests&filters[course]=6', headers=headers, name='Provas_dos_Cursos___Carregar')
        print(f"Executed Provas_dos_Cursos___Carregar with status code {response.status_code}")

    @task
    def Corrigir_Questões___Criar(self):
        body = {

	"data": {

        "comment": "Teste Correção",

        "date": "2023-10-23",

        "question": "1",

        "user": "7"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('corrections', headers=headers, json=body, name='Corrigir_Questões___Criar')
        print(f"Executed Corrigir_Questões___Criar with status code {response.status_code}")

    @task
    def Corrigir_Questões_Curso___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('corrections?populate=*', headers=headers, name='Corrigir_Questões_Curso___Listar')
        print(f"Executed Corrigir_Questões_Curso___Listar with status code {response.status_code}")

    @task
    def Corrigir_Questões_Prova___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('corrections?filters[question][exam]=1&populate=*', headers=headers, name='Corrigir_Questões_Prova___Listar')
        print(f"Executed Corrigir_Questões_Prova___Listar with status code {response.status_code}")

    @task
    def Corrigir_Questões___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('corrections/1', headers=headers, name='Corrigir_Questões___Excluir')
        print(f"Executed Corrigir_Questões___Excluir with status code {response.status_code}")

    @task
    def Turmas___Criar(self):
        body = {

    "period": "Matutino",

    "name": "aaaw",

    "courses": ["1203"]

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createClass', headers=headers, json=body, name='Turmas___Criar')
        print(f"Executed Turmas___Criar with status code {response.status_code}")

    @task
    def Turmas___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('classes?filters[userCompany]=129&populate=*', headers=headers, name='Turmas___Listar')
        print(f"Executed Turmas___Listar with status code {response.status_code}")

    @task
    def Turmas___Alterar(self):
        body = {

	"data": 

		{

			"period": "Noite",

			"name": "Turma 1",

			"courses": "2",

				"userStudent": ["8"]	

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('classes/1', headers=headers, json=body, name='Turmas___Alterar')
        print(f"Executed Turmas___Alterar with status code {response.status_code}")

    @task
    def Forum___Criar(self):
        body = {

	"data": {

        "comment": "Na opinião de vocês, quais são os pontos positivos do jogo? (ainda estou procurando)",

        "lesson": "1",

        "user": 73

    }   

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('forums', headers=headers, json=body, name='Forum___Criar')
        print(f"Executed Forum___Criar with status code {response.status_code}")

    @task
    def Forum___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('forums?populate=forum_answers.user&populate=lesson&populate=user&filters[lesson][course][id]=467', headers=headers, name='Forum___Carregar')
        print(f"Executed Forum___Carregar with status code {response.status_code}")

    @task
    def Forum___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deleteForums/7', headers=headers, name='Forum___Excluir')
        print(f"Executed Forum___Excluir with status code {response.status_code}")

    @task
    def Respostas_Forum___Criar(self):
        body = {

    "data": {

            "date": "2023-10-16T15:45:00.000Z",

            "description": "Teste da Aplicação",

            "forum": "1",

            "user": "1"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('forum-answers', headers=headers, json=body, name='Respostas_Forum___Criar')
        print(f"Executed Respostas_Forum___Criar with status code {response.status_code}")

    @task
    def Responder_Resposta_Forum___Criar(self):
        body = {

    "data": {

            "date": "2023-12-14",

            "description": "Teste da Aplicação 3",

            "forumAnswer": "13",

            "user": "6"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('forum-answers', headers=headers, json=body, name='Responder_Resposta_Forum___Criar')
        print(f"Executed Responder_Resposta_Forum___Criar with status code {response.status_code}")

    @task
    def Respostas_Forum___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('forum-answers?filters[forum]=1&populate=*', headers=headers, name='Respostas_Forum___Carregar')
        print(f"Executed Respostas_Forum___Carregar with status code {response.status_code}")

    @task
    def Respostas_Forum___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('forum-answers/1', headers=headers, name='Respostas_Forum___Excluir')
        print(f"Executed Respostas_Forum___Excluir with status code {response.status_code}")

    @task
    def Respostas_das_Respostas_do_Forum___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deleteAnswerForums/30', headers=headers, name='Respostas_das_Respostas_do_Forum___Excluir')
        print(f"Executed Respostas_das_Respostas_do_Forum___Excluir with status code {response.status_code}")

    @task
    def Certificado___Criar(self):
        body = {

	"data": 

		{

                "title": "Teste",

                "code": "1234##"

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('certificates', headers=headers, json=body, name='Certificado___Criar')
        print(f"Executed Certificado___Criar with status code {response.status_code}")

    @task
    def Certificado___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('certificates', headers=headers, name='Certificado___Carregar')
        print(f"Executed Certificado___Carregar with status code {response.status_code}")

    @task
    def Certificado___Editar(self):
        body = {

	"data": 

		{

                "title": "Teste",

                "code": "1234##"

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('certificates/362', headers=headers, json=body, name='Certificado___Editar')
        print(f"Executed Certificado___Editar with status code {response.status_code}")

    @task
    def Cursos_Em_Analise___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCoursesCompanyPendenting?page=1&perPage=10', headers=headers, name='Cursos_Em_Analise___Carregar')
        print(f"Executed Cursos_Em_Analise___Carregar with status code {response.status_code}")

    @task
    def Cursos___Publicar(self):
        body = {

	"data": 

		{

            "status": "Publicado",

            "userCompany": "7"

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('courses/6', headers=headers, json=body, name='Cursos___Publicar')
        print(f"Executed Cursos___Publicar with status code {response.status_code}")

    @task
    def Cursos___Reprovado(self):
        body = {

	"data": 

		{

            "status": "Negado",

            "active": False

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('courses/6', headers=headers, json=body, name='Cursos___Reprovado')
        print(f"Executed Cursos___Reprovado with status code {response.status_code}")

    @task
    def Cursos___Criar(self):
        body = {

	"data": 

		{

				"name": "Aprendendo Strapi",

				"description": "Aprendendo a utilizar a ferramenta",

				"validate": "2024-10-16",

				"banner": None,

				"status": "Em análise",

				"registerDate": "2023-10-16",

				"active": False,

				"workload": None,

				"modules": None,

				"questions": None,

				"activities": None,

                "tags": None,

                "category": "1",

                "userCompany": "147",

                "private": True 
		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('courses', headers=headers, json=body, name='Cursos___Criar')
        print(f"Executed Cursos___Criar with status code {response.status_code}")

    @task
    def Cursos___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCoursesCompany?name=&status=&page=1&perPage=7', headers=headers, name='Cursos___Carregar')
        print(f"Executed Cursos___Carregar with status code {response.status_code}")

    @task
    def Cursos___Carregar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('coursesCompanyId', headers=headers, name='Cursos___Carregar_Copy')
        print(f"Executed Cursos___Carregar_Copy with status code {response.status_code}")

    @task
    def Cursos___Em_analise(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCoursesCompanyPendenting?page=1&perPage=15', headers=headers, name='Cursos___Em_analise')
        print(f"Executed Cursos___Em_analise with status code {response.status_code}")

    @task
    def Cursos___Publicado(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('courses?filters[$and][2][status]=Publicado&filters[$and][1][userCompany]=410', headers=headers, name='Cursos___Publicado')
        print(f"Executed Cursos___Publicado with status code {response.status_code}")

    @task
    def Cursos___Listar_Alunos(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('courses?populate=*', headers=headers, name='Cursos___Listar_Alunos')
        print(f"Executed Cursos___Listar_Alunos with status code {response.status_code}")

    @task
    def Cursos___Pacote(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('courses?filters[$and][1][userCompany]=147&filters[$and][2][status][$ne]=Em análise', headers=headers, name='Cursos___Pacote')
        print(f"Executed Cursos___Pacote with status code {response.status_code}")

    @task
    def Cursos___Listar_Provas(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('modules?filters[course]=2&populate=*', headers=headers, name='Cursos___Listar_Provas')
        print(f"Executed Cursos___Listar_Provas with status code {response.status_code}")

    @task
    def Cursos___Listar_Alunos_não_Vinculados(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getNewStudentsCourse?courseId=692&page=2&perPage=7', headers=headers, name='Cursos___Listar_Alunos_não_Vinculados')
        print(f"Executed Cursos___Listar_Alunos_não_Vinculados with status code {response.status_code}")

    @task
    def Curso___Adicionar_aluno(self):
        body = {

    "studentId": 463

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('addStudentCourse?courseId=3481', headers=headers, json=body, name='Curso___Adicionar_aluno')
        print(f"Executed Curso___Adicionar_aluno with status code {response.status_code}")

    @task
    def Curso___Duplicar(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('doubleCourse/1115', headers=headers, json=body, name='Curso___Duplicar')
        print(f"Executed Curso___Duplicar with status code {response.status_code}")

    @task
    def Curso___Aprovar(self):
        body = {

	"data": 

		{

            "status": "Aprovado",

            "statusSales": None

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('courses/6', headers=headers, json=body, name='Curso___Aprovar')
        print(f"Executed Curso___Aprovar with status code {response.status_code}")

    @task
    def Cursos___Editar(self):
        body = {

	"data": 

		{

            "id": 6,

            "name": "Conceitos basicos de valorant",

            "description": "Aprenda comunicação, teamplay, posicionamento, coordenação, utilitário, timing, confiança, mira, economia, controle skillshot, movimentação e noção de jogo",

            "validate": "2024-10-10",

            "value": 2.99,

            "registerDate": "2023-10-16",

            "active": True,

            "modules": [1, 2, 3]

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('courses/6', headers=headers, json=body, name='Cursos___Editar')
        print(f"Executed Cursos___Editar with status code {response.status_code}")

    @task
    def Cursos___Habilitar_p_venda_ou_Gratuito(self):
        body = {

    "statusSales": "Desabilitado",

    "value": 0,

    "active": True

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('approveCourse/20290', headers=headers, json=body, name='Cursos___Habilitar_p/_venda_ou_Gratuito')
        print(f"Executed Cursos___Habilitar_p/_venda_ou_Gratuito with status code {response.status_code}")

    @task
    def Cursos___Habilitar_todos_p_venda(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('enablesCoursesSale', headers=headers, json=body, name='Cursos___Habilitar_todos_p/_venda')
        print(f"Executed Cursos___Habilitar_todos_p/_venda with status code {response.status_code}")

    @task
    def Curso___Ativar(self):
        body = {
    "status": "Publicado",
    "active": False
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('courses/2', headers=headers, json=body, name='Curso___Ativar')
        print(f"Executed Curso___Ativar with status code {response.status_code}")

    @task
    def Curso___Pausar(self):
        body = {
    "data": {
        "status": "Pausado",
        "active": False
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('courses/382', headers=headers, json=body, name='Curso___Pausar')
        print(f"Executed Curso___Pausar with status code {response.status_code}")

    @task
    def Cursos___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deleteCourse/748', headers=headers, name='Cursos___Excluir')
        print(f"Executed Cursos___Excluir with status code {response.status_code}")

    @task
    def Avaliação_dos_Cursos___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('course-evaluations?filter[course]=2&populate=*', headers=headers, name='Avaliação_dos_Cursos___Listar')
        print(f"Executed Avaliação_dos_Cursos___Listar with status code {response.status_code}")

    @task
    def Avaliação___Nota_do_Curso(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCourseEvaluation?courseId=554', headers=headers, name='Avaliação___Nota_do_Curso')
        print(f"Executed Avaliação___Nota_do_Curso with status code {response.status_code}")

    @task
    def Alunos_do_Curso(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getStudentsCourse?courseId=894&name=&status=&page=1&perPage=10', headers=headers, name='Alunos_do_Curso')
        print(f"Executed Alunos_do_Curso with status code {response.status_code}")

    @task
    def Categoria___Criar(self):
        body = {

    "data": 

        {

                "name": "Node",

                "active": True

        }

    

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createCategory', headers=headers, json=body, name='Categoria___Criar')
        print(f"Executed Categoria___Criar with status code {response.status_code}")

    @task
    def Categorias___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('categories?filters[userCompany]=7', headers=headers, name='Categorias___Listar')
        print(f"Executed Categorias___Listar with status code {response.status_code}")

    @task
    def Categorias_Padrão___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('categories?filters[$or][1][type]=standard&filters[$or][2][userCompany]=7&filters[active]=true', headers=headers, name='Categorias_Padrão___Listar')
        print(f"Executed Categorias_Padrão___Listar with status code {response.status_code}")

    @task
    def Categoria___Alterar(self):
        body = {

    "name": "Mais Vistos"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('updateCategory?categoryId=43', headers=headers, json=body, name='Categoria___Alterar')
        print(f"Executed Categoria___Alterar with status code {response.status_code}")

    @task
    def Categoria___Ativar_Todas(self):
        body = {

    "data": 

        {

                "name": "Node",

                "active": True

        }

    

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('activeCategories/false', headers=headers, json=body, name='Categoria___Ativar_Todas')
        print(f"Executed Categoria___Ativar_Todas with status code {response.status_code}")

    @task
    def Categoria___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('categories/1', headers=headers, name='Categoria___Excluir')
        print(f"Executed Categoria___Excluir with status code {response.status_code}")

    @task
    def Plano_Differenciais___Criar(self):
        body = {

    "data": 

        {

                "description": "Acesso livre ao curso após a compra",

                "plans": ["1"],

                "publishedAt": "2023-12-06T13:59:51.147Z"

        }

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('plan-differentials', headers=headers, json=body, name='Plano_Differenciais___Criar')
        print(f"Executed Plano_Differenciais___Criar with status code {response.status_code}")

    @task
    def Plano___Criar(self):
        body = {

    "data": 

        {

            "name": "Gold",

            "value": 1200,

            "description": "Curso preparatprio gold completo com todas as informações mais adequadas para elevar seu conhecimento.",

            "title": "Gold",

            "promotion": None,

            "externalId": None,

            "active": True,

            "registerDate": None,

            "renovationAutomatic": None,

            "discount": None,

            "parcel": 1,

            "trialPeriod": 1,

            "userCompany": "129",

            "type_signature": "2",

            "courses": ["6"],

            "plan_differentials": ["1", "2", "3", "4"]

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
        response = self.client.get('getCompanyPlans', headers=headers, name='Plano___Carregar')
        print(f"Executed Plano___Carregar with status code {response.status_code}")

    @task
    def Plano___Carregar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('plans?filters[userCompany]=410&filters[active]=true&fields=id&pagination[pageSize]=100', headers=headers, name='Plano___Carregar_Copy')
        print(f"Executed Plano___Carregar_Copy with status code {response.status_code}")

    @task
    def Plano___AtivarDesativar(self):
        body = {
    "data": {
        "active": True
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('plans/106', headers=headers, json=body, name='Plano___Ativar/Desativar')
        print(f"Executed Plano___Ativar/Desativar with status code {response.status_code}")

    @task
    def Plano___Atualizar(self):
        body = {
    "data": {
        "courses": ["6"],
        "renovationAutomatic": False,
        "plan_differentials": ["1", "2", "3"]
    },
    "meta": {}
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('plans/92', headers=headers, json=body, name='Plano___Atualizar')
        print(f"Executed Plano___Atualizar with status code {response.status_code}")

    @task
    def Plano___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deletePlanCompany?planId=250', headers=headers, name='Plano___Excluir')
        print(f"Executed Plano___Excluir with status code {response.status_code}")

    @task
    def Cursos___Publicados_Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('coursesCompanyId', headers=headers, name='Cursos___Publicados_Listar')
        print(f"Executed Cursos___Publicados_Listar with status code {response.status_code}")

    @task
    def Planos___Criados_Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('plansCompanyId', headers=headers, name='Planos___Criados_Listar')
        print(f"Executed Planos___Criados_Listar with status code {response.status_code}")

    @task
    def Pacotes___Criar(self):
        body = {

	"data": 

		{

				"name": "Premium",

				"value": 1200,

				"registerDate": "2023-12-05",

				"description": "Beneficios premium",

				"type_signature": "2",

				"courses": ["6"],

				"userCompany": "7"

	}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('packages', headers=headers, json=body, name='Pacotes___Criar')
        print(f"Executed Pacotes___Criar with status code {response.status_code}")

    @task
    def Pacotes___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('packages?filters[userCompany]=7&populate=*', headers=headers, name='Pacotes___Listar')
        print(f"Executed Pacotes___Listar with status code {response.status_code}")

    @task
    def Pacotes___Listar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('packages?filters[userCompany]=7&populate=*', headers=headers, name='Pacotes___Listar_Copy')
        print(f"Executed Pacotes___Listar_Copy with status code {response.status_code}")

    @task
    def Tipo_de_assinatura(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('type-signatures?sort[id]=asc', headers=headers, name='Tipo_de_assinatura')
        print(f"Executed Tipo_de_assinatura with status code {response.status_code}")

    @task
    def Pacotes___Atualizar(self):
        body = {

	"data": 

		{

            "id": 1,

				"name": "Teste Package",

				"value": 1200,

				"registerDate": "2023-10-18",

				"banner": None,

				"description": "awertyuqwert",

				"accessPeriod": "2023-11-30",

				"courses": "2",

				"company": "1"

	}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('packages/1', headers=headers, json=body, name='Pacotes___Atualizar')
        print(f"Executed Pacotes___Atualizar with status code {response.status_code}")

    @task
    def Pacotes___Salvar_Foto(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Pacotes___Salvar_Foto')
        print(f"Executed Pacotes___Salvar_Foto with status code {response.status_code}")

    @task
    def Pacotes___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('deletePackageCompany?packageId=72', headers=headers, name='Pacotes___Excluir')
        print(f"Executed Pacotes___Excluir with status code {response.status_code}")

    @task
    def Termo_Uso___Exibir(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=termo&populate=*', headers=headers, name='Termo_Uso___Exibir')
        print(f"Executed Termo_Uso___Exibir with status code {response.status_code}")

    @task
    def Politica_Privacidade___Exibir(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=politica&populate=*', headers=headers, name='Politica_Privacidade___Exibir')
        print(f"Executed Politica_Privacidade___Exibir with status code {response.status_code}")

    @task
    def Importar_arquivo(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Importar_arquivo')
        print(f"Executed Importar_arquivo with status code {response.status_code}")

    @task
    def Importar_Afiliados(self):
        body = {

	"fileId": 4100

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('importAffiliates', headers=headers, json=body, name='Importar_Afiliados')
        print(f"Executed Importar_Afiliados with status code {response.status_code}")

    @task
    def Novo_Usuario_Afiliado___Criar(self):
        body = {

    "username":"Vinicius Aguiar",

	"email":"vinicius_afiliado@gmail.com",

    "cpf": "92280507056",

	"password":"12345678",

	"about": "fghjklç",

	"linkLinkedin": "https://www.youtube.com/watch?v=KV2ssT8lzj8&list=RD8nBFqZppIF0&index=27",

	"linkInstagram": "https://docs.strapi.io/dev-docs/api/rest/filters-locale-publication"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createAffiliate', headers=headers, json=body, name='Novo_Usuario_Afiliado___Criar')
        print(f"Executed Novo_Usuario_Afiliado___Criar with status code {response.status_code}")

    @task
    def Usuario_Afiliado___Atualizar(self):
        body = {

	"id": 2,

	"username": "Bruno Mattos",

	"email": "mattos2708@gmail.com",

	"cpf": None,

	"phone": None,

	"role": "4",

	"company": None,

	"affiliate": "1"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/4', headers=headers, json=body, name='Usuario_Afiliado___Atualizar')
        print(f"Executed Usuario_Afiliado___Atualizar with status code {response.status_code}")

    @task
    def Usuario_Afiliado___Ativar(self):
        body = {
    "blocked": False
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/460', headers=headers, json=body, name='Usuario_Afiliado___Ativar')
        print(f"Executed Usuario_Afiliado___Ativar with status code {response.status_code}")

    @task
    def Usuario_Afiliado___AprovarReprovar(self):
        body = {
    "userid": 1380
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('updateUserAffiliate?type=1', headers=headers, json=body, name='Usuario_Afiliado___Aprovar/Reprovar')
        print(f"Executed Usuario_Afiliado___Aprovar/Reprovar with status code {response.status_code}")

    @task
    def Usuario_Afiliado_Pendente___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('affiliates?filters[$and][1][userId][role]=4&filters[$and][2][userId][blocked]=true&filters[$and][3][accepted]=false&filters[$and][4][userId][companyAffiliate][id]=44&populate=userId&pagination[page]=1&pagination[pageSize]=10', headers=headers, name='Usuario_Afiliado_Pendente___Listar')
        print(f"Executed Usuario_Afiliado_Pendente___Listar with status code {response.status_code}")

    @task
    def Usuarios_Afiliado___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('listAffiliates?page=1&perPage=10', headers=headers, name='Usuarios_Afiliado___Listar')
        print(f"Executed Usuarios_Afiliado___Listar with status code {response.status_code}")

    @task
    def Usuarios_Afiliado___Listagem(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCompanyAffiliates?page=4&perPage=7', headers=headers, name='Usuarios_Afiliado___Listagem')
        print(f"Executed Usuarios_Afiliado___Listagem with status code {response.status_code}")

    @task
    def Usuarios_Afiliado___Listagem_por_Nome(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCompanyAffiliateName?username=Michael&page=1&perPage=10', headers=headers, name='Usuarios_Afiliado___Listagem_por_Nome')
        print(f"Executed Usuarios_Afiliado___Listagem_por_Nome with status code {response.status_code}")

    @task
    def Comissão_Afiliado(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('commissions?filters[userAffiliate][id]=148&populate=*', headers=headers, name='Comissão_Afiliado')
        print(f"Executed Comissão_Afiliado with status code {response.status_code}")

    @task
    def Comissão_Afiliado___Filtro_por_Nome_e_Status(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('commissions?filters[userAffiliate][id]=497&filters[$or][1][client][$containsi]=&filters[$or][1][status]=Não Pago', headers=headers, name='Comissão_Afiliado___Filtro_por_Nome_e_Status')
        print(f"Executed Comissão_Afiliado___Filtro_por_Nome_e_Status with status code {response.status_code}")

    @task
    def Usuario_Afiliado___Atualizar_Comissão(self):
        body = {

    "data": {

        "status": "Não Pago"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('commissions/2', headers=headers, json=body, name='Usuario_Afiliado___Atualizar_Comissão')
        print(f"Executed Usuario_Afiliado___Atualizar_Comissão with status code {response.status_code}")

    @task
    def Download_da_Comissão(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('generateCommissionInformation?commissionId=5', headers=headers, name='Download_da_Comissão')
        print(f"Executed Download_da_Comissão with status code {response.status_code}")

    @task
    def Importar_arquivo(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Importar_arquivo')
        print(f"Executed Importar_arquivo with status code {response.status_code}")

    @task
    def Importar_Professores(self):
        body = {

	"fileId": 6196

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('importProfessors', headers=headers, json=body, name='Importar_Professores')
        print(f"Executed Importar_Professores with status code {response.status_code}")

    @task
    def Novo_Usuario_Professor___Criar(self):
        body = {

	"username": "Professor golden",

	"email": "professor_golden@teste.com",

    "password":"12345678",

	"cpf": "92252023007",

    "function": "professor"

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createProfessor', headers=headers, json=body, name='Novo_Usuario_Professor___Criar')
        print(f"Executed Novo_Usuario_Professor___Criar with status code {response.status_code}")

    @task
    def Usuario_Professor___Atualizar(self):
        body = {

	"username": "Professor",

	"email": "professor@teste.com",

    "password":"12345678",

	"cpf": None,

	"phone": None,

	"role": "5"

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/1', headers=headers, json=body, name='Usuario_Professor___Atualizar')
        print(f"Executed Usuario_Professor___Atualizar with status code {response.status_code}")

    @task
    def Usuario_Professor___Atualizar_Função(self):
        body = {

	"function": "Professor"

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('professors/1', headers=headers, json=body, name='Usuario_Professor___Atualizar_Função')
        print(f"Executed Usuario_Professor___Atualizar_Função with status code {response.status_code}")

    @task
    def Usuario_Professor___Bloquear(self):
        body = {

    "blocked": False

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/6', headers=headers, json=body, name='Usuario_Professor___Bloquear')
        print(f"Executed Usuario_Professor___Bloquear with status code {response.status_code}")

    @task
    def Usuario_Professor___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('listEmployees?page=1&perPage=10', headers=headers, name='Usuario_Professor___Listar')
        print(f"Executed Usuario_Professor___Listar with status code {response.status_code}")

    @task
    def Usuario_Professor___Listar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('users?populate=*', headers=headers, name='Usuario_Professor___Listar_Copy')
        print(f"Executed Usuario_Professor___Listar_Copy with status code {response.status_code}")

    @task
    def Usuario_Professor___Listar_por_Nome(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('listEmployeesName?username=fá&page=1&perPage=10', headers=headers, name='Usuario_Professor___Listar_por_Nome')
        print(f"Executed Usuario_Professor___Listar_por_Nome with status code {response.status_code}")

    @task
    def Usuario_Professor___Atualizar_Funções(self):
        body = {
    "course_permissions": ["1", "2"],
    "exam_permissions": ["1", "2"],
    "forum_permissions": ["1", "2", "4"]
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/6', headers=headers, json=body, name='Usuario_Professor___Atualizar_Funções')
        print(f"Executed Usuario_Professor___Atualizar_Funções with status code {response.status_code}")

    @task
    def Importar_arquivo(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Importar_arquivo')
        print(f"Executed Importar_arquivo with status code {response.status_code}")

    @task
    def Importar_Alunos(self):
        body = {

	"fileId": 6506

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('importStudents', headers=headers, json=body, name='Importar_Alunos')
        print(f"Executed Importar_Alunos with status code {response.status_code}")

    @task
    def Novo_Usuario_Aluno___Criar(self):
        body = {

	"email":"viniciusteste@gmail.com",

	"username":"Vini Aluno Teste",

    "cpf": "70305282042",

	"password":"12345678",

    "grade": []

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createStudentCompany', headers=headers, json=body, name='Novo_Usuario_Aluno___Criar')
        print(f"Executed Novo_Usuario_Aluno___Criar with status code {response.status_code}")

    @task
    def Usuario_Aluno___Atualizar(self):
        body = {

    "classesStudent": ["2", "84"]

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('users/73', headers=headers, json=body, name='Usuario_Aluno___Atualizar')
        print(f"Executed Usuario_Aluno___Atualizar with status code {response.status_code}")

    @task
    def Usuario_Aluno___Bloquear(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('blockStudentCompany/253', headers=headers, json=body, name='Usuario_Aluno___Bloquear')
        print(f"Executed Usuario_Aluno___Bloquear with status code {response.status_code}")

    @task
    def Usuario_Aluno___Desbloquear(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('activeStudentCompany/253', headers=headers, json=body, name='Usuario_Aluno___Desbloquear')
        print(f"Executed Usuario_Aluno___Desbloquear with status code {response.status_code}")

    @task
    def Usuario_Aluno___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('users?populate=*', headers=headers, name='Usuario_Aluno___Listar')
        print(f"Executed Usuario_Aluno___Listar with status code {response.status_code}")

    @task
    def Usuario_Aluno___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('listStudents?page=1&perPage=7', headers=headers, name='Usuario_Aluno___Listar')
        print(f"Executed Usuario_Aluno___Listar with status code {response.status_code}")

    @task
    def Usuario_Aluno___Listar_por_nome(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('listStudentName?username=Jor&page=1&perPage=10', headers=headers, name='Usuario_Aluno___Listar_por_nome')
        print(f"Executed Usuario_Aluno___Listar_por_nome with status code {response.status_code}")

    @task
    def Histórico_de_compras___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getTransactionsAprovedStudent/454', headers=headers, name='Histórico_de_compras___Listar')
        print(f"Executed Histórico_de_compras___Listar with status code {response.status_code}")

    @task
    def Cupons___Criar(self):
        body = {

    "data": 

        {

                "percent": 15,

                "code": "CUP0N1",

                "amount": 20,

                "dateEnd": "2024-01-26",

                "userCompany": 111,

                "active": True

            }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('coupons', headers=headers, json=body, name='Cupons___Criar')
        print(f"Executed Cupons___Criar with status code {response.status_code}")

    @task
    def Cupons___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('coupons?populate=*', headers=headers, name='Cupons___Listar')
        print(f"Executed Cupons___Listar with status code {response.status_code}")

    @task
    def Cupons___Atualizar(self):
        body = {

    "data": 

        {

                "id": 1,

                "name": "Desconto de 15%",

                "percent": 15,

                "value": 50,

                "validate": "2023-10-26",

                "code": "CUP0N1",

                "description": "Desconto de 15%",

                "maximumUtilization": 1,

                "amount": 20,

                "dateStart": "2023-10-19",

                "dateEnd": "2023-10-26",

                "active": True

            }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('coupons/1', headers=headers, json=body, name='Cupons___Atualizar')
        print(f"Executed Cupons___Atualizar with status code {response.status_code}")

    @task
    def Cupons___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('coupons/1', headers=headers, name='Cupons___Excluir')
        print(f"Executed Cupons___Excluir with status code {response.status_code}")

    @task
    def Kit_Midia___Criar(self):
        body = {

	"name": "Material de Venda Teste2",

	"type": "pdf",

	"linkFile": None

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createKitMedia', headers=headers, json=body, name='Kit_Midia___Criar')
        print(f"Executed Kit_Midia___Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Kit_Midia(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Kit_Midia')
        print(f"Executed Salvar_Foto___Kit_Midia with status code {response.status_code}")

    @task
    def Deletar_Foto___Kit_Midia(self):
        body = {

    "data": {

        "user": 1

    }

}
        headers = self.get_headers()
        response = self.client.delete('upload/files/1', headers=headers, name='Deletar_Foto___Kit_Midia')
        print(f"Executed Deletar_Foto___Kit_Midia with status code {response.status_code}")

    @task
    def Kit_Midia___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('media-kits?populate=*', headers=headers, name='Kit_Midia___Listar')
        print(f"Executed Kit_Midia___Listar with status code {response.status_code}")

    @task
    def Kit_Midia___Deletar(self):
        body = {

	"data": 

		{

			    "id": 1,

				"registerDate": "2023-10-13",

				"name": "Material de Venda",

				"type": "pdf",

				"linkFile": None,

				"affiliate": "1",

				"company": "1"

		}



}
        headers = self.get_headers()
        response = self.client.delete('media-kits/1', headers=headers, name='Kit_Midia___Deletar')
        print(f"Executed Kit_Midia___Deletar with status code {response.status_code}")

    @task
    def Prêmio___Criar(self):
        body = {

    "data":

        {

                "code": "#1A256",

                "name": "Banner Mestres",

                "value": 100,

                "userRule": "1",

                "amount": 1,

                "active": True,

                "userCompany": "87",

                "type": "Avatar",

                "type_reward": 1,

                "publishedAt": "2023-12-04T17:54:34.684Z"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('rewards', headers=headers, json=body, name='Prêmio___Criar')
        print(f"Executed Prêmio___Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Prêmio(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Prêmio')
        print(f"Executed Salvar_Foto___Prêmio with status code {response.status_code}")

    @task
    def Deletar_Foto___Prêmio(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('upload/files/263', headers=headers, name='Deletar_Foto___Prêmio')
        print(f"Executed Deletar_Foto___Prêmio with status code {response.status_code}")

    @task
    def Prêmio___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('rewards?filters[userCompany]=147&populate=*', headers=headers, name='Prêmio___Carregar')
        print(f"Executed Prêmio___Carregar with status code {response.status_code}")

    @task
    def Tipo_de_Prêmio___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('type-rewards', headers=headers, name='Tipo_de_Prêmio___Carregar')
        print(f"Executed Tipo_de_Prêmio___Carregar with status code {response.status_code}")

    @task
    def Prêmio___Desativar(self):
        body = {
    "data": {
        "active": False
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('rewards/1', headers=headers, json=body, name='Prêmio___Desativar')
        print(f"Executed Prêmio___Desativar with status code {response.status_code}")

    @task
    def Prêmio___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('rewards/29', headers=headers, name='Prêmio___Excluir')
        print(f"Executed Prêmio___Excluir with status code {response.status_code}")

    @task
    def Regra_Conquista___Criar(self):
        body = {

	"data": 

		{

				"description": "Chegar a 25% do Curso",

				"conquestEmblem": "1"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('rule-emblems', headers=headers, json=body, name='Regra_Conquista___Criar')
        print(f"Executed Regra_Conquista___Criar with status code {response.status_code}")

    @task
    def Regra_Conquista___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('rule-emblems?populate=conquestEmblem.photo', headers=headers, name='Regra_Conquista___Listar')
        print(f"Executed Regra_Conquista___Listar with status code {response.status_code}")

    @task
    def Regra_Conquista___Atualizar(self):
        body = {

	"data": 

		{

            "id": 1,

				"description": "Chegar a 25% do Curso",

				"conquestEmblem": "1"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('rule-emblems/1', headers=headers, json=body, name='Regra_Conquista___Atualizar')
        print(f"Executed Regra_Conquista___Atualizar with status code {response.status_code}")

    @task
    def Emblema___Criar(self):
        body = {

    "data": 

        {

            "name": "Concluiu o Curso",

            "ruleEmblems": None

        }

    

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('conquest-emblems', headers=headers, json=body, name='Emblema___Criar')
        print(f"Executed Emblema___Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Emblema(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Emblema')
        print(f"Executed Salvar_Foto___Emblema with status code {response.status_code}")

    @task
    def Deletar_Foto___Emblem(self):
        body = {

    "data": {

        "user": 1

    }

}
        headers = self.get_headers()
        response = self.client.delete('upload/files/1', headers=headers, name='Deletar_Foto___Emblem')
        print(f"Executed Deletar_Foto___Emblem with status code {response.status_code}")

    @task
    def Emblema___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('conquest-emblems?filters[company]=1&populate=*', headers=headers, name='Emblema___Listar')
        print(f"Executed Emblema___Listar with status code {response.status_code}")

    @task
    def Emblema___Alterar(self):
        body = {

    "data": 

        {

                "name": "Concluiu o Curso",

                "ruleEmblems": None

        }

    

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('conquest-emblems/1', headers=headers, json=body, name='Emblema___Alterar')
        print(f"Executed Emblema___Alterar with status code {response.status_code}")

    @task
    def Emblema___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('conquest-emblems/1', headers=headers, name='Emblema___Excluir')
        print(f"Executed Emblema___Excluir with status code {response.status_code}")

    @task
    def Métodos_de_Pagamento___Criar(self):
        body = {

	"data": 

		{

				"payment_methods": ["1", "2"],

                "userCompany": "7",

                "publishedAt": "2023-12-04T18:34:01.354Z"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('payment-method-companies', headers=headers, json=body, name='Métodos_de_Pagamento___Criar')
        print(f"Executed Métodos_de_Pagamento___Criar with status code {response.status_code}")

    @task
    def Métodos_de_Pagamento___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('payment-method-companies?filters[company]=111&populate[1]=payment_methods', headers=headers, name='Métodos_de_Pagamento___Listar')
        print(f"Executed Métodos_de_Pagamento___Listar with status code {response.status_code}")

    @task
    def Métodos_de_Pagamento___Alterar(self):
        body = {

	"data": 

		{

                "id": 1,

				"payment_methods": ["1", "2"],

                "publishedAt": "2023-12-04T18:34:01.354Z"

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('payment-method-companies/1', headers=headers, json=body, name='Métodos_de_Pagamento___Alterar')
        print(f"Executed Métodos_de_Pagamento___Alterar with status code {response.status_code}")

    @task
    def Metodos_de_Pagamento___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('payment-methods?populate=*', headers=headers, name='Metodos_de_Pagamento___Listar')
        print(f"Executed Metodos_de_Pagamento___Listar with status code {response.status_code}")

    @task
    def Metodos_de_Pagamento___Alterar(self):
        body = {

	"data": 

		{

			    "id": 1,

				"active": True

        }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('payment-methods/1', headers=headers, json=body, name='Metodos_de_Pagamento___Alterar')
        print(f"Executed Metodos_de_Pagamento___Alterar with status code {response.status_code}")

    @task
    def StylePage___Alterar(self):
        body = {

	"data": 

		{

			"id": 1,

				"BackgroundColor": "Cinza",

				"colorBlocks": None,

				"colorDetails1": None,

				"colorDetails2": None,

				"colorMainText": None,

				"colorSecondaryText": None,

				"colorMain": None,

				"colorSecondary": None

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('page-styles/1', headers=headers, json=body, name='StylePage___Alterar')
        print(f"Executed StylePage___Alterar with status code {response.status_code}")

    @task
    def StylePage___Alterar_Copy(self):
        body = {

	"data": 

		{

            "user": "87",

				"BackgroundColor": "Cinza",

				"colorBlocks": None,

				"colorDetails1": None,

				"colorDetails2": None,

				"colorMainText": None,

				"colorSecondaryText": None,

				"colorMain": None,

				"colorSecondary": None

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('page-styles', headers=headers, json=body, name='StylePage___Alterar_Copy')
        print(f"Executed StylePage___Alterar_Copy with status code {response.status_code}")

    @task
    def Salvar_Foto___StylePage(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___StylePage')
        print(f"Executed Salvar_Foto___StylePage with status code {response.status_code}")

    @task
    def StylePage___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('page-styles?filters[user]=258&populate=photo', headers=headers, name='StylePage___Carregar')
        print(f"Executed StylePage___Carregar with status code {response.status_code}")

    @task
    def Chamado_Suporte_Master____Criar(self):
        body = {

        "message": "Não estou conseguindo acessar as minhas turmas"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createSupportMaster', headers=headers, json=body, name='Chamado_Suporte_Master____Criar')
        print(f"Executed Chamado_Suporte_Master____Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Suporte(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Suporte')
        print(f"Executed Salvar_Foto___Suporte with status code {response.status_code}")

    @task
    def Chamado_Suporte_Master___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[user]=7&filters[status][$containsi]=em aberto&populate=*', headers=headers, name='Chamado_Suporte_Master___Carregar')
        print(f"Executed Chamado_Suporte_Master___Carregar with status code {response.status_code}")

    @task
    def Cancelamento_de_Conta___Criar(self):
        body = {

     "message": "Quero encerrar a minha conta"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createCancelSupport', headers=headers, json=body, name='Cancelamento_de_Conta___Criar')
        print(f"Executed Cancelamento_de_Conta___Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Suporte(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Suporte')
        print(f"Executed Salvar_Foto___Suporte with status code {response.status_code}")

    @task
    def Cancelamento_de_conta___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[user]=32&filters[type][$eq]=Cancelamento&populate=*', headers=headers, name='Cancelamento_de_conta___Carregar')
        print(f"Executed Cancelamento_de_conta___Carregar with status code {response.status_code}")

    @task
    def Chamados_Suporte_Usuários___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests?filters[users][role]=4&filters[users][role]=1&populate=*', headers=headers, name='Chamados_Suporte_Usuários___Carregar')
        print(f"Executed Chamados_Suporte_Usuários___Carregar with status code {response.status_code}")

    @task
    def Chamado_Suporte___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('support-requests/148?populate=*', headers=headers, name='Chamado_Suporte___Carregar')
        print(f"Executed Chamado_Suporte___Carregar with status code {response.status_code}")

    @task
    def Chamados_Suporte___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('supportsCompany?supportId=1598&status=Solucionado&page=1&perPage=7', headers=headers, name='Chamados_Suporte___Listar')
        print(f"Executed Chamados_Suporte___Listar with status code {response.status_code}")

    @task
    def Respostas_Chamados___Criar_Copy(self):
        body = {

    "supportid": "88",

            "message": "aguuhopkd"

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('createAnswerSupport', headers=headers, json=body, name='Respostas_Chamados___Criar_Copy')
        print(f"Executed Respostas_Chamados___Criar_Copy with status code {response.status_code}")

    @task
    def Salvar_Foto___Resposta_Chamado(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Resposta_Chamado')
        print(f"Executed Salvar_Foto___Resposta_Chamado with status code {response.status_code}")

    @task
    def Respostas_Chamados___Listar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('answer-supports?filters[support_request]=66&populate=*', headers=headers, name='Respostas_Chamados___Listar_Copy')
        print(f"Executed Respostas_Chamados___Listar_Copy with status code {response.status_code}")

    @task
    def arquivo___baixar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('fileDownload?fileId=5737', headers=headers, name='arquivo___baixar')
        print(f"Executed arquivo___baixar with status code {response.status_code}")

    @task
    def Configuração_Pontuação___Alterar(self):
        body = {

	"data": 

		{

				"type": "Resposta Correta",

				"points": 40,

				"lesson": "1",

				"questions": "1"

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('scores/1', headers=headers, json=body, name='Configuração_Pontuação___Alterar')
        print(f"Executed Configuração_Pontuação___Alterar with status code {response.status_code}")

    @task
    def Configuração_Pontuação___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('scores?filters[company]=25&populate=*', headers=headers, name='Configuração_Pontuação___Carregar')
        print(f"Executed Configuração_Pontuação___Carregar with status code {response.status_code}")

    @task
    def Regra_Aprovação_Curso___Alterar(self):
        body = {

	"data": 

		{

				"type": "Porcentagem",

				"value": 70,

				"course": "2"

        }

}


        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('rule-approvals/1', headers=headers, json=body, name='Regra_Aprovação_Curso___Alterar')
        print(f"Executed Regra_Aprovação_Curso___Alterar with status code {response.status_code}")

    @task
    def Regra_Aprovação_Curso___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('rule-approvals?filters[company]=25&populate=*', headers=headers, name='Regra_Aprovação_Curso___Listar')
        print(f"Executed Regra_Aprovação_Curso___Listar with status code {response.status_code}")

    @task
    def Informações_de_Pagamento___Alterar(self):
        body = {

	"data": 

		{

            "value": 30,

            "active": True,

            "updatedAt": "2024-01-09T14:15:35.351Z"

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('payment-informations/1', headers=headers, json=body, name='Informações_de_Pagamento___Alterar')
        print(f"Executed Informações_de_Pagamento___Alterar with status code {response.status_code}")

    @task
    def Informações_de_Pagamento___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('payment-informations?filters[company]=27&populate=*', headers=headers, name='Informações_de_Pagamento___Listar')
        print(f"Executed Informações_de_Pagamento___Listar with status code {response.status_code}")

    @task
    def Configuração_Comissão_Afiliado___Alterar(self):
        body = {

	"data": 

		{

            "studentActive": False,

            "duration": 0,

            "limited": False,

            "paymentMethod": "Automatico",

            "updatedAt": "2024-01-09T14:15:32.715Z"

		}

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('rule-commissions/18', headers=headers, json=body, name='Configuração_Comissão_Afiliado___Alterar')
        print(f"Executed Configuração_Comissão_Afiliado___Alterar with status code {response.status_code}")

    @task
    def Configuração_Comissão_Afiliado___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('rule-commissions?filters[company]=27&populate=*', headers=headers, name='Configuração_Comissão_Afiliado___Carregar')
        print(f"Executed Configuração_Comissão_Afiliado___Carregar with status code {response.status_code}")

    @task
    def Regras_Inadimplentes__Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('rule-suspensions', headers=headers, name='Regras_Inadimplentes__Listar')
        print(f"Executed Regras_Inadimplentes__Listar with status code {response.status_code}")

    @task
    def Regras_Inadimplentes___Editar(self):
        body = {
    "data": {
        "name": "Regras de suspensão de inadimplentes",
        "value": 30,
        "active": True
    }
}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('rule-suspensions/1', headers=headers, json=body, name='Regras_Inadimplentes___Editar')
        print(f"Executed Regras_Inadimplentes___Editar with status code {response.status_code}")

    @task
    def Configuração_de_faturamento___Atualizar(self):
        body = {

	"data": 

		{

			"id": 1,

				"active": True,

				"value": 120000,

				"singlePayment": False,

				"access_period": "None"

		}

}	
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('billing-setups/1', headers=headers, json=body, name='Configuração_de_faturamento___Atualizar')
        print(f"Executed Configuração_de_faturamento___Atualizar with status code {response.status_code}")

    @task
    def Configuração_de_faturamento(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('billing-setups?filters[company]=42&populate=*', headers=headers, name='Configuração_de_faturamento')
        print(f"Executed Configuração_de_faturamento with status code {response.status_code}")

    @task
    def Período_de_Acesso(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('access-periods', headers=headers, name='Período_de_Acesso')
        print(f"Executed Período_de_Acesso with status code {response.status_code}")

    @task
    def Seção_Foto___Criar(self):
        body = {

    "data": {

    "border": 1,

    "section": "1",

    "title": "fghjkl",

    "description": "fivgdhskjdç",

    "valueOrder": 1

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('section-photos', headers=headers, json=body, name='Seção_Foto___Criar')
        print(f"Executed Seção_Foto___Criar with status code {response.status_code}")

    @task
    def Seção_Foto___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('section-photos?populate=*', headers=headers, name='Seção_Foto___Listar')
        print(f"Executed Seção_Foto___Listar with status code {response.status_code}")

    @task
    def Seção_Foto___Alterar(self):
        body = {

    "data": {

    "border": 1,

    "section": "1",

    "title": "fghjkl",

    "description": "fivgdhskjdç",

    "valueOrder": 1

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('section-photos/1', headers=headers, json=body, name='Seção_Foto___Alterar')
        print(f"Executed Seção_Foto___Alterar with status code {response.status_code}")

    @task
    def Seção_Foto___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('section-photos/1', headers=headers, name='Seção_Foto___Excluir')
        print(f"Executed Seção_Foto___Excluir with status code {response.status_code}")

    @task
    def Foto___Criar(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Foto___Criar')
        print(f"Executed Foto___Criar with status code {response.status_code}")

    @task
    def Foto___Deletar(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('upload/files/1', headers=headers, name='Foto___Deletar')
        print(f"Executed Foto___Deletar with status code {response.status_code}")

    @task
    def Button___Criar(self):
        body = {

    "data": {

    "colorBG": "ghjklç",

    "colorText": "sfgh",

    "colorBorder": "sdfghj",

    "section": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('buttons', headers=headers, json=body, name='Button___Criar')
        print(f"Executed Button___Criar with status code {response.status_code}")

    @task
    def Button___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('buttons?populate=*', headers=headers, name='Button___Listar')
        print(f"Executed Button___Listar with status code {response.status_code}")

    @task
    def Button___Alterar(self):
        body = {

    "data": {

    "colorBG": "ghjklç",

    "colorText": "sfgh",

    "colorBorder": "sdfghj",

    "section": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('buttons/1', headers=headers, json=body, name='Button___Alterar')
        print(f"Executed Button___Alterar with status code {response.status_code}")

    @task
    def Button___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('buttons/1', headers=headers, name='Button___Excluir')
        print(f"Executed Button___Excluir with status code {response.status_code}")

    @task
    def Seção___Criar(self):
        body = {

    "data": {

    "title": "ghjklç",

    "type": "photo",

    "description": "bloco 2",

    "laddingPageId": "2",

    "valueOrder": "2"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('sections', headers=headers, json=body, name='Seção___Criar')
        print(f"Executed Seção___Criar with status code {response.status_code}")

    @task
    def Seção___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('sections?populate=*', headers=headers, name='Seção___Listar')
        print(f"Executed Seção___Listar with status code {response.status_code}")

    @task
    def Seção___Alterar(self):
        body = {

    "data": {

    "title": "ghjklç",

    "type": "Teste 2",

    "description": "sgahihidj",

    "laddingPageId": "1",

    "valueOrder": "1"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('sections/1', headers=headers, json=body, name='Seção___Alterar')
        print(f"Executed Seção___Alterar with status code {response.status_code}")

    @task
    def Seção___Excluir(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('sections/1', headers=headers, name='Seção___Excluir')
        print(f"Executed Seção___Excluir with status code {response.status_code}")

    @task
    def Foto___Seção(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Foto___Seção')
        print(f"Executed Foto___Seção with status code {response.status_code}")

    @task
    def Deletar_Foto___Seção(self):
        body = None
        headers = self.get_headers()
        response = self.client.delete('upload/files/1', headers=headers, name='Deletar_Foto___Seção')
        print(f"Executed Deletar_Foto___Seção with status code {response.status_code}")

    @task
    def Ladding_Pages___Criar(self):
        body = {

    "data": {

    "title": "Teste Empresa",

    "description": "Landing Page",

    "link": "https://blog.postman.com/filtering-and-sorting-apis-using-the-postman-api/",

    "plansId": ["1"],

    "userCompany": "147"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('ladding-pages', headers=headers, json=body, name='Ladding_Pages___Criar')
        print(f"Executed Ladding_Pages___Criar with status code {response.status_code}")

    @task
    def Salvar_Foto___Ladding_Page(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.post('upload', headers=headers, json=body, name='Salvar_Foto___Ladding_Page')
        print(f"Executed Salvar_Foto___Ladding_Page with status code {response.status_code}")

    @task
    def Ladding_Pages___Carregar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('ladding-pages?populate=user.userCompany.user.cpf', headers=headers, name='Ladding_Pages___Carregar')
        print(f"Executed Ladding_Pages___Carregar with status code {response.status_code}")

    @task
    def Ladding_Pages___Carregar_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('ladding-pages?filters[userCompany]=1&populate=*', headers=headers, name='Ladding_Pages___Carregar_Copy')
        print(f"Executed Ladding_Pages___Carregar_Copy with status code {response.status_code}")

    @task
    def Ladding_Pages___Buscar_por_Id(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('ladding-pages?pagination[page]=1&pagination[pageSize]=2&filters[$and][1][userCompany]=147&filters[$and][2][id]=2&populate=*', headers=headers, name='Ladding_Pages___Buscar_por_Id')
        print(f"Executed Ladding_Pages___Buscar_por_Id with status code {response.status_code}")

    @task
    def Planos_da_Empresa(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('plans?filters[userCompany]=129&populate=courses,userCompany,plan_differentials', headers=headers, name='Planos_da_Empresa')
        print(f"Executed Planos_da_Empresa with status code {response.status_code}")

    @task
    def Planos_da_Empresa_Copy(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('plans?filters[userCompany][laddingPages]=1&populate=plan_differentials', headers=headers, name='Planos_da_Empresa_Copy')
        print(f"Executed Planos_da_Empresa_Copy with status code {response.status_code}")

    @task
    def Ladding_Pages___Atualizar(self):
        body = {

    "data": {

    "title": "Teste 2",

    "description": "sgahihidj",

    "link": "https://blog.postman.com/filtering-and-sorting-apis-using-the-postman-api/",

    "plansId": ["1"],

    "affiliate": "1",

    "date": "2023-10-11"

    }

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('ladding-pages/1', headers=headers, json=body, name='Ladding_Pages___Atualizar')
        print(f"Executed Ladding_Pages___Atualizar with status code {response.status_code}")

    @task
    def Alterar_Ordem___Blocos_Seção(self):
        body = {

    "orderSection": ["3","2"]

}
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('listSectionLandingPage?landingPageId=2', headers=headers, json=body, name='Alterar_Ordem___Blocos_Seção')
        print(f"Executed Alterar_Ordem___Blocos_Seção with status code {response.status_code}")

    @task
    def Contrato___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('contracts?filters[active]=true&populate=*&filters[user]=410', headers=headers, name='Contrato___Listar')
        print(f"Executed Contrato___Listar with status code {response.status_code}")

    @task
    def Contrato___Cancelar(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('cancelPlanCompany/156', headers=headers, json=body, name='Contrato___Cancelar')
        print(f"Executed Contrato___Cancelar with status code {response.status_code}")

    @task
    def Contrato___Alterar_Plano(self):
        body = None
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        response = self.client.put('changePlanCompany?planId=156', headers=headers, json=body, name='Contrato___Alterar_Plano')
        print(f"Executed Contrato___Alterar_Plano with status code {response.status_code}")

    @task
    def Pagamentos_e_Faturas(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('payments?code=', headers=headers, name='Pagamentos_e_Faturas')
        print(f"Executed Pagamentos_e_Faturas with status code {response.status_code}")

    @task
    def Pagamentos_e_Faturas_do_Plano(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('paymentsContract?code=&transactionId=8623', headers=headers, name='Pagamentos_e_Faturas_do_Plano')
        print(f"Executed Pagamentos_e_Faturas_do_Plano with status code {response.status_code}")

    @task
    def Download_Pagamento(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('generatePaymentInformation?transactionId=8623', headers=headers, name='Download_Pagamento')
        print(f"Executed Download_Pagamento with status code {response.status_code}")

    @task
    def Planos___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('masterSalesPlan', headers=headers, name='Planos___Listar')
        print(f"Executed Planos___Listar with status code {response.status_code}")

    @task
    def CompanyStudents_List(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getStudentCompany/3/7', headers=headers, name='CompanyStudents_List')
        print(f"Executed CompanyStudents_List with status code {response.status_code}")

    @task
    def CompanyStudents_Search_Filter(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getReturnFilteredStudents?username=&status=Adimplente&page=1&perPage=10', headers=headers, name='CompanyStudents_Search_/_Filter')
        print(f"Executed CompanyStudents_Search_/_Filter with status code {response.status_code}")

    @task
    def CompanyAffiliate_List(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCompanyAffiliateList?page=1&perPage=10', headers=headers, name='CompanyAffiliate_List')
        print(f"Executed CompanyAffiliate_List with status code {response.status_code}")

    @task
    def Contas_a_Receber___Afiliado(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getReturnFilteredAffiliates?username=&status=Não Pago&page=1&perPage=7', headers=headers, name='Contas_a_Receber___Afiliado')
        print(f"Executed Contas_a_Receber___Afiliado with status code {response.status_code}")

    @task
    def DashboarsCompanyFinancial_Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getdashboardCompanyFinancial', headers=headers, name='DashboarsCompanyFinancial_Listar')
        print(f"Executed DashboarsCompanyFinancial_Listar with status code {response.status_code}")

    @task
    def Dashboard___Curso_do_Aluno(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getDashStudentCourse?userid=84&courseId=683', headers=headers, name='Dashboard___Curso_do_Aluno')
        print(f"Executed Dashboard___Curso_do_Aluno with status code {response.status_code}")

    @task
    def Dashboard___Curso_do_Aluno_Problema(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getDashStudentCourse?userid=84&courseId=519', headers=headers, name='Dashboard___Curso_do_Aluno_Problema')
        print(f"Executed Dashboard___Curso_do_Aluno_Problema with status code {response.status_code}")

    @task
    def Gráfico_de_Aulas(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getGraphicLesson?userId=449&courseId=894', headers=headers, name='Gráfico_de_Aulas')
        print(f"Executed Gráfico_de_Aulas with status code {response.status_code}")

    @task
    def Dashboard___Conclusão_de_aula(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getDashLessons?userId=194&courseId=519', headers=headers, name='Dashboard___Conclusão_de_aula')
        print(f"Executed Dashboard___Conclusão_de_aula with status code {response.status_code}")

    @task
    def DashboarsCompany_Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCompany', headers=headers, name='DashboarsCompany_Listar')
        print(f"Executed DashboarsCompany_Listar with status code {response.status_code}")

    @task
    def DashboarsCompanyDate_Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('getCompanyDate?month=4&year=2024', headers=headers, name='DashboarsCompanyDate_Listar')
        print(f"Executed DashboarsCompanyDate_Listar with status code {response.status_code}")

    @task
    def Faturas___Listar(self):
        body = None
        headers = self.get_headers()
        response = self.client.get('contracts?payments?filters[contract][id][$eq]=1&populate=*', headers=headers, name='Faturas___Listar')
        print(f"Executed Faturas___Listar with status code {response.status_code}")
