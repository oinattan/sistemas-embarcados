import random

def main():
    temperatura_limite = 75
    temperatura = random.randint(60, 90)
    print(f"Temperatura atual: {temperatura}°C")
    if temperatura > temperatura_limite:
        print("ALERTA: Temperatura crítica ultrapassada!")
    else:
        print("Temperatura dentro do limite seguro.")

if __name__ == '__main__':
    main()
