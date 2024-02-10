# main.py
import json
import tkinter as tk
from logger import Logger
from database import setup_connection, create_backup_table, update_backup
from ui import BackupAppUI

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    root = tk.Tk()
    logger = Logger()

    conn = setup_connection(config, logger.log, tk.StringVar())

    if conn:
        db_functions = {'update_backup': lambda ativo, erro, status, mensagem: update_backup(conn, ativo, erro, status, mensagem, logger.log, tk.StringVar())}
        app_ui = BackupAppUI(root, logger.log, tk.StringVar(), config, db_functions)
        app_ui.setup_ui()

    root.mainloop()
