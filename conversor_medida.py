def metros_to_centimetros(metros):
    return metros * 100

def centimetros_to_metros(centimetros):
    return centimetros / 100

def polegadas_to_centimetros(polegadas):
    return polegadas * 2.54

def centimetros_to_polegadas(centimetros):
    return centimetros / 2.54

def pes_to_centimetros(pes):
    return pes * 30.48

def centimetros_to_pes(centimetros):
    return centimetros / 30.48

def main():
    print("Conversor de Medidas")
    print("Escolha a conversão:")
    print("1. Metros para Centímetros")
    print("2. Centímetros para Metros")
    print("3. Polegadas para Centímetros")
    print("4. Centímetros para Polegadas")
    print("5. Pés para Centímetros")
    print("6. Centímetros para Pés")

    choice = int(input("Digite o número da conversão desejada: "))

    if choice == 1:
        metros = float(input("Digite o valor em metros: "))
        print(f"{metros} metros = {metros_to_centimetros(metros)} centímetros")
    elif choice == 2:
        centimetros = float(input("Digite o valor em centímetros: "))
        print(f"{centimetros} centímetros = {centimetros_to_metros(centimetros)} metros")
    elif choice == 3:
        polegadas = float(input("Digite o valor em polegadas: "))
        print(f"{polegadas} polegadas = {polegadas_to_centimetros(polegadas)} centímetros")
    elif choice == 4:
        centimetros = float(input("Digite o valor em centímetros: "))
        print(f"{centimetros} centímetros = {centimetros_to_polegadas(centimetros)} polegadas")
    elif choice == 5:
        pes = float(input("Digite o valor em pés: "))
        print(f"{pes} pés = {pes_to_centimetros(pes)} centímetros")
    elif choice == 6:
        centimetros = float(input("Digite o valor em centímetros: "))
        print(f"{centimetros} centímetros = {centimetros_to_pes(centimetros)} pés")
    else:
        print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
