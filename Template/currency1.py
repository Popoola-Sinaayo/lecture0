import requests

def main():
    base = input("Input first Currency")
    other = input("Input Second Currency")

    res = requests.get("http://data.fixer.io/api/latest?access_key=3bd73b0f7d8feaa4600ddacbc7b8643a&format=1", params={"base": base, "symbol": other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccesful")
    data = res.json()
    rate = data["rates"][other]
    print(f"1{base} is equal to {rate} {other}")
if __name__ == "__main__":
    main()
