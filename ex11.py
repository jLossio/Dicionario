votos = {}

while True:
    candidato = input("Digite o nome do candidato (ou 'fim' para encerrar:) ")
    if candidato == 'fim':
        break

    #verifica se o candidato já recebeu votos antes
    if candidato in votos:
        votos[candidato] += 1
    else:
        votos[candidato] = 1

print ("Resultado da voação: ")
for candidato, quantidade in votos.items():
    print(candidato, "-", quantidade, "votos")

print (votos)