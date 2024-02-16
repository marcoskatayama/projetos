# Cliente de API Python

Este é um cliente de API em Python que permite interagir com serviços web através de requisições HTTP.

## Como usar

### Instalação

1. Clone o repositório:

````bash
git clone https://github.com/seu-usuario/cliente-api-python.git
````

## Parâmetros opcionais

Você pode fornecer cabeçalhos (headers) ou cookies opcionais em suas requisições. Basta passá-los como argumentos adicionais para o método request.

````python
# Exemplo de uso headers
headers = {"Authorization": "Bearer my_token", "Content-Type": "application/json"}

# Exemplo de uso cookies
cookies = {"session_id": "1234567890"}

response = api_client.request("GET", "resource", headers=headers, cookies=cookies)
````

## Uso

Para executar o monitor de alterações, basta executar o arquivo main.py:

`python main.py`

Isso iniciará o monitoramento das alterações na tabela especificada no arquivo main.py. Quando uma alteração ocorrer, uma mensagem será exibida no console.

## Exemplos de uso

````python
from api_client.api_client import APIClient

def main():
    # Criando uma instância do cliente de API com a URL base do serviço
    api_client = APIClient("https://api.chucknorris.io")
    
    # Fazendo uma requisição GET para obter uma piada aleatória
    response = api_client.request("GET", "jokes/random")
       
    status_code = response.status_code
    json_data = response.json()

    # Exibindo o status da requisição e os dados recebidos
    print("Status:", status_code, "Resource data:", json_data)

if __name__ == "__main__":
    main()
````

## Contribuição

Contribuições são bem-vindas! Se você encontrar um problema ou desejar adicionar uma nova funcionalidade, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License.