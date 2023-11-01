import psycopg2

class CampeonatoBrasileiro:

    def __init__(self):
        hostname = 'localhost'
        database = 'campeonatobrasileiro'
        username = 'postgres'
        pwd = 'admin'
        port_id = 5432
        self.nome_banco = 'campeonatobrasileiro'
        self.connection = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)
        self.cursor = self.connection.cursor()

    def create_table(self, sql_command):
        self.cursor.execute(sql_command)
        self.connection.commit()

    def create_tables(self, sql_commands):
        for sql_command in sql_commands:
            self.cursor.execute(sql_command)

    def execute_sql_files(self, sql_files):
        for sql_file in sql_files:
            with open(sql_file, 'r') as file:
                try:
                    command = file.read()
                    self.cursor.execute(command)
                    self.connection.commit()

                except Exception as error:
                    print(error)

    def close_connection(self):
        self.connection.close()
