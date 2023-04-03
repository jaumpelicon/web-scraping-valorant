import requests
import json
from bs4 import BeautifulSoup

for page in range(1,2):
    # Define a URL a ser acessada
    url = "https://tracker.gg/valorant/leaderboards/ranked/all/default?page={}&region=br".format(page)

    # Envia uma solicitação GET para a URL e armazena a resposta
    response = requests.get(url)
    
    # Cria um objeto BeautifulSoup com o conteúdo da resposta
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra a tabela de liderança na página
    table = soup.find('table', {'class': 'trn-table'})
    if not table:
        continue
    # Encontra todas as linhas na tabela
    rows = table.find_all('tr')
    if not rows:
        continue
    # Percorre cada linha e imprime a classificação, nome do jogador e pontuação
    for row in rows:
        # Pula a linha de cabeçalho
        if row.has_attr('class') and 'header-row' in row['class']:
            continue
        rank = row.find('td', {'class': 'rank'}) 
        player = row.find('td', {'class': 'username'}) 
        score = row.find('td', {'class': 'stat highlight'}) 
        # Faz uma verificação do atributo para imprimir e evitar o erro :
        # AttributeError: 'NoneType' object has no attribute 'text'
        if not rank or not player or not score:
            continue
        # Transformando em json a respostas
        response = { 'rank_position':rank.text, 'player_name': player.text, 'points': score.text}
        jsonString = json.dumps(response, indent=4)

        print(jsonString)
        print('\n')