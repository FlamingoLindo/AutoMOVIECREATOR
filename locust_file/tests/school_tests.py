from locust import HttpUser, task, between
import sys
import os

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(path_to_add)

from FUNCTIONS.Create_Name import create_random_name
from FUNCTIONS.Create_CPF import gera_e_valida_cpf 

class SchoolUser(HttpUser):
    wait_time = between(1, 5)
    host = 'https://moviecreator.mestresdaweb.io/api/'
    
    token = None
    
    def on_start(self):
         print(u'\033[0;32mStarting test!\033[0m')
         if not SchoolUser.token:
             SchoolUser.token = self.login()
             
    def on_stop(self):
        print(u'\033[0;32mTeste stoped!\033[0m')
        
    def login(self):
        body = {
            "identifier": "master@moviecreator.com",
            "password": "12345678"
        }
        try:
            response = self.client.post('auth/local', json=body, name = 'Login' )

            if response.status_code == 200:
                response_json = response.json()
                print("\033[1;33mLOGIN", response_json, "\033[0m")
                token = response_json.get('jwt') or response_json('refreshToken')
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
    def create_company(self):
        body = {
            "username": f"{create_random_name()}",
            "email": f"{create_random_name()}@gmail.com",
            "cpf": f"{gera_e_valida_cpf()}",
            "password": "12345678",
            "phone": "(11) 91234-5678",
            "visible": True
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post("createCompany", json=body, name='Empresa - Registrar')

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
        response = self.client.post("auth/forgot-password", json=body, headers=headers, name='Esqueci a Senha')

    @task
    def load_school(self):
        body = {
            "id": 7,
            "username": "Company Teste",
            "email": "company@gmail.com",
            "phone": None
        }
        headers = self.get_headers()
        response = self.client.get('users?filters[id]=104&populate[0]=company&populate[1]=role', json=body, headers=headers, name='Usuario Empresa - Carregar')
    
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
        response = self.client.put('updateBankData', json=body, headers=headers, name='Dados Bancários - Cadastrar')
        
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
        response = self.client.get('clients?filters[user]=147', json=body, headers=headers, name='Dados Bancários - listar')
        
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
        response = self.client.post('createAddressCompany', json=body, headers=headers, name='Endereço - Criar')
        
    @task
    def load_adress(self):
        headers = self.get_headers()
        response = self.client.get('addresses?filters[company][userCompany]=276&populate=*', headers=headers, name='Endereço - Carregar')
        
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
        response = self.client.put('updatedAddressCompany', json=body, headers=headers, name='Endereço - Atualizar')
        
    @task
    def list_credit_card(self):
        headers = self.get_headers()
        response = self.client.get('myCards', headers=headers, name='Cartão - Listar')
        
    @task
    def fav_card(self): 
        headers = self.get_headers()
        response = self.client.put('setFavoriteCards/392', headers=headers, name='Cartão - Favoritar')
        
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
        response = self.client.post('insertTransactionItemCompany', headers=headers, name='Carrinho - Inserir Item')
        
        
    @task
    def show_bought_items(self):
        headers = self.get_headers()
        response = self.client.get('getMyExtract?page=1&perPage=10', headers=headers, name='Extrato - Listar')
        
    @task
    def get_transactions(self):
        headers = self.get_headers()
        response = self.client.get('transactions?filters[user}=147', headers=headers, name='Listar todas transações')

    @task
    def create_tag(self):
        body = {
            "data": {
                "name": "tag",
                "course": "6",
                "publishedAt": "2023-12-06T13:59:51.147Z"
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('tags', headers=headers, json=body, name='Curso - Criar Tags')
        
    @task
    def create_module_no_course(self):
        body = {
            "data": 
            {
                    "name": "Introdução",
                    "lessons": ["1"],
                    "userProfessors": ["1"],
                    "valueOrder": 1
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('modules',headers=headers, json=body, name='Modulo - Criar')
        
    @task
    def load_modules(self):
        response = self.client.get('modules', name='Modulo - Carregar')
        
    @task 
    def edit_module(self):
        body = {
            "data": 
            {
                "id": 787,
                "course": "6",
                "user": "73",
                "valueOrder": 1
            } 
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('modules/787', headers=headers, json=body, name='Modulo - Editar')
        
    @task
    def create_written_class(self):
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
        headers["Content-Type"] = "application/json"
        response = self.client.post('lesson-files', headers=headers, json=body, name = 'Arquivo da Aula - Criar')

    @task
    def list_written_class(self):
        headers = self.get_headers()
        response = self.client.get('lesson-files', headers=headers, name='Arquivo da Aula - Listar')
        
    @task 
    def edit_written_class(self):
        body = {
            "data": {
                "type": "video",
                "title": "teste2",
                "description": "Você está pronto!",
                "linkFile": "https://www.youtube.com/watch?v=h1Kp9x_ADZwg",
                "lesson": "5",
                "scoreFile": 10,
                "valueOrder": "4"
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('lesson-files/11', headers=headers, json=body, name = 'Texto Aula - Editar')
        
    @task 
    def create_question_alternative(self):
        body = {
            "data": {
            "description": "Questão 1 ",
            "isCorrect": "true"
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('alternatives', headers=headers, json=body, name='Alternativas de Questão - Criar')
        
    @task 
    def create_questions(self):
        body = {
            "data": {
                        "title": "Questão 1 ",
                        "description": "aHJHGSFDS",
                        "linkMaterial": None,
                        "alternatives": ["2"]
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('questions', headers=headers, json=body, name = 'Questões - Criar')
        
    @task
    def create_lesson(self):
        body = {
            "data": {
                "name": "Aula Teste",
                "description": "Aprensentação e configuração de projeto",
                "duration": "20",
                "forums": None,
                "fileClasses": None,
                "creatorName": "Movie Creator"
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('lessons', headers=headers, json=body, name='Aula - Criar')

    @task
    def load_lesson(self):
        headers = self.get_headers()
        response = self.client.get('lessons/5?populate=*', headers=headers, name='Aula - Carregar')
        
    @task
    def load_pendencies(self):
        headers = self.get_headers()
        response = self.client.get('lessons?filters[module][id]=200&filters[status][$containsi]=pendente&populate=*', headers=headers, name='Aulas - Pendentes')
        
    @task
    def edit_lesson(self):
        body = {
            "data": {
                "id": 6,
                "name": "Conclusão",
                "description": "Formatura!!! Você não precisa mais de nada!",
                "fileClasses": [11]
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('lessons/6', headers=headers, json=body, name='Aula - Editar')
        
    @task 
    def create_test_alternative(self):
        body = {
            "data": {
                "description": "Questão 1 ",
                "isCorrect": "true"
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('alternatives', headers=headers,json=body, name="Alternativas de Questão - Criar")
        
    @task
    def create_test_question(self):
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
        headers["Content-Type"] = "application/json"
        response = self.client.post('questions', headers=headers,json=body, name="Questões - Criar")
        
    @task
    def create_exam(self):
        body = {
            "data":{
                    "name": "Prova Teste 2",
                    "score": 10,
                    "status": "Em análise",
                    "numberAttempts": 1,
                    "module": "799",
                    "examBlocks": ["1","2"],
                    "userCompany": 147
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('exams', headers=headers,json=body, name="Provas - Criar")
        
    @task(3)
    def update_exam(self):
        body = {
            "data": {
                "name": "Prova 1",
                "score": 1000,
                "status": "Em aberto",
                "numberAttempts": 3,
                "registerDate": '2023-09-10T10:30:00.000Z',
                "module": "799",
                "questions": ["1","2"],
                "userProfessor": "1"
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('exams/1', headers=headers,json=body, name="Provas - Alterar")
        
    @task
    def get_pending_exams(self):
        headers = self.get_headers()
        if not headers.get('Authorization'):
            print("Erro: Token de autenticação não encontrado nos cabeçalhos.")
            return
        
        response = self.client.get('exams?filters[userCompany]=1756&filters[status][$containsi]=pendente', name="Provas - Pendentes")
        
    @task
    def load_tests(self):
        headers = self.get_headers()
        response = self.client.get('exams/42', headers=headers, name="Provas - Carregar")
      
    @task
    def get_question_answer(self):
        headers = self.get_headers()
        if not headers.get('Authorization'):
            print("Erro: Token de autenticação não encontrado nos cabeçalhos.")
            return
        
        response = self.client.get('answer-questions/3', headers=headers, name="Respostas da questão")
        
    @task
    def get_course_exams(self):
        headers = self.get_headers()
        if not headers.get('Authorization'):
            print("Erro: Token de autenticação não encontrado nos cabeçalhos.")
            return
        
        response = self.client.get('getExamsCompany?courseId=20626', name="Provas - Curso")
        
            
    @task
    def get_exams_from_course(self):
        headers = self.get_headers()
        if not headers.get('Authorization'):
            print("Erro: Token de autenticação não encontrado nos cabeçalhos.")
            return
        
        response = self.client.get('exams?filters[module][course]=20626', name="Provas - Carregar do curso")
       
    @task
    def load_exams_from_course(self):
        headers = self.get_headers()
        response = self.client.get('modules?populate=exams.take_tests&filters[course]=20626', name="Provas dos Cursos - Carregar")

    @task 
    def add_exam_correction(self):
        body = {
            "data": {
                "comment": "Teste Correção",
                "date": "2023-10-23",
                "question": "1",
                "user": "7"
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('corrections', headers=headers, json = body, name = 'Corrigir Questões - Criar')
        
    @task 
    def list_exam_corrections(self):
        headers = self.get_headers()
        response = self.client.get('corrections', headers=headers, name = 'Corrigir Questões Curso - Listar')
        
    @task 
    def create_class(self):
        body = {
            "period": "Matutino",
            "name": f"{create_random_name()}",
            "courses": ["20626"]
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('createClass', headers=headers, json = body, name = 'Turmas - Criar')
        
    @task
    def list_classes(self):
        headers = self.get_headers()
        response = self.client.get('classes?filters[userCompany]=147&populate=*', headers=headers, name= 'Turmas - Listar')
    
    @task 
    def update_class(self):
        body = {
            "data": 
                    {
                        "period": "Noite",
                    	"name": "Turma 1",
                    	"courses": "20626",
                        "userStudent": ["8"]	
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('classes/1', json = body, headers=headers, name = 'Turmas - Alterar')
        
    @task
    def create_forum(self):
        body = {
            "data": {
                "comment": "Comentario",
                "lesson":1,
                "user": 73
            }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('forums', json = body, headers=headers, name='Forum - Criar')

    """
    @task
    # this one does not work, so yeah dont worry if you see an error
    def load_forum(self):
        headers = self.get_headers()
        response = self.client.get('forums?populate=forum_answers.user&populate=lesson&populate=user&filters[lesson][course][id]=20626', headers=headers, name='Forum - Carregar')
    """
    
    @task
    def create_certificate(self):
        body = {
            "data": 
                    {
                        "title": "Teste",
                        "code": "1234##"
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('certificates', json = body, headers=headers, name= 'Certificado - Criar')
        
    @task
    def load_certificates(self):
        headers = self.get_headers()
        response = self.client.get('certificates', headers=headers, name = 'Certificado - Carregar')
    
    @task
    def edit_certificate(self):
        body = {
            "data": 
                    {
                        "title": "Teste",
                        "code": "1234##"
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('certificates/362', json = body, headers=headers, name= 'Certificado - Editar')  
        
    @task 
    def create_course(self):
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
        headers["Content-Type"] = "application/json"
        response = self.client.post('courses', json = body, headers=headers, name= 'Cursos - Criar') 
    
    @task
    def get_company_courses(self):
        headers = self.get_headers()
        response = self.client.get('getCoursesCompany?name=&status=&page=1&perPage=7', headers=headers, name = 'Cursos - Carregar')
        
    @task
    def get_company_pending(self):
        headers = self.get_headers()
        response = self.client.get('getCoursesCompanyPendenting?page=1&perPage=15', headers=headers, name = 'Cursos - Em analise')
        
    @task
    def get_company_published(self):
        headers = self.get_headers()
        response = self.client.get('courses?filters[$and][1][userCompany]=410&filters[$and][2][status]=Publicado', headers=headers, name = 'Cursos - Publicado')
        
    @task
    def list_student_course(self):
        headers = self.get_headers()
        response = self.client.get('courses?populate=*', headers=headers, name = 'Cursos - Listar Alunos')
        
    @task
    def list_student_pack(self):
        headers = self.get_headers()
        response = self.client.get('courses?filters[$and][1][userCompany]=147&filters[$and][2][status][$ne]=Em análise', headers=headers, name = 'Cursos - Pacote')
        
    @task
    def list_exam_course(self):
        headers = self.get_headers()
        response = self.client.get('modules?filters[course]=20626&populate=*', headers=headers, name = 'Cursos - Listar Provas')
    
    @task
    def list_exam_course(self):
        headers = self.get_headers()
        response = self.client.get('getNewStudentsCourse?courseId=20626&page=2&perPage=7', headers=headers, name = 'Cursos - Listar Alunos não Vinculados') 
    
    @task
    def add_student_course(self):
        body = {
            "studentId": 463
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('addStudentCourse?courseId=20626', headers=headers, json=body, name = 'Curso - Adicionar aluno') 
        
    @task
    def duplicate_course(self):
        headers = self.get_headers()
        response = self.client.put('doubleCourse/20626', headers=headers, name = 'Curso - Duplicar') 
        
    @task
    def list_course_ratings(self):
        headers = self.get_headers()
        response = self.client.get('course-evaluations?filter[course]=2&populate=*', headers=headers, name = 'Avaliação dos Cursos - Listar') 
        
    @task
    def list_course_rating(self):
        headers = self.get_headers()
        response = self.client.get('getCourseEvaluation?courseId=554', headers=headers, name = 'Avaliação - Nota do Curso') 
        
    @task
    def list_course_students(self):
        headers = self.get_headers()
        response = self.client.get('getStudentsCourse?courseId=20626&name=&status=&page=1&perPage=10', headers=headers, name = 'Alunos do Curso') 
        
    @task
    def create_category(self):
        body = {
            "data": 
                {
                        "name": "Node",
                        "active": True
                }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('createCategory', headers=headers, json=body, name = 'Categoria - Criar') 
        
    @task
    def list_categories(self):
        headers = self.get_headers()
        response = self.client.get('categories?filters[userCompany]=7', headers=headers, name = 'Categorias - Listar') 
        
    @task
    def create_diff_plan(self):
        body = {
            "data": 
                    {
                        "description": "Acesso livre ao curso após a compra",
                        "plans": ["335"],
                        "publishedAt": "2023-12-06T13:59:51.147Z"
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('plan-differentials', headers=headers, json=body, name = 'Plano Differenciais - Criar')
        
    @task
    def create_plan(self):
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
        headers["Content-Type"] = "application/json"
        response = self.client.post('plans', headers=headers, json=body, name = 'Plano - Criar') 
        
    @task
    def load_plans(self):
        headers = self.get_headers()
        response = self.client.get('getCompanyPlans', headers=headers, name = 'Plano - Carregar')
        
    @task
    def list_published_courses(self):
        headers = self.get_headers()
        response = self.client.get('coursesCompanyId', headers=headers, name = 'Cursos - Publicados Listar')
        
    @task
    def list_company_plans(self):
        headers = self.get_headers()
        response = self.client.get('plansCompanyId', headers=headers, name = 'Planos - Criados Listar')
        
    @task
    def create_course_pack(self):
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
        headers["Content-Type"] = "application/json"
        response = self.client.post('packages', headers=headers, json=body, name = 'Pacotes - Criar') 
        
    @task
    def list_packs(self):
        headers = self.get_headers()
        response = self.client.get('packages?filters[userCompany]=7&populate=*', headers=headers, name = 'Pacotes - Listar')
        
    @task
    def list_signature_types(self):
        headers = self.get_headers()
        response = self.client.get('type-signatures?sort[id]=asc', headers=headers, name = 'Tipo de assinatura')
        
    @task
    def show_terms(self):
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=termo&populate=*', headers=headers, name = 'Termo Uso - Exibir')
        
    @task
    def show_politcs(self):
        headers = self.get_headers()
        response = self.client.get('terms?filters[$or][0][type][$containsi]=politica&populate=*', headers=headers, name = 'Politica Privacidade - Exibir')
    
    @task
    def create_proff(self):
        body = {
            "data": 
                {
                    "username":f"{create_random_name()}",
                    "email":f"{create_random_name()}@gmail.com",
                    "cpf": f"{gera_e_valida_cpf()}",
                    "password":"12345678",
                    "function": "fghjklç"
                }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('createProfessor', headers=headers, json=body, name = 'Novo Usuario Professor - Criar') 
        
    @task
    def edit_proff(self):
        body = {
            "data": 
                {
                    "username": f"{create_random_name()}",
                    "email": f"{create_random_name()}@gmail.com",
                    "password":"12345678",
                    "cpf": None,
                    "phone": None,
                    "role": "5"
                }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('users/3281', headers=headers, json=body, name = 'Usuario Professor - Atualizar') 
        
    @task
    def edit_proff_func(self):
        body = {
            "function": "Professor"
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('professors/1', headers=headers, json=body, name = 'Usuario Professor - Atualizar Função') 
        
    @task
    def list_proffs(self):
        headers = self.get_headers()
        response = self.client.get('listEmployees?page=1&perPage=10', headers=headers, name = 'Usuario Professor - Listar')
        
        
    @task
    def create_stu(self):
        body = {
            "username":f"{create_random_name()}",
            "email":f"{create_random_name()}@gmail.com",
            "cpf": f"{gera_e_valida_cpf()}",
            "password":"12345678",
            "grade": []
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('createStudentCompany', headers=headers, json=body, name = 'Novo Usuario Aluno - Criar') 
    
    @task
    def edit_stu(self):
        body = {
            "classesStudent": ["2", "84"]
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.put('users/73', headers=headers, json=body, name = 'Usuario Aluno - Atualizar') 
        
    @task
    def list_stud(self):
        headers = self.get_headers()
        response = self.client.get('users?populate=*', headers=headers, name = 'Usuario Aluno - Listar')
        
    @task
    def create_cupon(self):
        body = {
            "data": 
                {
                        "percent": 15,
                        "code": f"{create_random_name()}",
                        "amount": 20,
                        "dateEnd": "2024-01-26",
                        "userCompany": 111,
                        "active": True
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('coupons', headers=headers, json=body, name = 'Cupons - Criar')
        
    @task
    def list_cupon(self):
        headers = self.get_headers()
        response = self.client.get('coupons?populate=*', headers=headers, name = 'Cupons - Listar')
        
    @task
    def edit_cupon(self):
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
        headers["Content-Type"] = "application/json"
        response = self.client.put('coupons/1', headers=headers, json=body, name = 'Cupons - Atualizar')
        
    @task
    def list_kit_midia(self):
        headers = self.get_headers()
        response = self.client.get('media-kits?populate=*', headers=headers, name = 'Kit Midia - Listar')
        
    @task
    def create_prize(self):
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
        headers["Content-Type"] = "application/json"
        response = self.client.post('rewards', headers=headers, json=body, name = 'Prêmio - Criar')
        
    @task
    def load_prize(self):
        headers = self.get_headers()
        response = self.client.get('rewards?filters[userCompany]=147&populate=*', headers=headers, name = 'Prêmio - Carregar')
    
    @task
    def create_achv(self):
        body = {
            "data": 
                {
                        "description": r"Chegar a 25% do Curso",
				        "conquestEmblem": "1"
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('rule-emblems', headers=headers, json=body, name = 'Regra Conquista - Criar')
        
    @task
    def list_achv(self):
        headers = self.get_headers()
        response = self.client.get('rule-emblems?populate=conquestEmblem.photo', headers=headers, name = 'Regra Conquista - Listar')
        
    @task
    def create_emblem(self):
        body = {
            "data": 
                {
                        "name": "Concluiu o Curso",
                        "ruleEmblems": None
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('conquest-emblems', headers=headers, json=body, name = 'Emblema - Criar')
        
    @task
    def list_emblem(self):
        headers = self.get_headers()
        response = self.client.get('conquest-emblems?filters[company]=1&populate=*', headers=headers, name = 'Emblema - Listar')
        
    @task
    def create_payment_method(self):
        body = {
            "data": 
                {
                        "payment_methods": ["1", "2"],
                        "userCompany": "7",
                        "publishedAt": "2023-12-04T18:34:01.354Z"
                    }
        }
        headers = self.get_headers()
        headers["Content-Type"] = "application/json"
        response = self.client.post('payment-method-companies', headers=headers, json=body, name = 'Métodos de Pagamento - Criar')
        
    @task
    def list_payment_methods(self):
        headers = self.get_headers()
        response = self.client.get('payment-method-companies?filters[company]=111&populate[1]=payment_methods', headers=headers, name = 'Métodos de Pagamento - Listar')