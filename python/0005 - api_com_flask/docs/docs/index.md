# Documentação do Projeto Flask

## Configuração

- Crie o arquivo main.py.
- Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
- Ative o ambiente virtual:
    ```bash
    .\venv\Scripts\activate
    ```
- Instale o Flask:
    ```bash
    pip install flask
    ```

## Executando o Aplicativo

Após configurar o ambiente, você pode executar o aplicativo Flask com o seguinte comando:
```bash
python main.py
```

## Estrutura do Projeto
```bash
projeto/
├── main.py                              # Ponto de entrada da aplicação Flask.
├── config.json                          # Arquivo de configuração da aplicação.
└── app/                                 # Diretório principal da aplicação.
    ├── __init__.py                      # Inicializa o aplicativo Flask e configurações globais.
    ├── controllers/                     # Controladores para lidar com solicitações HTTP e lógica de negócios.
    │   ├── __init__.py
    │   ├── carros_controller.py
    │   └── clientes_controller.py
    ├── models/                          # Modelos para interagir com o banco de dados.
    │   ├── __init__.py
    │   ├── carros.py
    │   └── clientes.py
    ├── views/                           # Modelos de visualização relacionados a cada controlador.
    │   ├── __init__.py
    │   ├── carros/
    │   │   ├── index.html
    │   │   ├── detalhes.html
    │   │   ├── criar.html
    │   │   └── editar.html
    │   └── clientes/
    │       ├── index.html
    │       ├── detalhes.html
    │       ├── criar.html
    │       └── editar.html
    └── templates/                       # Arquivos de modelo Jinja2 para visualizações HTML.
        ├── base.html
        ├── layout.html
        └── outros_templates.html
```

## Contribuindo
Este projeto está aberto a contribuições. Sinta-se à vontade para criar problemas, enviar solicitações de recebimento ou contribuir com código para melhorar o projeto.
