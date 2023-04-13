estudantes = {
    'João':{
    'idade': 18,
    'cidade': 'São Paulo',
    'notas': [7.5, 8.0, 9.0]
    },
    'Maria':{
    'idade': 20,
    'cidade': 'Rio de Janeiro',
    'notas': [6.5, 7.0, 8.6]
    },
    'Pedro':{
    'idade': 19,
    'cidade': 'Belo Horizonte',
    'notas': [8.5, 8.0, 9.5]
    },
}
#imprimir a idade do João
print ('A idade de João é: '+ str(estudantes['João']['idade']))
#adicionar uma nova nta para maria 
estudantes ['Maria']['notas'].append(9.0)

for estudantes, info in estudantes.items():
    print(estudantes + ':')
    print('idade: ' + str(info['idade']))
    print('cidade: ' + str(info['cidade']))
    print('notas: ' + str(info['notas']))
    print('media: ' + str(sum(info['notas']) / len(info['notas'])))