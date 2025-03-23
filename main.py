# Задание 1: Получение данных
# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

params = {
    'q' : 'html'
}

response = requests.get('https://api.github.com', params=params)

print(response.status_code)

response_json = response.json()
pprint.pprint(response_json)

# Задание 2: Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

url ='https://jsonplaceholder.typicode.com/posts'
params = {
    'userId' : 1
}
response = requests.get(url, params=params)

print(response.status_code)

response_json = response.json()
pprint.pprint(response_json)

# Задание 3: Отправка данных
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа

url ='https://jsonplaceholder.typicode.com/posts'
data = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1
}

response = requests.post(url, data=data)

print(response.status_code)

response_json = response.json()
print(response_json)