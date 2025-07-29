
import requests

def get_coordinates(city):
    server = 'http://geocode-maps.yandex.ru/1.x/?'
    api = '8013b162-6b42-4997-9691-77b7074026e0'
    geocoder_request = f'{server}apikey={api}&geocode={city}&format=json'
    
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_coordinates = toponym["Point"]["pos"]
        return toponym_coordinates
    else:
        print(f"Ошибка выполнения запроса для города {city}:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        return None

def find_southernmost_city(cities):
    s_city = None
    flag1 = None
    
    for el in cities:
        coord = get_coordinates(el)
        if coord:
            flag2 = float(coord.split()[1])
            if flag1 is None or flag2 < flag1:
                flag1 = flag2
                s_city = el
    
    return s_city

def main():
    s = input("Введите список городов через запятую: ")
    a = [city.strip() for city in s.split(',')]
    
    ss = find_southernmost_city(a)
    if ss:
        print(f"Самый южный город: {ss}")
    else:
        print("Не удалось определить самый южный город.")

if __name__ == "__main__":
    main()
