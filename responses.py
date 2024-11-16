from random import choice,randint
import requests
import json
import wordninja

def get_response(user_input:str) -> str:
    command: str = user_input.lower()
    
    if command.startswith('porygon'):
        name: str = command[len('porygon'):].strip().title()
        print(f'{name}')
        data = retrieve_data(name)
        return f'**{name}**\n(Usage: {data[0]}%)\n⚔️ __Moveset:__\n{split_with_wordninja(data[1][0])}\n{split_with_wordninja(data[1][1])}\n{split_with_wordninja(data[1][2])}\n{split_with_wordninja(data[1][3])}\n:apple: __Items:__\n{split_with_wordninja(data[2][0])}\n{split_with_wordninja(data[2][1])}\n{split_with_wordninja(data[2][2])}\n{split_with_wordninja(data[2][3])}\n:gem: __Teras:__\n{data[3][0]}\n{data[3][1]}\n{data[3][2]}\n{data[3][3]}\n:page_facing_up: __Spreads:__\n{data[4][0]}\n{data[4][1]}\n{data[4][2]}\n{data[4][3]}\n'

        
        
def retrieve_data(name:str):
    response = requests.get('https://www.smogon.com/stats/2024-10/chaos/gen9ou-1695.json')
    response_json = json.loads(response.text)
    data = response_json['data']
    data = data[name]
    print(name)
    
    usage = data['usage'] * 100
    print(usage)
    
    moves = data['Moves']
    sorted_moves = sort_data(moves)
    
    items = data['Items']
    sorted_items = sort_data(items)
    
    teras = data['Tera Types']
    sorted_teras = sort_data(teras)
    
    spreads = data['Spreads']
    sorted_spreads = sort_data(spreads)
    
    return [usage, sorted_moves, sorted_items, sorted_teras, sorted_spreads]


def sort_data(data):
    s = (sorted(data.items(), key=lambda item:item[1],reverse=True))[:4]
    arr = []
    for item in s:
        arr.append(item[0].title())
    print(arr)
    return arr
    
def split_with_wordninja(s):
    words = wordninja.split(s)
    # Capitalize each word
    words_capitalized = [word.capitalize() for word in words]
    return ' '.join(words_capitalized)

    

