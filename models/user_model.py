# models/user_model.py

from database.connection import get_connection

class UserModel:
    TABLE_NAME = "users"

    def check_login(self, username: str, password: str):
        conn = get_connection()
        if conn is None:
            return None

        cursor = conn.cursor(dictionary=True)
        sql = f"SELECT * FROM {self.TABLE_NAME} WHERE user=%s AND password=%s LIMIT 1"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.TABLE_NAME}")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
