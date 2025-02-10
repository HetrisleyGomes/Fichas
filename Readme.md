# Gerenciador de Atendimento e Recadastramento de Funcionários

Este projeto foi desenvolvido em Python para gerenciar o atendimento e o controle de funcionários a serem recadastrados pela gestão da cidade e municípios de São Paulo.

## Funcionalidades

O sistema oferece uma interface simples para a gestão dos recadastramentos de funcionários, permitindo que a equipe de administração da cidade e municípios de São Paulo realize o processo de forma eficiente e organizada.

## Requisitos

Para rodar este projeto, você precisa ter o Python 3.7+ instalado. Além disso, o projeto depende das seguintes bibliotecas:

- `bidict==0.23.1`
- `blinker==1.9.0`
- `click==8.1.8`
- `colorama==0.4.6`
- `Flask==3.1.0`
- `Flask-SocketIO==5.5.1`
- `h11==0.14.0`
- `itsdangerous==2.2.0`
- `Jinja2==3.1.5`
- `MarkupSafe==3.0.2`
- `python-engineio==4.11.2`
- `python-socketio==5.12.1`
- `simple-websocket==1.1.0`
- `Werkzeug==3.1.3`
- `wsproto==1.2.0`

## Instalação

### 1. Clone o repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
É recomendado criar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate   # No Windows use: venv\Scripts\activate
```

### 3. Instale as dependências
Instale as dependências do projeto utilizando o pip:

```bash
pip install -r requirements.txt
```

### 4. Execute o aplicativo
Para rodar o servidor, execute o seguinte comando:

```bash
python app.py
```
Isso iniciará o servidor Flask e o sistema estará disponível no endereço http://127.0.0.1:5000.


## Estrutura de Diretórios
O projeto possui a seguinte estrutura de diretórios:


```
/Cadastro
│

├── app.py         # Arquivo principal do aplicativo
├── src/               # Código fonte do aplicativo
│   ├── templates/     # Templates HTML usados pelo Flask
│   └── static/        # Arquivos estáticos como CSS, efeitos sonoros e imagens
│
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

## Contribuição
Contribuições são bem-vindas! Se você tiver alguma sugestão ou correção, fique à vontade para abrir uma issue ou enviar um pull request.

- Faça um fork deste repositório.
- Crie uma branch para a sua feature (git checkout -b feature/nova-feature).
- Commit suas mudanças (git commit -am 'Adiciona nova feature').
- Envie para o repositório remoto (git push origin feature/nova-feature).
- Abra um pull request.

## Licença
Este projeto está licenciado sob a MIT License.

```
Este modelo cobre as informações básicas para que os desenvolvedores e usuários saibam como instalar e executar o seu projeto. Adapte conforme necessário.
```


# Projeto de requisições de atendimento
Versão do Python 3.12.9

## Sobre o projeto
Este projeto Python foi desenvolvido para gerenciar o atendimento e controle de funcionários a serem recadastrados pela gestão da cidade e municipios de Monte Alegre.

Sistema por: @Hetrisley_Gomes.

## Estrtutura de Pastas
```
/static                 # Componentes estáticos
/templates              # Documentos HTML
run.py                  # Inicia o projeto, e controla suas requisições e rotas
```

## Tecnologias Usadas
- **venv**: Uma ferramenta integrada no Python para criar ambientes virtuais isolados, permitindo a instalação de dependências específicas do projeto sem interferir no sistema global.

- **Flask**: Um micro framework para Python que facilita o desenvolvimento de aplicações web rápidas e escaláveis com simplicidade e flexibilidade.

- **jQuery**: Uma biblioteca JavaScript que simplifica a manipulação do DOM, o tratamento de eventos e as chamadas Ajax, melhorando a compatibilidade entre navegadores.

- **Ajax**: Uma técnica para atualizar partes de uma página web de forma assíncrona sem recarregar a página inteira, proporcionando uma experiência de usuário mais dinâmica e interativa.

- **Bootstrap**: Um framework front-end que fornece um conjunto de ferramentas e componentes responsivos para criar layouts e design web consistentes e modernos

## Rodando Localmente
Clone do repositório:
```bash
git clone 
```


Instalando dependências:
```bash
pip install -r requirements.txt
```

Inicializando o ambiente virtual:
```bash
. .\.venv\Scripts\activate
```

Inicializando o servidor:
```bash
py run.py
```