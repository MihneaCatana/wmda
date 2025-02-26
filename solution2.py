### **Exercise 2: Web Scraping a Product Listings Page**
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

# Fetch the webpage content
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Extract product names and prices
products = soup.find_all("div", class_="thumbnail")
product_data_df = pd.DataFrame()

print("Scraped Product Prices:\n")

for product in products[:20]:  # Limit to first 10 products
    name = product.find("a", class_="title").text.strip()
    price = product.find("h4", class_="price").text.strip()
    product_json = {
        "name": [name],
        "price": [price]
    }

    product_df = pd.DataFrame(product_json)
    print(product_json)
    product_data_df = pd.concat([product_data_df, product_df], ignore_index=True)

df_cleaned =product_data_df.drop_duplicates()
print(df_cleaned)
df_cleaned.to_csv("scraped_products.csv", index=False)