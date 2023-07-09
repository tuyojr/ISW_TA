import pyodbc

class Database:
    records = []
    def __init__(self, name='', mark=0):
        self.conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-230524-1335\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes')
        self.cursor = self.conn.cursor()
        self.name = name
        self.course_code = 'CSC419'
        self.mark = mark
        self.grade = self.final_grade()
        self.employment = self.employment_status()

    def create_table(self):
        self.cursor.execute('CREATE TABLE Training.dbo.students(student_id INT IDENTITY(1,1) PRIMARY KEY, name VARCHAR(50) NOT NULL, course_code VARCHAR(10), mark INT NOT NULL, grade VARCHAR(1) NOT NULL, employment_status VARCHAR(50))')
        self.conn.commit()
        print("Operation performed successfully.")
        
    def final_grade(self):
        if self.mark >= 75:
            return 'A'
        elif self.mark >= 65 and self.mark < 75:
            return 'B'
        elif self.mark >= 55 and self.mark < 65:
            return 'C'
        else:
            return 'F'
        
    def employment_status(self):
        if self.final_grade() == 'A':
            return 'automatic employment'
        elif self.final_grade() == 'B':
            return 'open to work'
        else:
            return 'probation'
    
    def collect_user_records(self):
        self.records.append((self.name, self.course_code, self.mark, self.grade, self.employment))
        print("Record will be added!")

    def insert_records(self):
        self.cursor.executemany('INSERT INTO Training.dbo.students(name, course_code, mark, grade, employment_status) VALUES (?, ?, ?, ?, ?)', self.records)
        self.conn.commit()
        print("Operation performed successfully.")

    def delete_records(self, row_value):
        self.row_value = row_value
        self.cursor.execute('DELETE FROM Training.dbo.students WHERE (name) = (?)', self.row_value)
        self.conn.commit()
        print("Operation performed successfully.")

    def select_all_record(self):
        self.cursor.execute('SELECT * FROM Training.dbo.students')
        for row in self.cursor:
            return row
        
    def select_record_by_name(self, row_value):
        self.row_value = row_value
        self.cursor.execute('SELECT * FROM Training.dbo.students WHERE (name) = (?)', self.row_value)
        for row in self.cursor:
            return row

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("Connection closed successfully.")