# Tarea PIA01 - Piedra, papel o tijera
# Autora: Ana Belén Morales
import random
# Constantes con las tres jugadas posibles
PIEDRA ="piedra"
PAPEL ="papel"
TIJERAS ="tijeras"

# Decide quién gana una ronda y muestra el resultado
def decidir_ganador(user_action, computer_action):
    # Si los dos eligen lo mismo, es empate
    if user_action == computer_action:
        print(f"Usuario y ordenador eligieron {user_action}. ¡Empate!")
    # El usuario saca piedra
    elif user_action == PIEDRA:
        if computer_action == TIJERAS:
            print("Piedra rompe tijeras. ¡Ganaste!")
        else:
            print("Papel envuelve piedra. ¡Perdiste!")
    # El usuario saca papel
    elif user_action == PAPEL:
        if computer_action == TIJERAS:
            print("Tijeras cortan papel. ¡Perdiste!")
        else:
            print("Papel envuelve piedra. ¡Ganaste!")
    # El usuario saca tijeras
    elif user_action == TIJERAS:
        if computer_action == PIEDRA:
            print("Piedra rompe tijeras. ¡Perdiste!")
        else:
            print("Tijeras cortan papel. ¡Ganaste!")


# Bucle principal del juego
def main():
    # Bucle infinito: se juega ronda tras ronda hasta que el usuario escriba "salir"
    while True:
        # El usuario escribe su jugada (.lower() la pasa a minúsculas)
        user_action = input("\nElige una opción: piedra, papel o tijeras (o 'salir'): ").lower()

        # Si escribe "salir", se termina el juego
        if user_action == "salir":
            print("¡Hasta la próxima!")
            break

        # Si no es una jugada válida, se avisa y se vuelve a preguntar
        if user_action not in [PIEDRA, PAPEL, TIJERAS]:
            print("Opción no válida. Escribe piedra, papel o tijeras.")
            continue

        # El ordenador elige su jugada al azar
        computer_action = random.choice([PIEDRA, PAPEL, TIJERAS])

        # Se muestran las dos jugadas y se decide el ganador
        print(f"\nElegiste {user_action}. El ordenador eligió {computer_action}")
        decidir_ganador(user_action, computer_action)

# Punto de entrada: el juego arranca al ejecutar el fichero
if __name__ == "__main__":
    main()