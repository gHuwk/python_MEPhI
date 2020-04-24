import requests
import json
from lxml.html import fromstring

# from selenium import webdriver
#
# def get_page(url):
#     driver = webdriver.Firefox()
#     driver.get(url)
#
#     html = fromstring(driver.page_source)
#
#     driver.close()
#
#     return html


def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        html = fromstring(response.text)

        return html
    else:
        raise ConnectionRefusedError(f"Сервер вернул код статуса с номером: {response.status_code}")


def get_data(html):
    all_urls = html.xpath("//a")
    story_urls = []

    for element_url in all_urls:
        url = element_url.xpath("@href")
        if url:
            url = url[0]
            if "https://yandex.ru/news/" in url and "/story/" in url:
                if element_url.text_content():
                    story_urls.append((url, element_url.text_content()))

    return story_urls


def save_json(file_path, data):
    new_data = []
    for item in data:
        new_data.append(
            {
                "title": item[1],
                "url": item[0]
            }
        )

    json_content = json.dumps(new_data)

    # file = open(file_path, "w", encoding="utf-8")
    # file.write(json_content)
    # file.close()

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

    return file_path


def start():
    html = get_page("https://yandex.ru")
    data = get_data(html)
    file_path = save_json("recent_news.json", data)

    print(f"Собраны и сохранены последние новости по пути: {file_path}")


if __name__ == "__main__":
    start()
