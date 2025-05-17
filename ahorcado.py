# Def hace referencia a la creacion de funciones para poder reutilizar codigo
# Clase que gestiona la palabra secreta y el progreso del juego
class Palabra:
    def __init__(self):
        self.categoria = ""
        self.palabra_secreta = ""
        self.letras_adivinadas = []

    def configurar_palabra(self):
        print("=== Configuración de la palabra secreta ===")
        self.categoria = input("Ingresa la categoría o pista de la palabra: ")

        print("Ahora escribe la palabra secreta (el otro jugador no debe verla):")
        self.palabra_secreta = self._entrada_oculta().lower()

        print("\nPalabra registrada exitosamente.\n")

    def _entrada_oculta(self):
        # Simulación para ocultar la palabra con asteriscos
        palabra = ""
        while True:
            letra = input("Letra (enter para terminar): ")
            if letra == "":
                break
            print("*", end="")
            palabra += letra
        print()
        return palabra

    def mostrar_progreso(self):
        progreso = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        return progreso.strip()

    def adivinar(self, letra):
        letra = letra.lower()
        if letra in self.letras_adivinadas:
            print("Ya habías ingresado esa letra.")
            return False
        self.letras_adivinadas.append(letra)
        return letra in self.palabra_secreta

    def esta_completa(self):
        for letra in self.palabra_secreta:
            if letra not in self.letras_adivinadas:
                return False
        return True


# Clase que controla el flujo del juego
class JuegoAhorcado:
    def __init__(self):
        self.palabra = Palabra()
        self.intentos_fallidos = 0
        self.max_fallos = 6

    def iniciar(self):
        print("=== Bienvenido al juego del Ahorcado ===")
        self.palabra.configurar_palabra()
        self.jugar()

    def jugar(self):
        while self.intentos_fallidos < self.max_fallos and not self.palabra.esta_completa():
            self.mostrar_estado()
            letra = input("Ingresa una letra: ").lower()

            if not letra.isalpha() or len(letra) != 1:
                print("Entrada inválida. Ingresa solo una letra.")
                continue

            if self.palabra.adivinar(letra):
                print("¡Bien hecho! La letra está en la palabra.")
            else:
                self.intentos_fallidos += 1
                print("Incorrecto. Te queda(n):", self.max_fallos - self.intentos_fallidos)

        self.mostrar_estado(final=True)
        if self.palabra.esta_completa():
            print("¡Felicidades! Adivinaste la palabra.")
        else:
            print("Has perdido. La palabra era:", self.palabra.palabra_secreta)

    def mostrar_estado(self, final=False):
        print("\nCategoría:", self.palabra.categoria)
        print("Palabra:", self.palabra.mostrar_progreso())
        self.dibujar_ahorcado()
        if not final:
            print("Letras adivinadas:", ", ".join(self.palabra.letras_adivinadas))

    def dibujar_ahorcado(self):
        dibujo = [
            " +---+",
            " |   |",
            "     |",
            "     |",
            "     |",
            "     |",
            "======" 
        ]

        if self.intentos_fallidos > 0:
            dibujo[2] = " O   |"  # cabeza
        if self.intentos_fallidos > 1:
            dibujo[3] = " |   |"  # torso
        if self.intentos_fallidos > 2:
            dibujo[3] = "/|   |"  # brazos
        if self.intentos_fallidos > 4:
            dibujo[3] = "/|\\  |"  # pierna izquierda
        if self.intentos_fallidos > 5:
            dibujo[4] = "/ \\  |"  # pierna derecha

        for linea in dibujo:
            print(linea)


# Punto de entrada del programa
juego = JuegoAhorcado()
juego.iniciar()
