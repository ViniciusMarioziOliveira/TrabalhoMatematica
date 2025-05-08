def volume_prisma(largura, comprimento, altura):
    area_base = largura * comprimento
    volume = area_base * altura
    return volume

# Exemplo de uso
largura = float(input("Digite a largura da base (em metros): "))
comprimento = float(input("Digite o comprimento da base (em metros): "))
altura = float(input("Digite a altura do prisma (em metros): "))

volume = volume_prisma(largura, comprimento, altura)
print(f"O volume do prisma é {volume:.2f} metros cúbicos.")