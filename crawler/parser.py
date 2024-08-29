import requests
from parsel import Selector


def crawl_house_kg():
    url = 'https://www.house.kg/snyat'
    response = requests.get(url)
    selector = Selector(response.text)

    links = selector.css('a.listing__item::attr(href)').getall()
    full_links = [f'https://www.house.kg{link}' for link in links if link]

    return full_links

