# Guillaume
import driver


def cut(trameBruteKNX):
    """cut of the telegram as a carataire"""
    tout = ""
    champ = ""
    pariter = 0
    for x in range(len(trameBruteKNX)):
        # Start
        if(x % 13 == 0):
            champ = ""
            pariter = 0
        # Parity
        elif(x % 13 == 9):
            pariter += int(trameBruteKNX[x])
            if not (pariter % 2):
                tout += champ
        # 1 Stop and 2 Pause
        elif(x % 13 == 10 or x % 13 == 11 or x % 13 == 12):
            pass
        # Data
        else:
            champ = str(champ) + str(trameBruteKNX[x])
            if(trameBruteKNX[x] == "1"):
                pariter += 1

    return hex(int(tout[::-1], 2))


class CTrameKNX:
    def __init__(self, trameBruteKNX: str = None):
        if trameBruteKNX == None:
            # Simple constructor
            print("🤷‍♂️ Yes But Why ?")
        else:
            # Constructor overload with the trame
            self.trameBruteKNX = trameBruteKNX
            self.octetControle = ""
            self.adresseSoucre = ""
            self.adresseDestinataire = ""
            self.CR = ""
            self.LG = ""
            self.Data = ""
            self.securite = ""
        pass

    def traitement(self):

        print(cut(self.trameBruteKNX))

    def calculerChecksum(self):
        calcul = 1 + 1
        return calcul   # return a char
