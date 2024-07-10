class Buah:
    def __init__(self, nama, warna, rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa

    def getNama(self):
        return self.__nama
    
    def getWarna(self):
        return self.__warna
    
    def getRasa(self):
        return self.__rasa
    
    def setNama(self, namaBaru):
        self.__nama = namaBaru

    def setWarna(self, warnaBaru):
        self.__warna = warnaBaru

    def setRasa(self, rasaBaru):
        self.__rasa = rasaBaru

    def infoBuah(self):
        return f'Nama : {self.getNama()}, \nWarna : {self.getWarna()}, \nRasa : {self.getRasa()}'
    
class Mangga(Buah):
    def __init__(self, vitamin, nama, warna, rasa):
        super().__init__(nama, warna, rasa)
        self.__vitamin = vitamin

    def getVitamin(self):
        return self.__vitamin
    
    def setVitamin(self, vitaminBaru):
        self.__vitamin = vitaminBaru

    def infoMangga(self):
        return f'{self.infoBuah()}, \nVitamin : {self.getVitamin()}'

object = Mangga('C', 'Arumanis', 'Kuning', 'Manis')
print(object.infoMangga())
