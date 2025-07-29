import sys
import requests

def get_coordinates(api_key, address):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        longitude, latitude = pos.split(" ")
        return longitude, latitude
    else:
        print("Ошибка при получении координат")
        return None, None


def get_district(api_key, longitude, latitude):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": api_key,
        "geocode": f"{longitude},{latitude}",
        "kind": "district",
        "format": "json"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Извлекаем название района
        district = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
        return district
    else:
        print("Ошибка при получении района")
        return None


def main():
    if len(sys.argv) < 2:
        return

    address = " ".join(sys.argv[1:])
    api_key = "ваш_api_ключ" 
    longitude, latitude = get_coordinates(api_key, address)
    if longitude and latitude:
        print(f"Координаты: {longitude}, {latitude}")
        # Получаем район
        district = get_district(api_key, longitude, latitude)
        if district:
            print(f"Район: {district}")
        else:
            print("Не удалось определить район")
    else:
        print("Не удалось определить координаты")

if __name__ == "__main__":
    main()
