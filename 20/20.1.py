# import requests
# from bs4 import BeautifulSoup
# import lxml
#
#
# cookies = {
#     'qrator_ssid': '1678192001.840.odHfZgf6BgCaIr5I-90d00gr1hecthj9npqgm9u981cebavlg',
#     'stest201': '1',
#     'stest207': 'acc1',
#     'stest209': 'ct1',
#     'PHPSESSID': '4823ae1be5a5ba27b9c0e5e366a91f41',
#     'user_public_id': 'fvCrhikTlu2Vonv6dlXgcNy%2FLB18fNXdXn84FHkYIV8buSg0Xtv%2FHx%2B2Jw7ELVxT',
#     '_gcl_au': '1.1.240965828.1678192003',
#     '_gid': 'GA1.2.930831409.1678192003',
#     'tmr_lvid': 'fa25bcb82e91785972307543c78852aa',
#     'tmr_lvidTS': '1678192003215',
#     '_ym_uid': '1678192003843039455',
#     '_ym_d': '1678192003',
#     '_ym_isad': '1',
#     '_ym_visorc': 'b',
#     'afUserId': 'f9a4a39d-c96f-4c56-9938-c420a0d562d4-p',
#     'AF_SYNC': '1678192004853',
#     'tp_city_id': '38733',
#     'pageviewTimer': '13.639',
#     '_userGUID': '0:ley877rt:tkraTG2tO8wBozV1ca7G1Bapt8lv5TgE',
#     'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20adebfff4529ef1737384%22}',
#     'dSesn': '5dfeb6c5-8b79-7ead-791d-4e7eb7dbf9ad',
#     '_dvs': '0:ley877rt:qj8S7JtDoVAE_hC2PCEpkxeTLAQq4Q1q',
#     'promo1000closed': 'true',
#     'qrator_jsid': '1678192000.704.aKFDs5OOtB3va4ET-mbef0qhmkmf9lfpdu8mpqsnktcvai1uo',
#     'visitedPagesNumber': '7',
#     '_gat_UA-25136986-1': '1',
#     'tmr_detect': '1%7C1678193592308',
#     '_ga_RD4H4CBNJ3': 'GS1.1.1678192003.1.1.1678193592.60.0.0',
#     '_ga': 'GA1.1.1861347801.1678192003',
#     'mindboxDeviceUUID': 'fdb99174-4575-452d-9be8-2116f35b4b40',
#     'directCrm-session': '%7B%22deviceGuid%22%3A%22fdb99174-4575-452d-9be8-2116f35b4b40%22%7D',
#     'pageviewTimer': '1605.181',
# }
#
# headers = {
#     'authority': 'sochi.technopark.ru',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,bg;q=0.6',
#     'cache-control': 'max-age=0',
#     # 'cookie': 'qrator_ssid=1678192001.840.odHfZgf6BgCaIr5I-90d00gr1hecthj9npqgm9u981cebavlg; stest201=1; stest207=acc1; stest209=ct1; PHPSESSID=4823ae1be5a5ba27b9c0e5e366a91f41; user_public_id=fvCrhikTlu2Vonv6dlXgcNy%2FLB18fNXdXn84FHkYIV8buSg0Xtv%2FHx%2B2Jw7ELVxT; _gcl_au=1.1.240965828.1678192003; _gid=GA1.2.930831409.1678192003; tmr_lvid=fa25bcb82e91785972307543c78852aa; tmr_lvidTS=1678192003215; _ym_uid=1678192003843039455; _ym_d=1678192003; _ym_isad=1; _ym_visorc=b; afUserId=f9a4a39d-c96f-4c56-9938-c420a0d562d4-p; AF_SYNC=1678192004853; tp_city_id=38733; pageviewTimer=13.639; _userGUID=0:ley877rt:tkraTG2tO8wBozV1ca7G1Bapt8lv5TgE; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20adebfff4529ef1737384%22}; dSesn=5dfeb6c5-8b79-7ead-791d-4e7eb7dbf9ad; _dvs=0:ley877rt:qj8S7JtDoVAE_hC2PCEpkxeTLAQq4Q1q; promo1000closed=true; qrator_jsid=1678192000.704.aKFDs5OOtB3va4ET-mbef0qhmkmf9lfpdu8mpqsnktcvai1uo; visitedPagesNumber=7; _gat_UA-25136986-1=1; tmr_detect=1%7C1678193592308; _ga_RD4H4CBNJ3=GS1.1.1678192003.1.1.1678193592.60.0.0; _ga=GA1.1.1861347801.1678192003; mindboxDeviceUUID=fdb99174-4575-452d-9be8-2116f35b4b40; directCrm-session=%7B%22deviceGuid%22%3A%22fdb99174-4575-452d-9be8-2116f35b4b40%22%7D; pageviewTimer=1605.181',
#     'dnt': '1',
#     'if-none-match': '"144bda-yU5xYp7QNBHDZhBh6VSC2+BLMRw"',
#     'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
# }
#
# response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies, headers=headers)
# # with open("page.html", "w", encoding="UTF-8") as f:
# #     f.write(response.text)
#
# with open("page.html", "r", encoding="UTF-8") as file:
#     page = file.read()
#     bs = BeautifulSoup(page, "lxml")
#     containers = bs.find_all("div", "product-card-big__container")
#     result = {}
#     for i in containers:
#         name = i.find("div", "product-card-big__name").text[13:-11]
#         price = i.find("div", "product-prices__price").text[5:-5]
#         result[name] = price
#     print(result)

import requests
import json
from bs4 import BeautifulSoup

response = requests.get("https://music.yandex.ru/chart/")
soup = BeautifulSoup(response.content, "html.parser")

chart_list = soup.find("div", "chart__list")

chart_data = {}
for i, chart_item in enumerate(chart_list.find_all("div", "chart__item")):
    artist = chart_item.find("div", "chart__item-author").text.strip()
    track = chart_item.find("div", "chart__item-title").text.strip()
    chart_data[i+1] = (artist, track)

with open("yandex_music_chart.json", "w") as f:
    json.dump(chart_data, f)
