# -----------------------------------------------------------------------------
# Actividad:    M1-Hello World
# Creado el:    20.05.202
# Creado por:   Jabes Rivas
# Matrícula:    2019-8466
# Materia:      ITLA TDS-002 2025-C2
# Docente:      Persio Martinez
# Descripción:  Un programa que imprime "Hello World" y lo imprime junto
#               al nombre del usuario, utilizando colores en la consola
# -----------------------------------------------------------------------------

from colorama import init, Fore, Style


def main():
    """
    Esta función inicializa colorama, imprime "Hello World",
    pide el nombre del usuario y luego lo imprime
    """

    default_message: str = "Hello world"

    init(autoreset=True)

    # Constantes para colorama
    CLR_Y = Fore.YELLOW
    CLR_G = Fore.GREEN
    CLR_W = Fore.WHITE
    CLR_R = Fore.RED

    # Imprime la cabecera del programa
    print(Style.BRIGHT + CLR_Y + "-----------------------------------------------------------------------------")
    print(CLR_G + " Actividad:    " + CLR_W + "M1-Hello World")
    print(CLR_G + " Creado el:    " + CLR_W + "20.05.2025")
    print(CLR_G + " Creado por:   " + CLR_W + "Jabes Rivas")
    print(CLR_G + " Matrícula:    " + CLR_W + "2019-8466")
    print(CLR_G + " Materia:      " + CLR_W + "ITLA TDS-002 2025-C2")
    print(CLR_G + " Docente:      " + CLR_W + "Persio Martinez")
    print(CLR_G + " Descripción:  " + CLR_W + f"Un programa que imprime \"{default_message}\" y lo imprime")
    print(CLR_G + "               " + CLR_W + "junto al nombre del usuario, utilizando colores en la consola")
    print(Style.BRIGHT + CLR_Y + "-----------------------------------------------------------------------------")
    print("\n")

    # Pedir el nombre al usuario
    try:
        user_name = input(CLR_G + "¿Cuál es tu nombre? -> " + CLR_W)
    except KeyboardInterrupt:
        print(CLR_R + Style.BRIGHT + "\n\nEntrada de datos interrumpida por el usuario")
        return
    except EOFError:
        print(CLR_R + Style.BRIGHT + "\n\nNo se detectó entrada de datos")
        return

    # Imprimir con el nombre del usuario
    if user_name:
        print(CLR_Y + Style.BRIGHT + f"{default_message} {user_name}")
    else:
        # Saludo por defecto para cuando no se ingresa un nombre
        print(CLR_R + "\n\n(No se detectó entrada de datos)")
        print(CLR_Y + Style.BRIGHT + f"{default_message} + Nuestro nombre")


if __name__ == "__main__":
    main()
