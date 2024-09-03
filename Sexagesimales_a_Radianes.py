import math

class ConversorAngulos:
    def grados_a_radianes(self, grados: float) -> float:
        return grados * (math.pi / 180)

    def radianes_a_grados(self, radianes: float) -> float:
        return radianes * (180 / math.pi)
