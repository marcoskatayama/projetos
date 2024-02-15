import select
import psycopg2
import psycopg2.extensions

# Conecte ao seu banco de dados
conn = psycopg2.connect(
    database="nome do banco",
    user="usuario",
    password="password",
    host="localhost",
    port="5432")

# Coloque a conexão em modo autocommit.
# Isso significa que cada comando SQL
# será executado em sua própria
# transação e será automaticamente confirmado.
conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

# Crie um cursor conectado ao PostgreSQL
cur = conn.cursor()

# Execute o comando LISTEN
# Isso faz com que a sessão atual do PostgreSQL
# “escute” as notificações no canal especificado,
# neste caso, "users". Substitua pelo nome da tabela desejada.
cur.execute("LISTEN users;")

# Crie um loop enquanto aguarda por notificações
while True:
    # Se houver uma notificação disponível, extraia-a
    # A função select.select() é usada para aguardar
    # até que a conexão do banco de dados esteja pronta
    # para leitura (ou seja, quando uma notificação é recebida)
    # com um timeout de 5 segundos.
    if select.select([conn], [], [], 5) == ([], [], []):
        print("Escutando...")
    else:
        # Se uma notificação for recebida, conn.poll() é chamado
        # para processar as notificações e, em seguida,
        # cada notificação é removida da fila de notificações e impressa.
        conn.poll()
        while conn.notifies:
            notify = conn.notifies.pop(0)
            print("Got NOTIFY:", notify.pid, notify.channel, notify.payload)
