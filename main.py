import requests
from bs4 import BeautifulSoup
import json

headers = {
    "User_Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept" : "application/json, text/plain, */*"
}

result = []
for i in range(0, 11):
    url = f"https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset={i}&withStack=true"

    req = requests.get(url =url, headers=headers)

    data = req.json()
    items = data.get("items")

    for i in items:
        if i.get("overprice") is None:
            continue
        else:
            item_fullname = i.get("fullName")
            item_price = str(i.get("price")) + " $"
            item_3d = i.get("3d")
            item_overprice = i.get("overprice")
            result.append(
                {
                    "fullname" : item_fullname,
                    "price" : item_price,
                    "overprice" : item_overprice,
                    "3d" : item_3d
                }
            )

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent= 4, ensure_ascii=False)