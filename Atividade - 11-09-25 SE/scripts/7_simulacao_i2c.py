class I2C:
    def enviar(self, endereco, dado):
        print(f"Mestre enviou para {endereco}: {dado}")
    def receber(self, endereco):
        print(f"Escravo {endereco} respondeu: OK")

def main():
    i2c = I2C()
    i2c.enviar(0x10, "Comando")
    i2c.receber(0x10)

if __name__ == '__main__':
    main()
