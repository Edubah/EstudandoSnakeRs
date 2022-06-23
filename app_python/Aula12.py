import requests

def retorna_responses(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = retorna_responses('https://globalacademy.com/')
    print(response)