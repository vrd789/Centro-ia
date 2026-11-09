class CentroIA:
    def __init__(self):
        self.nombre = "CENTRO IA 1.0"
        self.modelos = ["ChatGPT", "Gemini", "DeepSeek"]

    def mostrar_estado(self):
        print("=" * 35)
        print(self.nombre)
        print("Coordinador iniciado correctamente")
        print("=" * 35)

        for modelo in self.modelos:
            print(f"IA disponible: {modelo}")

    def recibir_tarea(self, tarea):
        print("\nNueva tarea recibida:")
        print(tarea)
        print("\nPendiente de asignación a los modelos.")


if __name__ == "__main__":
    centro = CentroIA()
    centro.mostrar_estado()
    centro.recibir_tarea("Iniciar sistema multi-IA")
