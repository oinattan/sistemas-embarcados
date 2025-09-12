import time
import random

def main():
    for _ in range(5):
        valor_sensor = random.randint(0, 100)
        print(f"Valor do sensor: {valor_sensor}")
        time.sleep(1)

if __name__ == '__main__':
    main()
