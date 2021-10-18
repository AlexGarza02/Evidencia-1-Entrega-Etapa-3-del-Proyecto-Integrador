import time
import random
from random import sample
from random import choice

global lista_notas
global total_asiertos
global total_malas


# leer_archivo(nombre) que retorna la lista de preguntas y al final de la función debes llamar a def grabar_archivo(nombre, lista) para que grabe la información de todas las preguntas de la lista.
# leer_archivo(nombre): la función lee toda la información del archivo que tiene el nombre físico recibido en el parámetro de entrada y la retorna la información del mismo como una la lista de preguntas.
def leer_archivo(nombre_archivo):
    txtpreg = open(nombre_archivo + '.txt', 'r', encoding='utf8')
    preguntas = []
    for linea in txtpreg:
        linea = linea.replace('\n', '').split(',')
        linea = preguntas.append(linea)
    txtpreg.close()
    return preguntas


# def grabar_archivo(nombre, lista): la función recibe una la lista de todos las preguntas y el nombre del archivo donde se grabará la información, esta función sustituye toda la información del archivo por la nueva información que está en la lista.
def grabar_archivo(nombre, lista):
    archivo = open(nombre + '.txt', 'w')
    for i in range(len(lista)):
        archivo.write(
            f'{lista[i][0]},{lista[i][1]},{lista[i][2]},{lista[i][3]},{lista[i][4]},{lista[i][5]},{lista[i][6]},{lista[i][7]}\n')
    archivo.close()


# Matriz
preguntas = leer_archivo('preguntas')
total_asiertos = 0
total_malas = 0
lista_notas = []


# ['1', 'Matemáticas', 'Texto de la pregunta', 'R1', 'R2', 'R3', 'R4', 'RC' ]
# 0 -> num_pregunta
# 1 -> materia
# 2 -> Texto
# 3 -> R1
# 4 -> R2
# 5 -> R3
# 6 -> R4
# 7 -> RC


## Listo
# Actualiza tu función para almacenar los datos en una lista de listas, crea una lista por pregunta con los datos de la pregunta, y cada una de estas listas dentro de la lista de preguntas
def registrar_pregunta():
    global preguntas

    print(
        "Bienvenido a la opción para registrar preguntas, por favor sigue las instrucciones"
    )

    nueva_preg = []

    # id_pregunta = input("Ingresa el ID de la pregunta: ")
    nueva_preg.append(str(len(preguntas) + 1))
    print(f'Pregunta {nueva_preg[0]}:')
    enfoque = input(
        "Ingresa el enfoque de la pregunta: Lectura, Matemáticas, Ciencias: ")
    nueva_preg.append(enfoque)
    pregunta = input("Ingresa el texto de la pregunta: ")
    nueva_preg.append(pregunta)

    for num in range(4):
        respuesta = input("Ingresa la respuesta " + str(num + 1) + ": ")
        nueva_preg.append(respuesta)

    correcta = input("Ingresa la respuesta correcta:")
    nueva_preg.append(correcta)

    preguntas.append(nueva_preg)
    grabar_archivo('preguntas', preguntas)


## Listo
# Desarrolla la función def actualizar_pregunta( ) que despliegue la lista completa de preguntas numeradas y solicite el idPregunta para desplegar en un solo renglón toda la información
# que se encuentra actualmente en la lista de preguntas. La función debe validar que la pregunta exista.
#
# Si el id de la pregunta es correcto la función debe solicitar todos los datos de la pregunta,  si el usuario no quiere cambiar algún dato, solo debe dar <enter> y con ello se debe conservar
# la información que tenía previamente la pregunta. Una vez que ya ingresó toda la información, la función debe mostrar la nueva información de la pregunta y debe preguntar: ¿Está seguro de que
# quiere actualizar los datos de la pregunta? Si la respuesta es sí, la función se debe actualizar la información de la pregunta en la lista de preguntas.
def actualizar_pregunta():
    global preguntas

    print(
        "Bienvenido a la opción para actualizar preguntas, por favor sigue las instrucciones \nA continuación se despliega la lista de preguntas guardadas\n"
    )

    for pregunta in preguntas:
        id_pregunta, enfoque, pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = pregunta  # esto (pregunta) es una lista, hacemos asignación múltiple

        print(
            f"ID de la pregunta: {id_pregunta} \nEnfoque de la pregunta: {enfoque} \nPregunta: {pregunta}"
        )
        print(
            f"a){respuesta1:<15}b){respuesta2:<15}c){respuesta3:<15}d){respuesta4:<15} \n"
        )

    id_cambio = input("Ingresa el id de la pregunta que quieres cambiar: ")
    for pregunta in preguntas:
        id_pregunta, enfoque, pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = pregunta
        if id_cambio == id_pregunta:
            enfoque = input(
                "Ingresa el enfoque de la pregunta: Lectura, Matemáticas, Ciencias: "
            )
            pregunta = input("Ingresa el texto de la pregunta: ")
            respuestas = ""

            for num in range(4):
                respuesta = input("Ingresa la respuesta " + str(num + 1) +
                                  ": ")

                if num == 3:
                    respuestas = respuestas + respuesta  # string de respuesta 4, no lleva coma
                else:
                    respuestas = respuestas + respuesta + ","  # string de respuestas 1, 2, 3

            respuestas = respuestas.split(
                ","
            )  # hacer una lista desde un string, cada elemento es separado por coma

            respuesta1, respuesta2, respuesta3, respuesta4 = respuestas  # asignación múltiple de variables de una lista (elemento por elemento)

            correcta = input("Ingresa la respuesta correcta:")

            pregunta = [
                id_pregunta, enfoque, pregunta, respuesta1, respuesta2,
                respuesta3, respuesta4, correcta
            ]

            preguntas[int(id_cambio) - 1] = pregunta
            break
        else:
            id_cambio
    grabar_archivo('preguntas', preguntas)
    pass


# LISTO
# la cantidad de preguntas deseada para desplegar el quiz.
# Desarrolla la función def estudiar_area( ) para crear un Quiz de cierta área con las preguntas registradas en la lista de preguntas.
# La función debe solicitar el área de enfoque a estudiar y la cantidad de preguntas deseada para desplegar el quiz.
def estudiar_area():
    global preguntas

    enfoque_elegir = str(input("Seleccione el enfoque que desea estudiar: "))
    cantidad_elegir = int(
        input("Elegija la cantidad de pregutnas que desea presentar: "))

    filtro = []

    for i in range(len(preguntas)):
        if preguntas[i][1] == enfoque_elegir:
            filtro.append(preguntas[i])

    if cantidad_elegir > len(filtro):
        print('No hay preguntas suficientes')
    else:
        for i in range(cantidad_elegir):
            print(
                f"ID de la pregunta: {filtro[i][0]} \nEnfoque de la pregunta: {filtro[i][1]} \nPregunta: {filtro[i][2]}"
            )
            print(
                f"a){filtro[i][3]:<15}b){filtro[i][4]:<15}c){filtro[i][5]:<15}d){filtro[i][6]:<15} \n"
            )


pass


## EN proceso
# Desarrolla la función def presentar_quiz( ) para crear que contenga 10 preguntas de las 3 áreas de estudio y con límite de tiempo de 20 minutos.
# Debe usar las preguntas registradas en la lista de preguntas.
def presentar_quiz():
    print(
        "Bienvenido al quiz, por favor conteste las preguntas \nA continuación se despliega la lista de preguntas guardadas\n"
    )
    print('Tiene un límite de tiempo de 20 minutos por quiz')

    global preguntas
    global total
    global total_asiertos
    global total_malas

    tiempo = 1200

    total_rondas = 0
    total = 0
    total = total + 1
    preguntas_quiz = []
    # choice() method
    lista_aleat = choice(preguntas)

    # para despliegar 10 preguntas
    while total_rondas < 10:
        lista_aleat = choice(preguntas)
        if lista_aleat in preguntas_quiz:
            pass
        else:
            preguntas_quiz.append(lista_aleat)
            total_rondas = total_rondas + 1

    total_asiertos = 0
    total_malas = 0
    calif = 0
    for num in range(10):

        inicio = time.time()

        pregunta = preguntas_quiz[num]

        print(
            f"ID de la pregunta: {pregunta[0]} \nEnfoque de la pregunta: {pregunta[1]} \nPregunta: {pregunta[2]}"
        )
        print(
            f"a){pregunta[3]:<15} b){pregunta[4]:<15} c){pregunta[5]:<15} d){pregunta[6]:<15} \n"
        )

        ans_usuario = input("Ingrese su respuesta: ")

        if ans_usuario == pregunta[7]:
            print(f" ¡Felicidades, ha contestado correctamente! \n")
            total_asiertos = total_asiertos + 1

        else:
            print(f" Incorrecto.\n  Respuesta Correcta: {pregunta[7]} \n")
            total_malas = total_malas + 1

        fin = time.time()

        total = round((tiempo - (fin - inicio)) / 60, 2)
        print(f"\nEl tiempo restante son {total} minutos\n")

    print(" Fin del quiz. Recuerda, hay que caer para aprender a levantarse. ")
    print(" El total de preguntas contestadas correctamente fué ",
          total_asiertos)
    print(" El total de preguntas contestadas erroneamente fué ", total_malas)

    calif = total_asiertos * 10

    print(" SU calificación total fué de:", calif)
    lista_notas.append(calif)


pass


##
## Desarrolla la función def reportar_calificaciones( ) para generar un reporte de calificaciones con la siguiente información:
def reportar_calificaciones():
    global total_asiertos
    global total_malas
    global lista_notas

    usuarios = len(lista_notas)

    suma = 0
    for nota in lista_notas:
        suma = suma + nota

    promedio = suma / len(lista_notas)

    porcentaje_correctas = round(total_asiertos / (total_asiertos + total_malas) * 100, 2)
    porcentaje_incorrectas = round(total_malas / (total_asiertos + total_malas) * 100, 2)

    print(
        f'{"Total de usuarios":<30}{usuarios}\n{"Promedio de calificaciones":<30}{promedio}\n{"Respuestas correctas":<30}{porcentaje_correctas}%\n{"Respuestas incorrectas":<30}{porcentaje_incorrectas}%'
    )

    pass


def menu():
    print("""Menú de opciones:
    1.	Alta de preguntas de prueba PISA (lectura, matemáticas, ciencias)
    2.	Actualizar preguntas de la prueba PISA (lectura, matemáticas, ciencias)
    3.	Estudiar preguntas de cierta área (lectura, matemáticas, ciencias)
    4.	Presentar un quiz (lectura, matemáticas, ciencias)
    5.	Reporte de calificaciones
    6.	Salir""")
    op = int(input("Selecciona una opción: "))

    return op


def salir():
    print("Gracias por usar el sistema")
    sigue = False

    return sigue


def main():
    sigue = True

    while sigue:

        op = menu()

        if op < 1 or op > 6:
            print('Elija la opcion que desea correr:')
            continue
        elif op == 1:
            registrar_pregunta()

        elif op == 2:
            actualizar_pregunta()

        elif op == 3:
            estudiar_area()

        elif op == 4:
            presentar_quiz()

        elif op == 5:
            reportar_calificaciones()
            print("el resultado de la calificación es: ",
                  reportar_calificaciones)
        else:
            print('Fin del programa.')
            sigue = salir()


main()
