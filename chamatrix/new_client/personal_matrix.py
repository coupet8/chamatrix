import sqlite3

def read_single_row(matrix_id):
    try:
        sqlite_connection = sqlite3.connect('db_matrix.db')
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * FROM matrix where id = ?"""
        cursor.execute(sqlite_select_query, (matrix_id, ))
        record = cursor.fetchone()
        personal_matrix = [record[1], record[2], record[3], record[3]]
        cursor.close()
        print(personal_matrix)
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

read_single_row(2)