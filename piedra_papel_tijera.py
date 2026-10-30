# Tarea PIA01 - Piedra, papel o tijera
# Autora: Ana Belén Morales
import random
# Constantes con las tres jugadas posibles
PIEDRA ="piedra"
PAPEL ="papel"
TIJERAS ="tijeras"

# Decide quién gana una ronda (se completa en el commit 2)
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


# Bucle principal del juego (se completa en el commit 3)
def main():
    pass

# Punto de entrada: el juego arranca al ejecutar el fichero
if __name__ == "__main__":
    main()