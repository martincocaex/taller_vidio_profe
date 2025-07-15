data = {
    "reserva":[
            {
                "id_reserva":"re01",
                "nombre_huesped":"juanito",
                "numero_habitacion":105,
                "tipo_habitacion":"individual",
                "cantidad_dias":3,
                "costo_total":2500





            },
            {

            
                "id_reserva":"re02",
                "nombre_huesped":"pedrito",
                "numero_habitacion":106,
                "tipo_habitacion":"doble",
                "cantidad_dias":8,
                "costo_total":3990

            },
            {
                
                "id_reserva":"re03",
                "nombre_huesped":"maria",
                "numero_habitacion":110,
                "tipo_habitacion":"suite",
                "cantidad_dias":9,
                "costo_total":6850
            }






        ]



}



def buscar_reserva(id_reserva:str):
    for i in data["reserva"]:
        if i["id_reserva"]== id_reserva:
            return i
        





def valida_numero_entero_positivo(mensaje_input:str):
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero <=0:
                print("No puede ingresar numero negativos")
                continue
        except ValueError:
            print("Solo se puede ingresar numeros enteros")
            continue



def valida_texto (mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip())== 0:
            continue
        else:
            return texto
        



def valida_tipo_habitacion(mensaje_input:str):
    while True:
        tipo_habitacion = input("Ingrese el tipo de habitacion: ")
        if tipo_habitacion == "individual" or tipo_habitacion == "doble" or tipo_habitacion == "suite":
            return tipo_habitacion
        else:
            print("El tipo de habitacion no es valido.")
            continue



def calcula_costo_habitacion(tipo_habitacion:str, cantidad_dias:int):
    if tipo_habitacion == "individual":
        return cantidad_dias * 50
    if tipo_habitacion ==  "doble":
        return cantidad_dias * 80
    else:
        return cantidad_dias * 120
    



def valida_id_reserva(id_reserva:str):

    numeros = "1234567890"
    for i in id_reserva:
        for j in numeros:
            if i == j:
                return True
    return False



def valida_id_letra(id_reserva:str):

    letra = "qwertyuiopasdsfghjklzxcvbnm"
    for i in id_reserva:
        for j in letra:
            if i == j:
                return True
    return False

def agregar_reserva(id_reserva:str, nombre:str, numero_habitacion:int, tipo_habitacion:str, cantidad_dias:int):
    reserva_generada = {
                "id_reserva":id_reserva,
                "nombre_husped":nombre,
                "nuermo_habitacion":numero_habitacion,
                "tipo_habitacion": tipo_habitacion,
                "cantidad_dias": cantidad_dias,
                "costo_total": calcula_costo_habitacion()
    }
    data["reserva"].append(reserva_generada)



def buscar_habitacion(numero_habitacion:int):
    for i in data["reserva"]:
        if i["numero_habitacion"] == numero_habitacion:
            return True
        else:
            return False
        
def modificar_reserva(id_reserva:int,cantidad_dias:str, tipo_habitacion:str):
    reserva_encontrada = buscar_reserva(id_reserva)
    if reserva_encontrada == None:
        print("Reserva no encontrada")
    else:
        reserva_encontrada["cantidad_dias"]= cantidad_dias
        reserva_encontrada["tipo_habitacion"] = tipo_habitacion
        reserva_encontrada["costo-total"] = calcula_costo_habitacion(tipo_habitacion, cantidad_dias)
        print("Reserva modificada con exito")


def cancelar_reserva(id_reserva:str):
    reserva_encontrada = buscar_reserva(id_reserva)
    if reserva_encontrada == None:
        print("Reserva no encontrada")
    else:
        data["reserva"].remove(reserva_encontrada)
        print("Reserva eliminada correctamente")
 

def mostrar_todas_las_reservas():
    for i in data["reserva"]:
        print(f"ID: {i["id_reserva"]} - TOTAL - {i["costo_total"]}")


def menu():
    while True:
        print("*** MENU ***")
        print("[1]- agregar reserva")
        print("[2]- buscar reserva")
        print("[3]- moidificar reserva")
        print("[4]- Cancelar reserva")
        print("[5]- Mostar todas las reservas")
        print("[6]- salir")

        opcion = valida_numero_entero_positivo("Ingrese una opcion:")
        

        if opcion == 1:
            while True:
                id_reserva = valida_texto("Ingrese el id de la reserva:")

                if buscar_reserva(id_reserva) != None:
                    print("El id ya se encuntra registrado")
                    continue
                elif valida_id_letra(id_reserva) == False:
                    print("El id debe contener almenos una letra")
                    continue
                elif valida_numero_entero_positivo(id_reserva) == False:
                    print("El id debe contener al menos un numero.")
                    continue
                break        
            nombre= valida_texto("Ingrese el nombre del huesped: ")
            while True:
                numero_habitacion = valida_numero_entero_positivo("Ingrese el numero de la habitacion: ")
                if numero_habitacion <= 101 and numero_habitacion >= 999:
                    print("El numero de habitacion ingresado no existe.")
                    continue
                
                
                if buscar_habitacion(numero_habitacion) == False:
                    break
                else:
                    print("La habitacion se encuntra ocupada")
                    continue
            tipo_habitacion = valida_tipo_habitacion("Ingrese el tipo de habitacion: ")
            dias = valida_numero_entero_positivo("Ingrese la cantidad de dias: ")

            agregar_reserva(id_reserva,nombre,numero_habitacion,tipo_habitacion,dias)
            print("Reserva registrada correctamente")

        elif opcion == 2:
            id_reserva = valida_texto("Ingrese el id de la reserva: ")
            reserva_encontrada = buscar_reserva(id_reserva)
            if reserva_encontrada == None:
                print("La reserva no se encuentra")
            else:
                print(f"ID: {reserva_encontrada["id_reserva"]} - TOTAL: {reserva_encontrada["costo_total"]}")

        
        elif opcion == 3:
            id_reserva = valida_texto("Ingrese el id de la reserva: ")
            cantidad_dias = valida_numero_entero_positivo("Ingrese la cantidad de dias: ")
            tipo_habitacion = valida_tipo_habitacion


            modificar_reserva(id_reserva,cantidad_dias,tipo_habitacion)

        
        elif opcion == 4:
            id_reserva = valida_texto("Ingrese el id que desea cancelar: ")
            cancelar_reserva(id_reserva)

            
        
        elif opcion == 5:
            mostrar_todas_las_reservas()

        elif opcion == 6:
            print("Saliendo de la aplicacion...")
            break
        else:
            print("opcion no valida")

        