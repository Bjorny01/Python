class Djur:
    def __init__(self, namn, ide, vaknar, somnar, matningstid):
        self.namn = namn
        self.ide = ide
        self.vaknar = vaknar
        self.somnar = somnar
        self.matningstid = matningstid

    def get_namn(self):
        return self.namn

    def get_ide(self):
        return self.ide

    def get_vaknar(self):
        return self.vaknar

    def get_somnar(self):
        return self.somnar

    def get_matningstid(self):
        return self.matningstid
