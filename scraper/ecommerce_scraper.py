import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://webscraper.io"

categories = {
    "laptops": "/test-sites/e-commerce/static/computers/laptops",
    "tablets": "/test-sites/e-commerce/static/computers/tablets",
    "phones": "/test-sites/e-commerce/static/phones/touch"
}

data = []

for category_name, category_path in categories.items():

    for page in range(1,6):

        url = base_url + category_path + "?page=" + str(page)

        response = requests.get(url)

        soup = BeautifulSoup(response.text,"html.parser")

        products = soup.find_all("div", class_="thumbnail")

        if len(products) == 0:
            break

        for product in products:

            name = product.find("a", class_="title").text.strip()
            price = product.find("h4", class_="price").text.strip()
            description = product.find("p", class_="description").text.strip()

            review_tag = product.find("p", class_="pull-right")

            if review_tag:
                reviews = review_tag.text.strip()
            else:
                reviews = "0 reviews"

            data.append({
                "product_name": name,
                "price": price,
                "description": description,
                "reviews": reviews,
                "category": category_name
            })

df = pd.DataFrame(data)

df.to_csv("ecommerce_products_raw.csv", index=False)