# Guillaume
import driver


class CTrameKNX:
    def __init__(self, trameBruteKNX: str = None):
        if trameBruteKNX == None:
            # constuceur simple
            print("🤷‍♂️")
        else:
            # constructeur surcharger avec la trame
            self.trameBruteKNX = trameBruteKNX
        pass

    def checkEmissionNormaleOuReception(self):
        pass

    def calculerChecksum(self):
        calcul = 1 + 1
        return calcul   # return a char
