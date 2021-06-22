with open('contatos.csv') as arq:
    lista = list()
    for linha in arq:
        dados = linha.split(';')
        for i in range(0, 3):
            if '@' in dados[i]:
                email = dados[i].strip('\n')
            elif dados[i].isalpha():
                nome = dados[i].strip('\n')
            else:
                telefone = dados[i].strip('\n')
        lista.append([nome, telefone, email])
print(lista)
