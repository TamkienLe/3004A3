import psycopg2
import psycopg2.extras

# Connection parameters
db_params = {
    'dbname': 'assignment3',
    'user': 'postgres',
    'password': 'Batgioi99',
    'host': 'localhost',
    'port': '5432'
}

#Gets all the student records and puts them in one output
def getAllStudents():
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM students ORDER BY student_id;")
            records = cur.fetchall()
            for record in records:
                print(f"ID: {record['student_id']}, Name: {record['first_name']} {record['last_name']}, Email: {record['email']}, Enrollment Date: {record['enrollment_date']}")

#Inserts a new student record into table
def addStudent(first_name, last_name, email, enrollment_date):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date)
            )

#Updates the email address for student based on id
def updateStudentEmail(student_id, new_email):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id)
            )
#deletes record of student based on student ID
def deleteStudent(student_id):
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM students WHERE student_id = %s",
                (student_id,)
            )

# Replace the below calls with actual function calls and parameters as needed.
getAllStudents()
#addStudent('Student', '1', 'student1@example.com', '2023-09-10')
#updateStudentEmail(1, 'Student3.newemail@example.com')
deleteStudent(4)