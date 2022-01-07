import requests
import argparse
from bs4 import BeautifulSoup
import datetime

def try_parse_date(text: str):
    try:
        return datetime.datetime.strptime(text, "%A %B %d, %Y").date()
    except:
        pass

def parse_next_trash_and_recycling_dates(address_number: str, street_direction: str, street_name: str, street_suffix: str):
    data = dict(laddr=address_number, sdir=street_direction, sname=street_name, stype=street_suffix, embed="Y", Submit="Submit")
    response = requests.post("https://itmdapps.milwaukee.gov/DpwServletsPublic/garbage_day", data=data)
    parsed = BeautifulSoup(response.text, features="html.parser")
    strong_elements = parsed.find_all("strong")
    dates = []
    for element in parsed.find_all("strong"):
        parsed_date = try_parse_date(element.text)
        if parsed_date:
            dates.append(parsed_date)

    if len(dates) != 2:
        raise Exception(f"Failed to parse: {response.text}")

    return dates[0], dates[1]

def main():
    parser = argparse.ArgumentParser(description="Get data from Milwaukee DPW")
    parser.add_argument("address_number", type=str, help="Address number, e.g., 200")
    parser.add_argument("street_direction", type=str, help="Street direction, e.g., N")
    parser.add_argument("street_name", type=str, help="Street name, e.g., 1st")
    parser.add_argument("street_suffix", type=str, help="Street suffix, e.g., st")
    args = parser.parse_args()
    trash_date, recycling_date = parse_next_trash_and_recycling_dates(args.address_number, args.street_direction.upper(), args.street_name.upper(), args.street_suffix.upper())
    print(trash_date)
    print(recycling_date)

if __name__ == "__main__":
    main()
