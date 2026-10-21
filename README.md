# 🎬 Projeto 4 | API de Filmes e Gêneros

### 🐍 Python/Django | IFB

**Desenvolvedoras:** Neidiman Raposo e Sarah Vilanova  
**Instituição:** Instituto Federal de Brasília (IFB)  
**Área:** Desenvolvimento Back-end com Python e Django  
**Projeto:** API REST para gerenciamento de filmes e gêneros  
**Ano:** 2026

---

## 📖 1. Apresentação do projeto

O **Projeto 4** consiste no desenvolvimento de uma API REST para gerenciamento de filmes e gêneros cinematográficos, utilizando Python, Django e Django REST Framework.

A aplicação permite consultar informações cadastradas e realizar operações de criação por meio de requisições HTTP, respeitando as regras de autenticação e permissão configuradas.

O projeto foi desenvolvido como atividade prática da formação em Python/Django, com o objetivo de aplicar os conhecimentos adquiridos durante as aulas, especialmente na construção de APIs, manipulação de dados e controle de acesso.

### 🎯 Objetivos

- Desenvolver uma API REST utilizando Django REST Framework.
- Organizar os dados de filmes e gêneros em modelos relacionados.
- Disponibilizar endpoints para consulta de informações.
- Trabalhar com requisições HTTP, incluindo `GET` e `POST`.
- Implementar autenticação de usuários.
- Utilizar autenticação por token.
- Controlar permissões de acesso às operações da API.
- Testar o comportamento da aplicação com usuários autenticados e não autenticados.

---

## 🛠️ 2. Tecnologias e ferramentas utilizadas

| Tecnologia | Finalidade |
|---|---|
| 🐍 Python | Linguagem de programação |
| 🌐 Django | Framework para desenvolvimento web |
| 🔗 Django REST Framework | Construção da API REST |
| 🗄️ SQLite | Banco de dados da aplicação |
| 🔐 Token Authentication | Autenticação por token |
| 💻 Visual Studio Code | Desenvolvimento e organização do código |
| 🐧 Ubuntu | Ambiente de desenvolvimento |
| 📦 Git | Controle de versões |
| 🌍 GitHub | Hospedagem do código-fonte |
| 🧪 cURL | Execução de testes HTTP pelo terminal |

---

## 📂 3. Estrutura do projeto

A organização principal dos arquivos é apresentada abaixo:

```text
projeto4/
│
├── filmes/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
│
├── projeto4/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── base_filmes.csv
├── importarDados.py
├── manage.py
├── README.md
└── requirements.txt
```

### Principais arquivos

| Arquivo | Descrição |
|---|---|
| `models.py` | Define a estrutura dos dados da aplicação |
| `serializers.py` | Realiza a serialização e validação dos dados da API |
| `views.py` | Contém as visualizações e operações disponibilizadas |
| `urls.py` | Organiza as rotas de acesso |
| `settings.py` | Armazena as configurações do projeto |
| `admin.py` | Configura a integração com o painel administrativo |
| `base_filmes.csv` | Arquivo com dados utilizados no projeto |
| `importarDados.py` | Script relacionado à importação dos dados |
| `requirements.txt` | Lista as dependências necessárias |
| `.gitignore` | Define arquivos e diretórios que não devem ser versionados |

---

## ⚙️ 4. Instalação e execução

### 4.1. Pré-requisitos

Para executar a aplicação localmente, é necessário ter instalado:

- Python;
- Git;
- Um terminal para executar os comandos.

### 4.2. Clonar o repositório

```bash
git clone https://github.com/NeidinhaRaposo/projeto4.git
```

Acessar a pasta:

```bash
cd projeto4
```

### 4.3. Criar e ativar o ambiente virtual

No Ubuntu ou em outra distribuição Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

> **Importante:** o ambiente virtual deve estar ativado antes da instalação das dependências e da execução do projeto.

### 4.4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4.5. Preparar o banco de dados

Executar as migrações:

```bash
python manage.py migrate
```

O projeto utiliza SQLite. O arquivo `db.sqlite3` não está incluído no repositório, pois é um banco de dados local.

Por isso, ao clonar o projeto, será necessário preparar o banco e cadastrar ou importar os dados utilizados nos testes.

### 4.6. Criar um usuário administrador

Para acessar o painel administrativo do Django, pode ser criado um superusuário:

```bash
python manage.py createsuperuser
```

O terminal solicitará as informações necessárias para o cadastro.

### 4.7. Iniciar o servidor

```bash
python manage.py runserver
```

Com o servidor em execução, a aplicação estará disponível em:

**http://127.0.0.1:8000/**

---

## 🎞️ 5. Endpoints da API

A API disponibiliza rotas para trabalhar com filmes, gêneros e autenticação.

| Método | Endpoint | Finalidade |
|---|---|---|
| `GET` | `/api/filmes/` | Consultar os filmes cadastrados |
| `GET` | `/api/filmes/{id}/` | Consultar um filme específico |
| `POST` | `/api/filmes/` | Cadastrar um filme, com autenticação |
| `GET` | `/api/generos/` | Consultar os gêneros cadastrados |
| `POST` | `/api/generos/` | Cadastrar um gênero, com autenticação |
| `POST` | `/api/token/` | Solicitar um token de autenticação |

### 🔎 Consulta de filmes

Endereço:

```text
http://127.0.0.1:8000/api/filmes/
```

Exemplo com cURL:

```bash
curl http://127.0.0.1:8000/api/filmes/
```

### 🎭 Consulta de gêneros

Endereço:

```text
http://127.0.0.1:8000/api/generos/
```

Exemplo:

```bash
curl http://127.0.0.1:8000/api/generos/
```

### 🎬 Consulta de um filme específico

```bash
curl http://127.0.0.1:8000/api/filmes/1/
```

O número representa o identificador do filme que será consultado.

---

## 🔐 6. Autenticação e controle de permissões

Uma das funcionalidades centrais do Projeto 4 é o controle de acesso às operações da API.

A aplicação foi testada utilizando uma usuária chamada **Aurora**, cadastrada no sistema para verificar o comportamento das permissões.

### 👤 Usuário autenticado

Ao realizar o login, a usuária pode acessar a interface navegável do Django REST Framework e utilizar os formulários disponíveis para as operações autorizadas.

Durante os testes, verificamos a disponibilização da operação `POST` nas páginas de filmes e gêneros.

### 🔓 Usuário não autenticado

Após realizar o logout, a consulta aos dados continua disponível, mas o formulário de criação deixa de ser apresentado na interface navegável.

Dessa forma, a aplicação diferencia as permissões de leitura e escrita.

### 🛡️ Painel administrativo

O acesso às operações administrativas depende de permissões específicas.

A usuária Aurora não recebeu permissões para visualizar ou modificar os modelos pelo painel administrativo do Django.

O gerenciamento administrativo completo fica reservado ao superusuário.

**Observação:** possuir autenticação para utilizar a API não significa ter autorização para administrar o sistema.

---

## 🔑 7. Autenticação por token

Além da autenticação pela interface do navegador, o projeto foi testado utilizando token.

O token permite identificar o usuário em requisições HTTP sem depender de uma sessão de navegador.

### Solicitação do token

Endpoint:

```text
POST /api/token/
```

Exemplo de requisição:

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -d "username=SEU_USUARIO" \
  -d "password=SUA_SENHA"
```

Após a autenticação, o token recebido pode ser utilizado nas requisições que exigem identificação.

### Envio do token

Exemplo de cabeçalho HTTP:

```text
Authorization: Token SEU_TOKEN
```

**Importante:** senhas e tokens reais não devem ser publicados no repositório.

---

## 🧪 8. Testes realizados

Durante o desenvolvimento, foram realizados testes tanto pela interface navegável do Django REST Framework quanto pelo terminal do Ubuntu.

### Teste 1: Consulta de filmes

**Método:** `GET`

Foi realizada uma requisição para consultar os filmes cadastrados.

**Resultado observado:** a API retornou os registros em formato JSON.

### Teste 2: Consulta individual

**Método:** `GET`

Foi realizada uma requisição utilizando o identificador de um filme.

**Resultado observado:** a API retornou os dados do registro solicitado.

### Teste 3: Autenticação por token

**Método:** `POST`

Foi enviada uma requisição ao endpoint de autenticação com credenciais de usuário.

**Resultado observado:** o sistema retornou um token para utilização nas requisições autenticadas.

### Teste 4: Cadastro de filme

**Método:** `POST`

Foi realizado o cadastro de um novo filme utilizando autenticação.

O filme utilizado no teste foi **Garota Exemplar (2014)**.

Exemplo dos dados cadastrados:

```json
{
  "titulo": "Garota Exemplar",
  "descricao": "Uma mulher desaparece misteriosamente e seu marido se torna o principal suspeito.",
  "ano_lancamento": 2014,
  "duracao": 149,
  "genero": 1
}
```

**Resultado observado:** a API confirmou a criação do registro, atribuindo o identificador `21` no banco de dados utilizado durante o teste.

### Teste 5: Permissões com login

Foi realizado o login com a usuária Aurora.

**Resultado observado:** a interface navegável apresentou o formulário e o botão `POST`, permitindo o envio de dados conforme as permissões configuradas.

### Teste 6: Permissões após logout

Após encerrar a sessão, as páginas da API foram acessadas novamente.

**Resultado observado:** os registros permaneceram disponíveis para consulta, mas o formulário `POST` deixou de aparecer.

### Teste 7: Acesso administrativo

Foi verificado o comportamento da usuária Aurora no painel administrativo do Django.

**Resultado observado:** o painel informou que a usuária não possuía permissões para visualizar ou editar os modelos administrativos.

### Resumo dos resultados

| Teste | Resultado |
|---|---|
| Consulta de filmes por `GET` | ✅ Realizado |
| Consulta individual por `GET` | ✅ Realizado |
| Consulta de gêneros | ✅ Realizado |
| Obtenção de token | ✅ Realizado |
| Cadastro de filme por `POST` | ✅ Realizado |
| Exibição do `POST` com login | ✅ Verificado |
| Ocultação do formulário após logout | ✅ Verificado |
| Restrição de permissões administrativas | ✅ Verificado |

---

## 🗃️ 9. Banco de dados e arquivos auxiliares

O projeto utiliza SQLite durante o desenvolvimento local.

Também estão presentes os arquivos:

- `base_filmes.csv`, contendo dados utilizados na atividade;
- `importarDados.py`, relacionado ao processo de importação desses dados.

Como o banco SQLite não é enviado ao GitHub, os dados existentes no ambiente original não aparecem automaticamente em uma nova instalação.

Para reproduzir os testes com os mesmos registros, é necessário preparar o banco e executar o procedimento de importação correspondente ao script do projeto.

---

## 📌 10. Boas práticas adotadas

Durante a organização do projeto, foram considerados alguns cuidados importantes:

- Separação entre a aplicação de filmes e as configurações gerais do Django.
- Utilização de serializers para representação dos dados.
- Definição de rotas específicas para acesso aos recursos.
- Uso de autenticação para operações protegidas.
- Diferenciação entre permissões da API e permissões administrativas.
- Utilização de ambiente virtual para isolar dependências.
- Registro das dependências no `requirements.txt`.
- Configuração de `.gitignore` para evitar o envio de arquivos locais e temporários.
- Versionamento do código-fonte utilizando Git e GitHub.

---

## 🎓 11. Considerações finais

O desenvolvimento do Projeto 4 permitiu aplicar, de maneira prática, conceitos importantes para a construção de aplicações back-end com Python e Django.

A atividade envolveu a organização dos modelos, disponibilização de endpoints REST, utilização de serializers, configuração de autenticação e realização de testes de requisições HTTP.

Um dos principais pontos trabalhados foi a distinção entre usuários autenticados e não autenticados, demonstrando como o controle de permissões contribui para proteger operações de alteração de dados.

Os testes realizados permitiram verificar o funcionamento das consultas, do cadastro de filmes, da autenticação por token e das restrições de acesso.

O projeto representa mais uma etapa do aprendizado em desenvolvimento de APIs REST, reunindo conhecimentos de programação, banco de dados, autenticação e versionamento de código.

---

## 👩‍💻 12. Desenvolvedoras

**Neidiman Raposo**  
**Sarah Vilanova**

**Residência em Python/Django**  
**Instituto Federal de Brasília (IFB)**

📅 **2026**

### 🔗 Repositório

[GitHub | Projeto 4: API de Filmes e Gêneros](https://github.com/NeidinhaRaposo/projeto4)

---

**Projeto desenvolvido para fins educacionais, como parte das atividades práticas da formação em Python/Django do IFB.**
