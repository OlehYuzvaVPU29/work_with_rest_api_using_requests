from star_wars_api import StarWarsApi

api_client = StarWarsApi()

person = api_client.get_person(1)
print(f'Person name: {person.name}')
print(f'Person skin color: {person.skin_color}')

starship = api_client.get_starship(9)
print(f'Starship name: {starship.name}')
print(f'Starship crew: {starship.crew}')
print(f'Starship model: {starship.model}')

planet = api_client.get_planet(3)
print(f'Starship name: {planet.name}')
print(f'Starship crew: {planet.climate}')
print(f'Starship model: {planet.population}')
