import mysql.connector
from mysql.connector import Error


class DAO():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='university',
                port='3306',
            )
        except Error as err:
            print(err)

    def getCourses(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute('SELECT * FROM courses ORDER BY name ASC')
                result = cursor.fetchall()
                return result
            except Error as err:
                print(err)

    def createCourse(self, course):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = 'INSERT INTO courses (code, name) VALUES ("{0}", "{1}")'
                cursor.execute(sql.format(int(course[0]), course[1]))
                self.connection.commit()
                print(' Curso Registrado !\n')
            except Error as err:
                print(err)

    def updateCourse(self, course):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = 'UPDATE courses SET name = "{0}" WHERE code="{1}"'
                cursor.execute(sql.format(course[1], course[0]))
                self.connection.commit()
                print('Curso Actualizado!\n')
            except Error as err:
                print(err)

    def deleteCourse(self, code):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = 'DELETE FROM courses WHERE code="{0}"'
                cursor.execute(sql.format(code))
                self.connection.commit()
                print('Curso eliminado!\n')

            except Error as err:
                print(err)



