# database.py
import psycopg2
from datetime import datetime
from enum import Enum

class BackupStatus(Enum):
    INICIADO = "INICIADO"
    PARADO = "PARADO"
    ERRO = "ERRO"
    FECHADO = "FECHADO"

def setup_connection(config, log, mensagem_var):
    try:
        conn = psycopg2.connect(
            host=config["database"]["host"],
            port=config["database"]["port"],
            dbname=config["database"]["name"],
            user=config["database"]["user"],
            password=config["database"]["password"]
        )
        mensagem = "Conexão com o banco de dados estabelecida com sucesso."
        log(mensagem)
        mensagem_var.set(mensagem)
        create_backup_table(conn, log, mensagem_var)
        return conn
    except Exception as e:
        mensagem = f"Erro ao conectar ao banco de dados: {str(e)}"
        log(mensagem)
        mensagem_var.set(mensagem)
        return None

def create_backup_table(conn, log, mensagem_var):
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'backup')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            cursor.execute("""
                CREATE TABLE public.backup (
                    id SERIAL,
                    ativo INTEGER DEFAULT 0 NOT NULL,
                    databackup VARCHAR(40),
                    erro INTEGER DEFAULT 0 NOT NULL,
                    status VARCHAR(50),
                    mensagem VARCHAR(500),
                    CONSTRAINT backup_pkey PRIMARY KEY(id)
                )
            """)
            conn.commit()

            mensagem = "Tabela 'backup' criada com sucesso."
            log(mensagem)
            mensagem_var.set(mensagem)

            cursor.execute("""
                INSERT INTO backup(ativo,databackup,erro,status,mensagem) VALUES(0,now(),0,'','')
            """)
            conn.commit()

            mensagem = "Tabela 'backup' criada com sucesso."
            log(mensagem)
            mensagem_var.set(mensagem)

    except Exception as e:
        mensagem = f"Erro ao verificar/criar a tabela 'backup': {str(e)}"
        log(mensagem)
        mensagem_var.set(mensagem)

def update_backup(conn, ativo, erro, status, mensagem, log, mensagem_var):
    try:
        backup_data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor = conn.cursor()
        update_query = "UPDATE backup SET ativo = %s, databackup = %s, erro = %s, status = %s, mensagem = %s"
        cursor.execute(update_query,
                       (ativo, backup_data, erro, status.value if isinstance(status, Enum) else status, mensagem))
        conn.commit()

        mensagem = f"{update_query % (ativo, backup_data, erro, status.value if isinstance(status, Enum) else status, mensagem)}"
        log(mensagem)

    except Exception as e:
        mensagem = f"Erro ao atualizar a tabela 'backup': {str(e)}"
        log(mensagem)
        mensagem_var.set(mensagem)
