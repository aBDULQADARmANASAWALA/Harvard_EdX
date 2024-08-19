from sys import argv, exit
import requests

try:
    if len(argv) == 2:
        n = float(argv[1])
    else:
        print("Missing Command-Line Argument")
        exit(1)
except ValueError:
        print("Command-Line Argument is not a Number")
        exit(1)

try:
     response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
     print("Error querying response from API")
     exit(1)

amount = float(response.json()["bpi"]["USD"]["rate"].replace(",", "")) * n
print(f"${amount:,.4f}")
