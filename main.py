import functions
from DB.connection import DAO


def mainMenu():
    conti = True
    while (conti):
        correctOption = False
        while (not correctOption):
            print("========= MENÚ PRINCIPAL =========")
            print("1.- Listar Cursos")
            print("2.- Registrar Curso")
            print("3.- Actualizar Curso")
            print("4.- Eliminar Curso")
            print("5.- Salir")
            print("==================================\n")
            option = int(input('Elige una Opcion: '))

            if option < 1 or option > 5:
                print("Elige una opción válida")
            elif option == 5:
                conti = False
                print("Gracias por usar el sistema, Adios!.")
                break
            else:
                correctOption = True
                executeOption(option)


def executeOption(option):
    dao = DAO()

    if option == 1:
        try:
            courses = dao.getCourses()
            functions.listCourse(courses)
        except:
            print('Ha ocurrido un error!')
    elif option == 2:
        course = functions.insertData()
        try:
            dao.createCourse(course)
        except:
            print('Ha ocurrido un error al registrar el curso')
    elif option == 3:
        try:
            courses = dao.getCourses()
            functions.listCourse(courses)
            course = functions.insertUpdateData(courses)
            if course:
                dao.updateCourse(course)
            else:
                print('\nCódigo no encontrado...\n')
        except:
            print('')
    elif option == 4:
        try:
            courses = dao.getCourses()
            functions.listCourse(courses)
            deleteCode = functions.insertCode(courses)
            if not (deleteCode == ''):
                dao.deleteCourse(deleteCode)
            else:
                print('\nCódigo no encontrado...\n')
        except:
            print('')
    else:
        print('Elige una opción válida')


mainMenu()
