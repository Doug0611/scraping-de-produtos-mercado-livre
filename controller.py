import requests
from bs4 import BeautifulSoup


def soup():
    for page in range(3):
        url = requests.get(f'https://www.mercadolivre.com.br/ofertas?page={page}')
        
        if url.status_code:
            soup = BeautifulSoup(url.text, 'html.parser')
            
            for item in soup.select('li.promotion-item'):
                image = str(item.select_one('img.promotion-item__img').get('src'))
                
                if not 'https://' in image:
                    image = image = str(item.select_one('img.promotion-item__img').get('data-src'))
                
                title = str(item.select_one('p.promotion-item__title').text) 
                old_price = str(item.select_one('span.promotion-item__oldprice').text)
                price = str(item.select_one('span.promotion-item__price').text)[:len(old_price)]
                
            
                price_cents = str(item.select_one('.promotion-item__price sup')).replace('<sup>','').replace('</sup>','')

                if price_cents == 'None':
                    price_cents = ''
                
                link = str(item.select_one('a.promotion-item__link-container').get('href'))
                price_descount = str(item.select_one('span.promotion-item__discount').text)
                
                installments = str(
                    item.select_one('span.promotion-item__installments')
                                ).replace(
                                    '<span class="promotion-item__installments">','').replace(
                                        '</span>','').replace(
                                            '<sup>',',').replace('</sup>','')
                
                if installments == 'None':
                    installments = ''   
                
                            
                yield { 'title': title,
                    'price': price,
                    'price_cents': price_cents,
                    'image': image,
                    'link_product': link,
                    'price_descount': price_descount,
                    'old_price': old_price,
                    'installments': installments,
                    }            
