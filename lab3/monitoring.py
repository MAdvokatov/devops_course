import time

import requests
import json
import logging

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
        logging.info(
            "The server is up and running ,will skip the translation of the other messages below to save time.")
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])
    except requests.exceptions.RequestException as e:
        logging.error("ERROR WITHIN THE SERVER ")


if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        time.sleep(60)
