from library import *


def main(): 
    SALARIO_MIN = 1000000
    SUB_ALIM = 120000
    SUB_TRANSP = 80000
    BONO = 50000
    nombre = input("Digite el Nombre ==> ")
    salario = int(input("Digite el salario: ")) 
    dias_trabajados = int(input("Digite los dias trabajados: ")) 
    sueldoPagar = calcularSueldo(salario, dias_trabajados)

    if salario < (SALARIO_MIN * 2):
        sueldoPagar= sueldoPagar + SUB_ALIM + SUB_TRANSP
    else:
        sueldoPagar = sueldoPagar + BONO


    print (f"Su nombre es: {nombre} y el sueldo a pagar es: {sueldoPagar:.0f}")

if __name__ == "__main__":
    main()
