import requests
import json
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

def print_data_to_file(data):
    file = open("./output.json", 'w', encoding="utf-8")
    json.dump(data, file, ensure_ascii=False, indent=4)
    file.close()
    
def start():
    server = 'https://yandex.ru'
    server_status(server)
    get_text('https://api.github.com/events')
    print_data_to_file(get_json('http://yandex.ru'))
    
    
if __name__ == "__main__":
    start()
