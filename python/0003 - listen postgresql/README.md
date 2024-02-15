# Monitor de Alterações em Banco de Dados PostgreSQL

Este é um projeto simples em Python que monitora as alterações em uma tabela específica de um banco de dados PostgreSQL e exibe uma mensagem quando ocorre qualquer alteração.

## Instalação

1. Clone o repositório:

`git clone https://github.com/seu-usuario/nome-do-repositorio.git`

2. Instale as dependências:

`pip install psycopg2`

## Configuração

Antes de executar o script, é necessário configurar as credenciais do banco de dados no arquivo `main.py`. Abra o arquivo `main.py` e substitua as informações de `DATABASE`, `USER`, `PASSWORD`, `HOST` e `PORT` pelas credenciais do seu banco de dados PostgreSQL.

Além disso, para capturar as notificações de alterações no banco de dados, você precisará configurar uma trigger no PostgreSQL. Execute o seguinte script SQL no seu banco de dados para criar a trigger:

```sql
CREATE OR REPLACE FUNCTION notify_event() RETURNS TRIGGER AS $$
DECLARE
    record RECORD;
    payload JSON;
BEGIN
    IF (TG_OP = 'DELETE') THEN
        record = OLD;
    ELSE
        record = NEW;
    END IF;

    payload = json_build_object('table', TG_TABLE_NAME,
                                'action', TG_OP,
                                'data', row_to_json(record));

    PERFORM pg_notify(TG_TABLE_NAME, payload::text);

    IF (TG_OP = 'DELETE') THEN
        RETURN OLD;
    ELSE
        RETURN NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_changed
AFTER INSERT OR UPDATE OR DELETE ON users
FOR EACH ROW EXECUTE PROCEDURE notify_event();
```

Substitua users pelo nome da sua tabela e users_changed pelo nome da sua trigger, se necessário. Esta trigger notificará o Python sobre alterações na tabela especificada.

## Uso

Para executar o monitor de alterações, basta executar o arquivo main.py:

`python main.py`

Isso iniciará o monitoramento das alterações na tabela especificada no arquivo main.py. Quando uma alteração ocorrer, uma mensagem será exibida no console.

## Contribuição

Contribuições são bem-vindas! Se você encontrar um problema ou desejar adicionar uma nova funcionalidade, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License.