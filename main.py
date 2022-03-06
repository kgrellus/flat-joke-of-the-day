import html.parser

import requests

from os import getenv
import json
import logging

from bs4 import BeautifulSoup


def init_loggers():
    logging.basicConfig(
        level='INFO',
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    request_logger = logging.getLogger("requests")
    request_logger.setLevel(logging.CRITICAL)

    main_logger = logging.getLogger(__name__)
    return main_logger


def get_flat_joke() -> str:
    response = requests.get("https://www.1a-flachwitze.de/zufall/")
    if response.status_code != 200:
        raise ConnectionRefusedError(response.text)
    parsed_html = BeautifulSoup(response.text, features="html.parser")
    question = parsed_html.find('header', attrs={'class': 'entry-header'}).text
    answer = parsed_html.findAll('div', attrs={'class': 'entry-content'})[2].next_element.text
    return f'{question} {answer}'


def send_slack_notification(url: str, message: str):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = {
        "text": message
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(body))
    if response.status_code != 200:
        raise ConnectionRefusedError(response.text)


def main():
    slack_webhook_url = getenv("SLACK_WEBHOOK_URL")
    if not slack_webhook_url:
        logger.error("env SLACK_WEBHOOK_URL not set.")
        exit()
    joke = get_flat_joke()
    send_slack_notification(slack_webhook_url, joke)


if __name__ == '__main__':
    logger = init_loggers()
    logger.info('Started...')
    main()
