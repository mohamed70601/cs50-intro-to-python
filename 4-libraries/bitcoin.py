import sys
import requests


def main():
    # updated sys.exit to 1
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=key***"
        )
        data = response.json()
        price = float(data["data"]["priceUsd"])
        amount = bitcoin * price
        print(f"${amount:,.4f}")

    except requests.RequestException:
        print("Error")


main()
