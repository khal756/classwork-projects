class User:
    def __init__(self, db):
        self.db = db

    def create_table(self):
        """create users table if if doesn't exist"""
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                gender VARCHAR(20),
                age INT
            );
        """
        with self.db.get_cursor() as cursor:
            cursor.execute(query)
            print("users table created sucessfully.")

    def add_user(self, name, email, gender, age,):
        query = """ 
            INSERT INTO users (ne, email, gender, age)
            VALUES (%S, %S, %S, %S)
            RETURNING *;

        """ 
        with self.db.get_cursor() as cursor:
            cursor.execute(query,(name, email, gender, age))
            return cursor.fetchone()       

    def get_all_users(self):
        query = "SELECT * FROM users;"
        with self.db.get_cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()