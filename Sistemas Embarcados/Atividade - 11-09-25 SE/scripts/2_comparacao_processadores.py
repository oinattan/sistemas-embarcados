def main():
    processador = {"Núcleos": 4, "RAM": "Não integrada", "Uso": "PC/Servidor"}
    microcontrolador = {"Núcleos": 1, "RAM": "Integrada", "Uso": "Dispositivos embarcados"}
    soc = {"Núcleos": 4, "RAM": "Integrada", "Periféricos": "Integrados", "Uso": "Celulares, IoT"}

    print("Processador:", processador)
    print("Microcontrolador:", microcontrolador)
    print("SoC:", soc)
    print("\nDiferença principal: Microcontroladores e SoCs têm periféricos integrados, processadores não.")

if __name__ == '__main__':
    main()
