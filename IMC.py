def avaliar_IMC(altura, peso):
    imc = peso / (altura ** 2)  
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

altura = float(input("Informe sua altura em metros: "))  
peso = float(input("Informe seu peso em quilos: "))  

resultado_IMC = avaliar_IMC(altura, peso)

print("Seu IMC é:", resultado_IMC)
