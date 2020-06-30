import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=3bd73b0f7d8feaa4600ddacbc7b8643a&format=1")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful")
    data = res.json()
    rate = data["rates"]["USD"]
    print(f"1 Euro is Equal to {rate} DOllars")

if __name__ == "__main__":
    main()
