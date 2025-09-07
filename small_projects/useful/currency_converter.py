from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, to_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={to_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find("span", class_="ccOutputRslt").get_text().split(" ")[0]
    currency = float(currency.split(" ")[0])
    return currency


def main():
    in_currency = input("From what currency you want to convert (ex. 'EUR'): ")
    out_currency = input("To what currency you want to convert (ex. 'USD'): ")
    currency = get_currency(in_currency, out_currency)
    how_much = float(input(f"How much {in_currency} you want to convert in {out_currency}: "))
    print(f"Result: {how_much} {in_currency} = {how_much * currency} {out_currency}")


if __name__ == "__main__":
    main()
