def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Conversor de Temperatura")
    print("Escolha a conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Kelvin para Celsius")
    print("5. Fahrenheit para Kelvin")
    print("6. Kelvin para Fahrenheit")

    choice = int(input("Digite o número da conversão desejada: "))

    if choice == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius} °C = {celsius_to_fahrenheit(celsius):.2f} °F")
    elif choice == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit} °F = {fahrenheit_to_celsius(fahrenheit):.2f} °C")
    elif choice == 3:
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius} °C = {celsius_to_kelvin(celsius):.2f} K")
    elif choice == 4:
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"{kelvin} K = {kelvin_to_celsius(kelvin):.2f} °C")
    elif choice == 5:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit} °F = {fahrenheit_to_kelvin(fahrenheit):.2f} K")
    elif choice == 6:
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"{kelvin} K = {kelvin_to_fahrenheit(kelvin):.2f} °F")
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
