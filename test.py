import requests


def test_token_auth():
    response = requests.post("http://localhost:8000/api/auth/", json={"username":"natali", "password":"140917"})

    print(response.status_code)
    print(response.json())

    token = response.json()['token']
    response = requests.get('http://localhost:8000/api/vacancies/', headers={'Authorization': f'Token {token}'})

    print(response.status_code)
    print(response.json())


def test_registration():
    registration_data = {
        'username':'test',
        'password':'zxcv1234!'
    }

    response = requests.post('http://localhost:8000/api/register/', json=registration_data)

    print(response.status_code)
    print(response.json())


def get_company_profile():
    token = 'd05eae248744af84477fc4801bd98a2c07c3141e'

    response = requests.get('http://localhost:8000/api/vacancies/', headers={'Authorization': f'Token {token}'})
    print(response.status_code)
    print(response.json())


if __name__ == "__main__":
    get_company_profile()