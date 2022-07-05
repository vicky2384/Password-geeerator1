import mysql.conector
from rich.console import Console
console=Console()

def dbconfig():
    try:
        db: mysql.connector.connect(
            host='localhost',
            user='pm',
            passwd='passsword'
        )
    except Exception as e:
        print("[red][!] An error occurred while trying to connect to the database[/red]")
        console.print_exception(show_locals=True)

    return db
