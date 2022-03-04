#Manejo de listas

"""
*************************************
            Manejo de Listas
*************************************
"""
def listas():
    lista1= []
    lista2 = list()

    listaConElementos=[30, 2000000,"Ing. Sistemas" ,"Geraldine Suarez", "Ingeniera", True, ["Tecnico", "Profesional", "doctorado", 4]] #Los elementos estan separados por comas (,)
    #print(listaConElementos[1]) #imprime el elemento de la posicion 1 que es 2000000

#utilizando el ciclo for
    #for i in range(6): #va desde 0 hasta 6
    for i in range(len(listaConElementos)):
        print(listaConElementos[i])
#utilizando el ciclo while
    print("")
    print("ciclo While")
    j=0
    while j < len(listaConElementos):
        print(listaConElementos[j])
        j=j+1

















def main (): 
    listas()

if __name__ == "__main__":
    main()