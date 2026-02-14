pessoas = [
    
    {'Nome': 'Lucas Santos', 'Idade': 22, 'Profissão': 'Desenvolvedor de Software'},
    {'Nome': 'Maria Texeira', 'Idade': 30, 'Profissão': 'Designer de Jogos'},
    {'Nome': 'Jõao Silva', 'Idade': 28, 'Profissão': 'Analista de Dados'},
    {'Nome': 'Gabriela Clicia', 'Idade': 25, 'Profissão': 'Professora'},
    {'Nome': 'Gustavo Tominaga', 'Idade': 24, 'Profissão': 'Geologo'}
    ]

for pessoa in pessoas:
    print(f'Nome: {pessoa["Nome"]}, Idade: {pessoa["Idade"]}, Profissão: {pessoa["Profissão"]}')