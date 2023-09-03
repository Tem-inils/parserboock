import requests
from bs4 import BeautifulSoup


#<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
#<a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>

url = 'https://books.toscrape.com/'
def parse_page(url):
    pars = requests.get(url)
    soup = BeautifulSoup(pars.content, "html.parser")

    book_items = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for index, item in enumerate(book_items, start=1):
        book_link = item.find("a")["href"]
        book_title = item.find("h3").find("a")["title"]
        book_price = item.find("div", class_="product_price").find("p", class_="price_color").text
        book_in_stock = item.find("div", class_="product_price").find("p", class_="instock availability").text
        print(f"{index}. Title:", book_title)
        print("Price", book_price)
        print("In stock:", book_in_stock.strip())
        print("  Link", book_link)
        print("-" * 50)

for page_number in range(1, 51):
    page_url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    parse_page(page_url)

