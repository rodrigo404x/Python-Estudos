caracterList = []
for i in range (10):
    caractere = str(input(f"Digite o {i+1} caractere: "))
    caracterList.append(caractere)
    consoantes = []
    for char in caracterList:
        if char.lower() not in 'aeiou':
            consoantes.append(char)
            print(f'Foram lidas {len(consoantes)} consoantes: {consoantes}')
