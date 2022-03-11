from urllib import response
import requests

from bs4 import BeautifulSoup
import time
from random import randrange
import json

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
    articles_urls_list = []

    for page in range(1, pagination_count + 1):
    # for page in range(1, 2):
        response = s.get(url=f'https://elmakon.uz/telefony-gadzhety-aksessuary/smartfony/page-{page}/', headers=header)
        soup = BeautifulSoup(response.text, 'lxml')

        articles_info = soup.find_all('a', class_='product-title')

        for au in articles_info:
            art_url = au.get('href')
            articles_urls_list.append(art_url)

        # time.sleep(randrange(2, 5))
        print(f'We got {page}/{pagination_count}')
        # print(response)

    with open('articles_urls.txt', 'w') as file:
        for url in articles_urls_list:
            file.write(f'{url}\n')


    return 'Working link'
   # print(pagination_count)


def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]
   

    urls_count = len(urls_list)
    s = requests.Session()

    result_data = []

    for url in enumerate(urls_list[:5]):
        response = s.get(url=url[1], headers=header)
        soup = BeautifulSoup(response.text, 'lxml')

        article_title = soup.find('div', class_='ut2-pb ty-product-block ut2-three-columns ty-product-detail').find('h1', class_='ut2-pb__title').text.strip()
        article_selling_info = soup.find('div', class_='ty-control-group product-list-field').text.strip()
        prodact_info = soup.find('div', class_='ty-features-list').text.strip()
        prodact_image = soup.find('a', class_='cm-image-previewer cm-previewer ty-previewer').get('href')


        result_data.append(
            {
                'original_url': url[1],
                'article_title': article_title,
                'article_selling_info': article_selling_info,
                'prodact_info': prodact_info,
                'prodact_image': prodact_image,
            }
        )

        print(f'Preapering {url[0] + 1}/{urls_count}')
        # print(f"{article_title}\n{article_selling_info}\n{prodact_info}\n{prodact_image}\n")

    with open('result.json', 'w') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)   

def main():
    # print(get_article_urls(url='https://elmakon.uz/telefony-gadzhety-aksessuary/smartfony/'))
    get_data('articles_urls.txt')

if __name__ == '__main__':
    main()