import random

def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)
    jugador = input("Elige piedra, papel o tijera: ").strip().lower()
    
    if jugador not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        return jugar()
    
    print(f"La computadora eligió: {computadora}")
    
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == 'piedra' and computadora == 'tijera') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijera' and computadora == 'papel'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

if __name__ == "__main__":
    while True:
        jugar()
        otra = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if otra != 's':
            print("¡Gracias por jugar!")
            break
