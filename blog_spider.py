import requests
from bs4 import BeautifulSoup

urls = [
    f'https://www.cnblogs.com/#p{page}'
    for page in range(1, 50+1)
]

# print(urls)

def craw(url):
    r = requests.get(url)
    # print(url, len(r.text))
    return r.text

# craw(urls[0])

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', 'post-item-title')
    return [(link['href'], link.get_text()) for link in links]

if __name__ == '__main__':
    html = craw(urls[0])
    res = parse(html)
    print(res)