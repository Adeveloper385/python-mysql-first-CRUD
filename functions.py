def listCourse(courses): # SELECT
    counter = 1
    print('\nCursos:\n')
    for c in courses:
        data = " Código: {0}. | Nombre: {1}."
        print(data.format(c[0], c[1]))
        counter = counter + 1
    print()


def insertData(): # INSERT
    rightCode = False
    while (not rightCode):
        code = input('Ingresa el código del curso: ')
        if len(code) == 6:
            rightCode = True
        else:
            print('Ingresa un código con 6 dígitos')

    name = input('Ingresa el nombre del curso: ')

    course = (code, name)
    return course

def insertUpdateData(courses): #UPDATE
    isCode = False
    updateCode = input('Ingrese el código del curso a actualizar: ')
    for c in courses:
        if c[0] == int(updateCode):
            isCode = True
            break

    if isCode:
        name = input('Ingresar el nuevo nombre del curso: ')
        course = (updateCode, name)
    else:
        course = None

    return course

def insertCode(courses): # DELETE
    isCode = False
    deleteCode = input('Ingrese el código del curso a Eliminar: ')
    for c in courses:
        if c[0] == int(deleteCode):
            isCode = True
            break

    if not isCode:
        deleteCode = ""

    return deleteCode
    
