class UART:
    def __init__(self):
        self.buffer = ""
    def enviar(self, dado):
        print(f"Enviando: {dado}")
        self.buffer = dado
    def receber(self):
        print(f"Recebido: {self.buffer}")

def main():
    uart1 = UART()
    uart2 = UART()

    uart1.enviar("Olá, dispositivo 2!")
    uart2.buffer = uart1.buffer
    uart2.receber()

if __name__ == '__main__':
    main()
