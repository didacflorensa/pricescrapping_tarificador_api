import pyodbc

class DatabaseSQL:
    connection = None
    dbconfig = {
        'url': '192.168.101.70',
        'database': 'Flower',
        'user': 'sa',
        'password': 'Hu9iQYtGRCUKa6'
    }

    def __init__(self):
        try:
            self.connection = pyodbc.connect("Driver=/usr/local/lib/libmsodbcsql.17.dylib;Server=192.168.101.70;Database=Flower;UID=sa;PWD=Hu9iQYtGRCUKa6;")
        except ConnectionError as exc:
            raise RuntimeError('Failed to open connection') from exc

    def get_connection(self):
        return self.connection

    def close_connection(self):
        self.connection.close()