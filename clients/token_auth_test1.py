import requests
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


def client():

    token = 'Token 40e87dbdaea00fd1ad5eb8884336c140cece0a39'

    headers = {
        'Autohorization': token,
    }

    response = requests.get(
        url='http://127.0.0.1:8000/api/kullaniciProfilleri/',
        headers=headers
        # data = credentials
    )

    print(f'Status Code={response.status_code}')

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()


# credentials = {
    #     'username' : 'testUser',
    #     'passsword' : 'Kullanici1.'
    # }
