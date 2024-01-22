"""There is currently one goal: ship it quickly"""
from bs4 import BeautifulSoup
import re
import requests

url = 'https://infourok.ru/metodicheskaya-razrabotka-uprazhneniya-po-podgotovke-k-sochineniyu-na-ege-po-russkomu-yaziku-2218364.html'

def scrape(url: str) -> str:
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, 'html.parser')

    content_element = soup.find(id='aa-scroll-0')
    if not content_element:
        return "Не удалось разобрать исходную страницу"

    content = str(content_element)
    regex = r"style=\".*?\""
    content = re.sub(regex, "", content, 0, re.MULTILINE)
    return content

template = ''
with open('template.html', 'r') as file:
    template = file.read()

def create_template(body):
    html = template.replace('TITLE GOES HERE', 'infourok').replace('CONTENT GOES HERE', body)
    return html
