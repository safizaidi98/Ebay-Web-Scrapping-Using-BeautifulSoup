import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)
    print(response.ok)
    if not response.ok:
        print('Server that responded is not valid and the code : ', response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup
        
def get_data(soup_object):
    
    title = soup_object.find('h1', id_ = 'itemTitle')
#     title = soup_object.select('h1#itemTitle')[0].text.strip().split('Details about')
    # title = soup_object.select('h1#itemTitle').text.strip()
    print(title)
    
    
    
    
def main():
    url = 'https://www.ebay.com/itm/Mens-Leather-Military-Casual-Analog-Quartz-Wrist-Watch-Business-Watches-Gifts/312115693156?hash=item48ab8b8664:m:mGnNNrfrWAfVuG9ZMsyv5VQ'
    get_page(url)
 #   get_data(get_page(url))


if __name__ == '__name__':
    main()