def main():
    plataforma = "ESP32"
    if plataforma == "Arduino":
        print("IDE recomendada: Arduino IDE. Compilador: avr-gcc.")
    elif plataforma == "Raspberry Pi":
        print("IDE recomendada: Thonny. Compilador: Python (interpretado).")
    elif plataforma == "ESP32":
        print("IDE recomendada: VS Code + PlatformIO. Compilador: xtensa-esp32-elf-gcc.")
    else:
        print("Plataforma não reconhecida.")

if __name__ == '__main__':
    main()
