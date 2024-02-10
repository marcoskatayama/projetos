# ui.py
import tkinter as tk
from ttkthemes import ThemedStyle
from tkinter import ttk
from datetime import datetime
from database import BackupStatus
from logger import Logger

class BackupAppUI:
    def __init__(self, root, logger_func, mensagem_var, config, db_functions):
        self.root = root
        self.logger_func = logger_func
        self.mensagem_var = mensagem_var
        self.config = config
        self.db_functions = db_functions
        self.process = None
        self.logger = Logger()  # Crie uma instância de Logger
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Kralen Manager Backup 1.0")
        self.root.geometry("400x200")
        self.root.resizable(width=False, height=False)
        self.root.configure(background="#FFFFFF")

        self.style = ThemedStyle(self.root)
        self.style.set_theme("clam")  # Configura o tema do Chrome

        self.create_widgets()
        self.db_functions['update_backup'](0, 0, BackupStatus.PARADO, "Iniciado sistema")
        self.check_database_periodically()

    def create_widgets(self):
        self.status_var = tk.StringVar()
        self.mensagem_var = tk.StringVar()

        self.style = ttk.Style()

        # Label da mensagem
        mensagem_label = tk.Label(
            self.root,
            textvariable=self.mensagem_var,
            font=("Tahoma", 11),
            justify="center",  # Centraliza horizontalmente
            background="#2793F2",  # Cor mais escura
            foreground="#FFFFFF",  # Fonte na cor clara
            padx=10,  # Margem à direita
            pady=10,  # Espaçamento na margem
            border=1,
            relief="groove"
        )
        mensagem_label.pack(side='top', padx=5, pady=5, fill="both",expand=True)

        # Botões centralizados
        button_frame = ttk.Frame(
            self.root,
            pad=(0,0),
            border=0,
            relief="groove",
            )
        button_frame.pack(side='top', padx=5, pady=15)

        # Adiciona o estilo "NoOutline.TButton"
        self.style.configure("NoOutline.TButton", relief="flat",  borderwidth=0)

        # Botão Iniciar Backup
        start_button = ttk.Button(
            button_frame,
            text="Iniciar Backup",
            command=self.start_backup,
            style="NoOutline.TButton",  # Adiciona estilo para remover tracejado
            pad=(1,1)
        )
        start_button.grid(row=0, column=0, padx=(10, 5), pady=5)

        # Botão Fechar
        close_button = ttk.Button(
            button_frame,
            text="Fechar",
            command=self.close_app,
            style="NoOutline.TButton",  # Adiciona estilo para remover tracejado
            pad=(1,1)
        )
        close_button.grid(row=0, column=1, padx=10, pady=5)

        # Barra de status
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Tahoma", 8),
            background="#F2F2F2",  # Cor mais escura
            foreground="#0D0D0D",  # Fonte na cor clara
            anchor="e"  # Alinhado à direita
        )
        status_bar.pack(side="bottom", fill="x", pady=0, padx=0)

    def check_database_periodically(self):
        interval_seconds = int(self.config["geral"]["verificabd"])

        if not self.process:
            mensagem = "Escutando"
            self.log(mensagem)
            self.mensagem_var.set(mensagem)

            self.root.after(interval_seconds * 1000, self.check_database_for_backup)

    def check_database_for_backup(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM backup WHERE ativo = 1")
            active_backups = cursor.fetchall()

            if active_backups:
                self.start_backup()

            self.root.after(1000, self.check_database_periodically)
        except Exception as e:
            status = BackupStatus.ERRO
            self.status_var.set(status.value)

            mensagem = f"Erro ao verificar o banco de dados: {str(e)}"
            self.log(mensagem)
            self.mensagem_var.set(mensagem)

    def close_app(self):
        self.finalize_backup()
        self.root.destroy()

    def finalize_backup(self):
        try:
            if self.process:
                mensagem = "Backup finalizado com sucesso."
                status = BackupStatus.PARADO
            else:
                mensagem = "Sistema fechado."
                status = BackupStatus.FECHADO

            self.db_update_backup(0, 0, status,mensagem)

            self.status_var.set(status.value)

            self.log(mensagem)
            self.mensagem_var.set(mensagem)

        except Exception as e:
            status = BackupStatus.ERRO
            self.status_var.set(status.value)

            mensagem = f"Erro ao finalizar o backup: {str(e)}"
            self.log(mensagem)
            self.mensagem_var.set(mensagem)

    def start_backup(self):
        if self.process:
            status = BackupStatus.INICIADO
            self.status_var.set(status.value)

            mensagem = "Backup já em andamento."
            self.log(mensagem)
            self.mensagem_var.set(mensagem)

            return

        try:
            self.conn.commit()

            status = BackupStatus.INICIADO
            self.status_var.set(status.value)

            mensagem = "Criando backup"
            self.log(mensagem)
            self.mensagem_var.set(mensagem)

            self.db_update_backup(0,0,status.value,"")
            self.process = subprocess.Popen(self.get_backup_command(), shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, universal_newlines=True)
            self.check_backup_status()

        except Exception as e:
            self.db_update_backup(0,1,BackupStatus.ERRO,str(e))

            status = BackupStatus.ERRO
            self.status_var.set(status.value)

            mensagem = f"Erro ao iniciar o backup: {str(e)}"
            self.log(mensagem)
            self.mensagem_var.set(mensagem)

    def check_backup_status(self):
        try:
            return_code = self.process.poll()

            if return_code is None:
                self.root.after(1000, lambda: self.check_backup_status())
                return
            elif return_code == 0:
                status = BackupStatus.PARADO
                self.status_var.set(status.value)

                mensagem = ""
                self.log(mensagem)
                self.mensagem_var.set(mensagem)

                self.finalize_backup()

                #self.root.after(1000, self.check_database_for_backup)
                self.root.after(1000, self.check_database_periodically)

            else:
                stdout, stderr = self.process.communicate()

                status = BackupStatus.ERRO
                self.status_var.set(status.value)

                mensagem = f"Saída Padrão: {stdout}\nErro Padrão: {stderr}"
                self.log(mensagem)
                self.mensagem_var.set(mensagem)

                self.finalize_backup()

            self.process = None

        except Exception as e:
            self.conn.rollback()

            status = BackupStatus.ERRO
            self.status_var.set(status.value)

            mensagem = f"Erro ao verificar o status do backup: {str(e)}"
            self.log(mensagem)
            self.mensagem_var.set(mensagem)

    def log(self, message):
        self.logger.log(message)
