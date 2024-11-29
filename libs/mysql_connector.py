from mysql import connector
from mysql.connector import errorcode

class Db:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def _use_database(self, db_name):
        try:
            self.cursor.execute(f'USE {db_name}')
        except connector.Error as err:
            print(err.msg)
            return False
        return True

    def connect(self):
        try:
            self.connection = connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            self.cursor = self.connection.cursor()
        except connector.Error as err:
            print(f'Błąd połączenia z bazą danych {err}')
            return False
        return True
    def close(self):
        if self.connection:
            self.connection.close()
        print('Zamknięto połączenie z bazą danych')

    def create_database(self, db_name):
        try:
            self.connect()
            self.cursor.execute(f'CREATE DATABASE {db_name}')
            print(f'Utworzono bazę danych {db_name}')
        except connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print(f"Baza danych o nazwie {db_name} już istnieje")
            else:
                print(err.msg)

    def create_table(self, table_name, columns, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)
            self.cursor.execute(f'CREATE TABLE {table_name} ({columns})')
            print(f'Utworzono tabelę {table_name}')
        except connector.Error as err:
            print(err.msg)
            return False
        return True

    def alter_table(self, table_name, columns, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)
            self.cursor.execute(f'ALTER TABLE {table_name} ADD {columns}')
            print(f'Zmodyfikowano tabelę {table_name}, dodano kolumny {columns}')
        except connector.Error as err:
            print(err.msg)
            return False
        finally:
            self.close()
        return True

    def drop_table(self, table_name, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)
            self.cursor.execute(f'DROP TABLE {table_name}')
            print(f'Usunięto tabelę {table_name}')
        except connector.Error as err:
            print(err.msg)
            return False
        finally:
            self.close()
        return True

    def drop_database(self, db_name):
        try:
            self.connect()
            self.cursor.execute(f'DROP DATABASE {db_name}')
            print(f'Usunięto bazę danych {db_name}')
        except connector.Error as err:
            print(err.msg)
            return False
        finally:
            self.close()
        return True

    def insert_record(self, table_name, columns, values, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            self.cursor.execute(query)
            self.connection.commit()
            print(f'Dodano rekord do tabeli {table_name}')
        except connector.Error as err:
            print(err.msg)
            return False
        return True

    def update_record(self, table_name, set_clause, condition, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print(f'Zaktualizowano rekordy w tabeli {table_name}')
        except connector.Error as err:
            print(err.msg)
            return False
        finally:
            self.close()
        return True

    def delete_record(self, table_name, condition, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)
            query = f"DELETE FROM {table_name} WHERE {condition}"
            self.cursor.execute(query)
            self.connection.commit()
            print(f'Usunięto rekordy z tabeli {table_name}')
        except connector.Error as err:
            print(err.msg)
            return False
        finally:
            self.close()
        return True

    def select_records(self, table_name=None, columns="*", joins=None, condition=None, order_by=None, group_by=None,
                       query=None, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)

            if query:
                full_query = query
            else:
                full_query = f"SELECT {columns} FROM {table_name}"

                if joins:
                    for join in joins:
                        full_query += f" {join}"  # Dodaj każde złączenie (JOIN)

                if condition:
                    full_query += f" WHERE {condition}"

                if group_by:
                    full_query += f" GROUP BY {group_by}"

                if order_by:
                    full_query += f" ORDER BY {order_by}"

            self.cursor.execute(full_query)
            results = self.cursor.fetchall()
            return results
        except connector.Error as err:
            print(err.msg)
            return False
        finally:
            self.close()

    def execute_query(self, query, db_name=None):
        try:
            self.connect()
            if db_name:
                self._use_database(db_name)
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except connector.Error as err:
            print(err.msg)
            return False
