import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success status code : {response.status_code}')
        # print(f'\nContent : {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil dari {url}')
        print(f'Title : {soup.title.string}')
    else:
        print(f'Ooopsssss, ada kesalahan request {response.status_code}')
except Exception as e:
    print(f'Ooopsssss, ada kesalahan')
print('Program End')
