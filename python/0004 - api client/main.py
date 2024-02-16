from api_client.api_client import APIClient


def main():
    # Criando uma instância do cliente de API com a URL base do serviço
    api_client = APIClient("https://api.chucknorris.io")
    
    response = api_client.request("GET", "jokes/random")
    
    # Exemplo de uso headers
    # headers = {"Authorization": "Bearer my_token", "Content-Type": "application/json"}

    # Exemplo de uso cookies
    # api_client = APIClient("https://api.example.com")
    # cookies = {"session_id": "1234567890"}
    # response = api_client.request("GET", "resource", cookies=cookies)
       
    status_code = response.status_code
    json_data = response.json()

    # Exemplo de GET
    print("Status:", status_code, "Resource data:", json_data)

    # Exemplo de POST
    # new_data = {"key": "value"}
    # response = api_client.request("POST", "resource", new_data)
    # print("POST response:", response)


if __name__ == "__main__":
    main()
