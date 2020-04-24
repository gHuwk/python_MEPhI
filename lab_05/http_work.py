import requests
response = requests.get('https://yandex.ru')


def get_status(response):
    code = response.status_code
    if code == 404:
        print("Not Found")
    if code == 400:
        print("Bad Request")
    if code == 200:
        print("OK!")
    if code == 204:
        print("No Content")
    return code

def server_status(server):
    response = requests.get(server)
    print("Status:")
    return get_status(response)

def get_text(server):
    response = requests.get(server)
    text = response.text
    print(text)
    return text
def get_json(server):
    response = requests.get(server)
    json = response.json()
    
def start():
    server = 'https://yandex.ru'
    server_status(server)
    get_text('https://api.github.com/events')
    
if __name__ == "__main__":
    start()
