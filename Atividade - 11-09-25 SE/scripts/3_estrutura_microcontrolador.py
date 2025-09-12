class CPU:
    def executar(self):
        print("CPU executando instruções.")

class Memoria:
    def __init__(self):
        self.dados = {}

class GPIO:
    def set_high(self, pino):
        print(f"Pino {pino} em nível ALTO.")

class Periferico:
    def acionar(self):
        print("Periférico acionado.")

class Microcontrolador:
    def __init__(self):
        self.cpu = CPU()
        self.memoria = Memoria()
        self.gpio = GPIO()
        self.periferico = Periferico()

def main():
    mcu = Microcontrolador()
    mcu.cpu.executar()
    mcu.gpio.set_high(1)
    mcu.periferico.acionar()

if __name__ == '__main__':
    main()
