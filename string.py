def inverter_string(string):
    invertida = ''
    for caractere in string:
        invertida = caractere + invertida
    return invertida

# Exemplo de uso
entrada = input("Digite uma string: ")
saida = inverter_string(entrada)
print("String invertida:", saida)