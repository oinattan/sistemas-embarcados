class SPI:
    def transferir(self, dado):
        print(f"Microcontrolador enviou: {dado}")
        resposta = "Sensor: dado lido"
        print(f"Sensor respondeu: {resposta}")

def main():
    spi = SPI()
    spi.transferir("Solicitar leitura")

if __name__ == '__main__':
    main()
