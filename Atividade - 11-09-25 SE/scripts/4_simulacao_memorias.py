class ROM:
    def __init__(self, dados):
        self.dados = dados
    def ler(self):
        return self.dados

class RAM:
    def __init__(self):
        self.dados = None
    def escrever(self, valor):
        self.dados = valor
    def ler(self):
        return self.dados

class EEPROM:
    def __init__(self):
        self.dados = None
    def escrever(self, valor):
        self.dados = valor
    def ler(self):
        return self.dados

def main():
    rom = ROM("Firmware v1.0")
    ram = RAM()
    eeprom = EEPROM()

    ram.escrever("Dado temporário")
    eeprom.escrever("Configuração salva")

    print("ROM:", rom.ler())
    print("RAM:", ram.ler())
    print("EEPROM:", eeprom.ler())

if __name__ == '__main__':
    main()
