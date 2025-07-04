import requests

# Надіслати GET-запит до API
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)

# Перевірити, чи відповідь успішна
if response.status_code == 200:
    heroes = response.json()
    for hero in heroes[:5]:  # Перші п'ять героїв
        print(f"Ім'я: {hero['name']}")
        print("Сили:")
        for stat, value in hero['powerstats'].items():
            print(f"  {stat.capitalize()}: {value}")
        print("\n" + "-"*40 + "\n")
else:
    print("Не вдалося отримати дані про героїв.")
