def substituir_letra(string, letra_antiga, letra_nova):
    nova_string = ''
    for char in string:
        if char == letra_antiga:
            nova_string += letra_nova
        else:
            nova_string += char
    return nova_string

texto = input("Digite uma string: ")
letra_antiga = input("Digite a letra que deseja substituir: ")
letra_nova = input("Digite a nova letra: ")
nova_string = substituir_letra(texto, letra_antiga, letra_nova)
print("A string com as substituições é:", nova_string)
