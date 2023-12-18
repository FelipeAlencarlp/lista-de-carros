# Projeto Lista de Carros Python com ReactJS

- Python back-end
- ReactJS front-end
- Banco de Dados SQLite

Os projetos estão separados por pastas com os nomes, backend e frontend.


# BackEnd (Python)

ANTES DE EXECUTAR QUALQUER COMANDO ABAIXO, CERTIFIQUE-SE DE TER EM SUA MÁQUINA A VERSÃO 3 DO PYTHON!!
SE FOR UTILIZAR O PROJETO NO VSCODE CERIFIQUE-SE DE TER A SEGUINTE EXTENSÃO:
    PYTHON - INTELLISENSE (o VSCode precisa dessa extensão para reconhecer arquivos em .py)

# Para iniciar o projeto no backend, basta seguir os passos:
1 - Navegue até a pasta do projeto, é possível através do próprio terminal:

# Windows:
– No seu teclado, pressione a tecla Windows + R para abrir a caixa de diálogo Executar.
– Digite “cmd” e pressione Enter para abrir o Prompt de Comando.
– no terminal navegue até a pasta que está o projeto utilizando o comando "cd /SeuDiretórioOndeEstaOprojeto/backend"

# Linux:
– No seu teclado, pressione as teclas CTRL + ALT + T para abrir um novo terminal
– no terminal navegue até a pasta que está o projeto utilizando o comando "cd /SeuDiretórioOndeEstaOprojeto/backend"

2 - criar a pasta .venv com o seguinte comando dentro da pasta /backend:
    python3 -m venv venv

- Com as pasta criada basta acessá-la com o seguinte comando:
    source venv/bin/activate

- Em seguida é preciso instalar todas as dependências que estão em requirements.txt com o comando:
    pip install -r requirements.txt

-Por último basta iniciar o projeto com o comando:

    Linux:
    uvicorn main:app --reload

    Windows:
    python -m uvicorn main:app --reload


# OBS: 

O Banco de Dados utilizado no projeto foi o SQLite, quando iniciar o projeto ele vai criar um banco de dados automático na sua máquina chamdo carros.db e junto com a criação do banco de dados um usuário ADMIN.

Credênciais do Admin:
email: "admin@carros.com"
password: "secret123"

1 - Para acessar o banco de dados, é possível através do próprio terminal:

# Windows:
– No seu teclado, pressione a tecla Windows + R para abrir a caixa de diálogo Executar.
– Digite “cmd” e pressione Enter para abrir o Prompt de Comando.
– no terminal navegue até a pasta que está o projeto utilizando o comando "cd /SeuDiretórioOndeEstaOprojeto/backend" e digite sqlite3;

# Linux:
– No seu teclado, pressione as teclas CTRL + ALT + T para abrir um novo terminal
– no terminal navegue até a pasta que está o projeto utilizando o comando "cd /SeuDiretórioOndeEstaOprojeto/backend" e digite sqlite3;

– agora que está dentro do sqlite3 basta abrir o banco de dados com o seguinte comando

  sqlite> .open carros.db
  (com esse comando você já vai estar dentro do banco de dados carros)

– para visualizar as tabelas criadas

  sqlite> .tables
  (esse comando retorna as tabelas criadas que são "users" e "cars")

– para sair do sqlite

  sqlite> .exit

2 – A segunda opção para acessar o banco de dados é a utilização de algum programa para ler o banco de dados:
– um exemplo de programa seria o Beekeeper Studio no seguinte link

  https://www.beekeeperstudio.io/get

– ao realizar o download e instalação, abra o programa e clice em New Connection
– escolha em connection type a opção SQLite
– agora basta localizar onde se encontra o arquivo chamado carros.db e iniciar.



# FrontEnd (ReactJs)

- Node Versão 20.5.1

# Para iniciar o projeto no front, basta seguir os passos:

1 - certifique-se de que o projeto backend esteja funcionando;
2 - com o terminal aberto, navegue até a pasta dentro do projeto chamada de 'frontend';
3 - ainda no terminal dentro da pasta digite o seguinte comando:
    npm install   -> esse comando garntirá que todas as dependências necessárias para funcionamento
                     do projeto sejam instaladas
4 - ao finalizar a instalação de todas as dependências basta iniciar o projeto com o seguinte comando:
    npm start   -> esse comando inicia o projeto com uma nova aba em seu navegador, basta aguardar.

# OBS:

Lembrando que para total funcionamento de ambos os lados 'backend' e 'frontend', os dois projetos tem que estar funcionando localmente em sua máquina, através dos comando fornecidos nos passos acima.

