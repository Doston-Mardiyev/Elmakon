from email import header
from urllib import response
import requests
from bs4 import BeautifulSoup

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

def get_article_urls(url):
    s = requests.Session()
    response = s.get(url=url, headers=header)

    # with open('index.html', 'w', encoding="utf-8") as file:
    #     file.write(response.text)

    soup = BeautifulSoup(response.text, 'lxml')
    pagination_count = int(soup.find('div', class_='ty-pagination__items').find_all('a')[-1].text)

    for page in range(1, 2):
        response = s.get(url=f'https://elmakon.uz/telefony-gadzhety-aksessuary/smartfony/page-{page}/', headers=header)
        #soup = BeautifulSoup(response.text, 'lxml')

        #articles_info = soup.find_all('a', class_='')

        print(response)


   # print(pagination_count)

def main():
    get_article_urls(url='https://elmakon.uz/telefony-gadzhety-aksessuary/smartfony/')


if __name__ == '__main__':
    main()