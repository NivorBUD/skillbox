import json
import requests

my_req = requests.get('https://swapi.dev/api//starships/10')

data = dict(sorted(filter(lambda item: item[0] in
                                       ['max_atmosphering_speed', 'pilots', 'name', 'starship_class'], json.loads(my_req.text).items())))

data['ship_name'] = data.pop('name')

pilots_list = list(map(lambda pilot_info: dict(filter(lambda info: info[0] in ['height', 'homeworld', 'mass', 'name'],
                                                      json.loads(requests.get(pilot_info).text).items())), data['pilots']))

for i in range(len(pilots_list)):
    pilot = pilots_list[i]
    pilot['homeworld_url'] = pilot.pop('homeworld')
    pilot['homeworld'] = json.loads(requests.get(pilot['homeworld_url']).text)['name']
    pilots_list[i] = dict(pilot.items())

data['pilots'] = pilots_list

print(data)

with open('StarWars.json', 'w') as file:
    json.dump(data, file, indent=4)
