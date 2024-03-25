import requests
from bs4 import BeautifulSoup

# this is ecommerce web scraping project

class EcommerceProductPages:
    def __init__(self
                 , base_url : str
                 , product_name : str
                 , product_description : str
                 , product_price : str
                 , product_quantity : str
                 , product_image_url : str
                 , product_url : str
                 ):
        self.base_url = base_url
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price

