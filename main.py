from Sexagesimales_a_Radianes import ConversorAngulos
if __name__ == "__main__":
    conversor = ConversorAngulos()

    # Convertir de grados a radianes
    grados = float(input("Ingresa el ángulo en grados: "))
    radianes = conversor.grados_a_radianes(grados)
    print(f"{grados} grados son {radianes:.4f} radianes")

    # Convertir de radianes a grados
    radianes = float(input("Ingresa el ángulo en radianes: "))
    grados = conversor.radianes_a_grados(radianes)
    print(f"{radianes:.4f} radianes son {grados:.4f} grados")
