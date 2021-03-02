# Guillaume
import driver


class CTrameKNX:
    def __init__(self, trameBruteKNX: str = None):
        if trameBruteKNX == None:
            # Simple constructor
            print("🤷‍♂️ Yes But Why ?")
        else:
            # Constructor overload with the trame
            self.trameBruteKNX = trameBruteKNX
            self.trameKNX = ""
            self.octetControle = ""
            self.adresseSoucre = ""
            self.adresseDestinataire = ""
            self.CR = ""
            self.LG = ""
            self.Data = ""
            self.securite = ""
            self.acquittement = ""
        pass

    def traitement(self):
        """cut of the telegram as a carataire"""

        total = ""
        champ = ""
        parity = 0
        for x in range(len(self.trameBruteKNX)):
            # Start
            if(x % 13 == 0):
                champ = ""
                parity = 0
            # Parity
            elif(x % 13 == 9):
                parity += int(self.trameBruteKNX[x])
                total = champ + total
                # if not (parity % 2):
                #     total = champ + total
            # 1 Stop and 2 Pause
            elif(x % 13 == 10 or x % 13 == 11 or x % 13 == 12):
                pass
            # Data
            else:
                champ = str(champ) + str(self.trameBruteKNX[x])
                if(self.trameBruteKNX[x] == "1"):
                    parity += 1

        # self.trameKNX = hex(int(total[::-1], 2))
        self.trameKNX = total[::-1]

    def CalculDesChamps(self):
        self.octetControle = self.trameKNX[:8]
        self.adresseSoucre = self.trameKNX[8:24]
        self.adresseDestinataire = self.trameKNX[24:40]
        self.typeCast = self.trameKNX[40:41]
        self.CR = self.trameKNX[41:44]
        self.LG = self.trameKNX[44:48]
        self.securite = self.trameKNX[-16:-8]
        self.acquittement = self.trameKNX[-8:]

        # Part of octectControle
        if(self.octetControle[2] == "0"):
            print('Extended frame')
        else:
            print('Standard frame')

        if(self.octetControle[2] == "0"):
            print('Repeated')
        else:
            print('Normal emission')

        if(self.octetControle[4] == "0" and self.octetControle[5] == "0"):
            print('Priority System')
        elif(self.octetControle[4] == "1" and self.octetControle[5] == "0"):
            print('Priority Urgent')
        elif(self.octetControle[4] == "0" and self.octetControle[5] == "1"):
            print('Priority Normal')
        elif(self.octetControle[4] == "1" and self.octetControle[5] == "1"):
            print('Priority Low')

        if(self.typeCast == 0):
            print('Unicast')
        else:
            print('Multicast')

        # faire les données
        self.Data = self.trameKNX[48:48+8*(int(self.LG)+1)]

        # somme de tout
        # somme += self.trameKNX[::]
        # somme foreach donnée

        if(hex(int(self.acquittement, 2)) == "0xcc"):
            print('ACK')
        elif(hex(int(self.acquittement, 2)) == "0x0c"):
            print('NAK')
        else:
            print('BUSY')

    def calculerChecksum(self):
        calcul = 1 + 1
        return calcul   # return a char
