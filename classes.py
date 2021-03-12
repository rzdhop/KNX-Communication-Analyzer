# Guillaume
import driver
from logs import logs

# init the repo of the logs
log = logs()


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
            self.CRLG = ""
            self.modCast = ""
            self.CR = ""
            self.LG = ""
            self.Data = ""
            self.securite = ""
            self.acquittement = ""

            self.typeFrame = ""
            self.typeEmision = ""
            self.typePriority = ""
            self.typeCast = ""
            self.typeAcquittement = ""

            self.traitement()
            self.CalculDesChamps()

    def traitement(self):
        self.trameKNX = self.trameBruteKNX.upper()

    def CalculDesChamps(self):
        self.octetControle = self.trameKNX[:2]
        self.adresseSoucre = self.trameKNX[2:6]
        self.adresseDestinataire = self.trameKNX[6:10]
        # probleme est ici au niveau du CR car le data n'est pas bon
        # self.CRLG = bin(int(self.trameKNX[10:12], 16))[2:]
        self.CRLG = bin(int(self.trameKNX[10:12], 16))[2:].zfill(len(self.trameKNX[10:12]) * 4)
        self.Cast = self.CRLG[0:1]
        self.CR = int(self.CRLG[1:4], 2)
        self.LG = self.CRLG[4:8]
        self.Data = self.trameKNX[12:12+2*(int(self.LG, 2)+1)]
        self.securite = self.trameKNX[-4:-2]
        self.acquittement = self.trameKNX[-2:]

        # Part of octectControle
        if(self.octetControle[0] == "1"):
            self.typeFrame = 'Extended frame'
            self.typeEmision = 'Repeated'
        elif(self.octetControle[0] == "9"):
            self.typeFrame = 'Standard frame'
            self.typeEmision = 'Repeated'
        elif(self.octetControle[0] == "3"):
            self.typeFrame = 'Extended frame'
            self.typeEmision = 'Normal emission'
        elif(self.octetControle[0] == "B"):
            self.typeFrame = 'Standard frame'
            self.typeEmision = 'Normal emission'

        if(self.octetControle[1] == "0"):
            self.typePriority = 'Priority System'
        elif(self.octetControle[1] == "8"):
            self.typePriority = 'Priority Urgent'
        elif(self.octetControle[1] == "4"):
            self.typePriority = 'Priority Normal'
        elif(self.octetControle[1] == "C"):
            self.typePriority = 'Priority Low'

        if(self.modCast == 0):
            self.typeCast = 'Unicast'
        else:
            self.typeCast = 'Multicast'

        if(self.acquittement == "CC"):
            self.typeAcquittement = 'ACK'
        elif(self.acquittement == "0C"):
            self.typeAcquittement = 'NAK'
        else:
            self.typeAcquittement = 'BUSY'

    def calculerChecksum(self):
        tab = [0, 0, 0, 0, 0, 0, 0, 0]

        data = (bin(int(self.trameKNX[:-4], 16))[2:]).zfill(len(self.trameKNX[:-4]) * 4)

        for counter, value in enumerate(data):
            if(counter % 8 == 0):
                tab[0] += int(value)
            elif(counter % 8 == 1):
                tab[1] += int(value)
            elif(counter % 8 == 2):
                tab[2] += int(value)
            elif(counter % 8 == 3):
                tab[3] += int(value)
            elif(counter % 8 == 4):
                tab[4] += int(value)
            elif(counter % 8 == 5):
                tab[5] += int(value)
            elif(counter % 8 == 6):
                tab[6] += int(value)
            elif(counter % 8 == 7):
                tab[7] += int(value)

        print(tab)

        sec = (bin(int(self.securite, 16))[2:]).zfill(len(self.securite) * 4)

        for counter, value in enumerate(sec):
            if not(int(value) + tab[counter] % 2):
                return False

        return True

    def writeInfo(self):
        txt = "Info de trame"
        log.info(txt)

# # Guillaume
# import driver
# from logs import logs

# # init the repo of the logs
# log = logs()


# class CTrameKNX:
#     def __init__(self, trameBruteKNX: str = None):
#         if trameBruteKNX == None:
#             # Simple constructor
#             print("🤷‍♂️ Yes But Why ?")
#         else:
#             # Constructor overload with the trame
#             self.trameBruteKNX = trameBruteKNX
#             self.trameKNX = ""
#             self.octetControle = ""
#             self.adresseSoucre = ""
#             self.adresseDestinataire = ""
#             self.modCast = ""
#             self.CR = ""
#             self.LG = ""
#             self.Data = ""
#             self.securite = ""
#             self.acquittement = ""

#             self.typeFrame = ""
#             self.typeEmision = ""
#             self.typePriority = ""
#             self.typeCast = ""
#             self.typeAcquittement = ""
#         pass

#     def traitement(self):
#         """cut of the telegram as a carataire"""

#         total = ""
#         champ = ""
#         parity = 0
#         for x in range(len(self.trameBruteKNX)):
#             # Start
#             if(x % 13 == 0):
#                 champ = ""
#                 parity = 0
#             # Parity
#             elif(x % 13 == 9):
#                 parity += int(self.trameBruteKNX[x])
#                 total = champ + total
#                 # if not (parity % 2):
#                 #     total = champ + total
#             # 1 Stop and 2 Pause
#             elif(x % 13 == 10 or x % 13 == 11 or x % 13 == 12):
#                 pass
#             # Data
#             else:
#                 champ = str(champ) + str(self.trameBruteKNX[x])
#                 if(self.trameBruteKNX[x] == "1"):
#                     parity += 1

#         # self.trameKNX = hex(int(total[::-1], 2))
#         self.trameKNX = total[::-1]

#     def CalculDesChamps(self):
#         self.octetControle = self.trameKNX[:8]
#         self.adresseSoucre = self.trameKNX[8:24]
#         self.adresseDestinataire = self.trameKNX[24:40]
#         self.modCast = self.trameKNX[40:41]
#         self.CR = self.trameKNX[41:44]
#         self.LG = self.trameKNX[44:48]
#         self.Data = self.trameKNX[48:48+8*(int(self.LG)+1)]
#         self.securite = self.trameKNX[-16:-8]
#         self.acquittement = self.trameKNX[-8:]

#         # Part of octectControle
#         if(self.octetControle[2] == "0"):
#             self.typeFrame = 'Extended frame'
#         else:
#             self.typeFrame = 'Standard frame'

#         if(self.octetControle[2] == "0"):
#             self.typeEmision = 'Repeated'
#         else:
#             self.typeEmision = 'Normal emission'

#         if(self.octetControle[4] == "0" and self.octetControle[5] == "0"):
#             self.typePriority = 'Priority System'
#         elif(self.octetControle[4] == "1" and self.octetControle[5] == "0"):
#             self.typePriority = 'Priority Urgent'
#         elif(self.octetControle[4] == "0" and self.octetControle[5] == "1"):
#             self.typePriority = 'Priority Normal'
#         elif(self.octetControle[4] == "1" and self.octetControle[5] == "1"):
#             self.typePriority = 'Priority Low'

#         if(self.modCast == 0):
#             self.typeCast = 'Unicast'
#         else:
#             self.typeCast = 'Multicast'

#         if(hex(int(self.acquittement, 2)) == "0xcc"):
#             self.typeAcquittement = 'ACK'
#         elif(hex(int(self.acquittement, 2)) == "0x0c"):
#             self.typeAcquittement = 'NAK'
#         else:
#             self.typeAcquittement = 'BUSY'

#     def calculerChecksum(self):
#         tab = [0, 0, 0, 0, 0, 0, 0, 0]

#         for counter, value in enumerate(self.trameKNX[:-16]):
#             if(counter % 8 == 0):
#                 tab[0] += int(value)
#             elif(counter % 8 == 1):
#                 tab[1] += int(value)
#             elif(counter % 8 == 2):
#                 tab[2] += int(value)
#             elif(counter % 8 == 3):
#                 tab[3] += int(value)
#             elif(counter % 8 == 4):
#                 tab[4] += int(value)
#             elif(counter % 8 == 5):
#                 tab[5] += int(value)
#             elif(counter % 8 == 6):
#                 tab[6] += int(value)
#             elif(counter % 8 == 7):
#                 tab[7] += int(value)

#         for counter, value in enumerate(self.securite):
#             if not(int(value) + tab[counter] % 2):
#                 return False

#         return True

#     def writeInfo(self):
#         txt = "Info de trame"
#         log.info(txt)
