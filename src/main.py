import random
import matplotlib.pyplot as plt

# Datos de las tecnologías y sectores
tecnologias = ["IA", "Automatización", "Blockchain", "5G"]
sectores = ["Industria", "Educación", "Salud", "Economía"]

# Impacto de las tecnologías en los sectores
impacto_tecnologias = {
    "IA": [random.randint(1, 10) for _ in range(4)],
    "Automatización": [random.randint(1, 10) for _ in range(4)],
    "Blockchain": [random.randint(1, 10) for _ in range(4)],
    "5G": [random.randint(1, 10) for _ in range(4)]
}

# Función para mostrar el impacto de una tecnología
def mostrar_impacto(tecnologia):
    if tecnologia not in impacto_tecnologias:
        print("Tecnología no válida.")
        return

    impacto = impacto_tecnologias[tecnologia]
    print(f"Impacto de {tecnologia} en los sectores:")
    for sector, valor in zip(sectores, impacto):
        print(f"{sector}: {valor}/10")

# Función para generar un gráfico de barras
def generar_grafico(tecnologia):
    if tecnologia not in impacto_tecnologias:
        print("Tecnología no válida.")
        return

    impacto = impacto_tecnologias[tecnologia]
    plt.bar(sectores, impacto)
    plt.title(f"Impacto de {tecnologia} en diferentes sectores")
    plt.xlabel('Sectores')
    plt.ylabel('Impacto (1-10)')
    plt.show()

# Función principal de menú
def menu():
    print("Bienvenido al visualizador del impacto de las nuevas tecnologías.")
    print("Selecciona una tecnología para visualizar su impacto:")
    for i, tecnologia in enumerate(tecnologias, 1):
        print(f"{i}. {tecnologia}")

    opcion = int(input("Elige una opción (1-4): "))
    if opcion < 1 or opcion > 4:
        print("Opción no válida.")
        return

    seleccion_tecnologia = tecnologias[opcion - 1]
    mostrar_impacto(seleccion_tecnologia)
    generar_grafico(seleccion_tecnologia)

# Ejecutar el programa
if __name__ == "__main__":
    menu()
    
