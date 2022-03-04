from api.library import *

def main():
    #aplicacion de los diccionarios

    # persona = {
    #     "nombre": "Geraldine",
    #     "apellidos": "Suarez Solano",
    #     "edad": 22
    # }

    persona = { #este objeto, tiene dos objetos
        "datos_personales":{
        "nombre": "Geraldine",
        "apellidos": "Suarez Solano",
        "edad": 22
        },

        "salarial": {
            "salario": 2000000,
            "subtransporte": 50000,
            "subalimentacion": 60000
        }
        
    }
    print(persona["salarial"])
    print (f"Nombre: {persona ['datos_personales']['nombre']} {persona ['datos_personales']['apellidos']}")
    #print (persona["nombre"]+" "+ persona["apellidos"])
    # persona ["nombre"] = "Karina"
    # print (f"{persona['nombre']} {persona['apellidos']}")

if __name__ == "__main__":
    main()