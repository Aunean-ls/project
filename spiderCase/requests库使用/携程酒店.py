import requests
import os
import json

url = "https://m.ctrip.com/restapi/soa2/16709/json/HotelSearch?testab=3d57011a3735191ede7a5aa845560a9901b7cbd497b3ff65a9331f287b5c7895"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
    'origin': 'https://hotels.ctrip.com',
    'p': '27121495033',
    'referer': 'https://hotels.ctrip.com/',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site'
}
request_payload = {
    "meta": [{"fgt": "", "hotelId": "", "priceToleranceData": "", "priceToleranceDataValidationCode": "", "mpRoom": [],
              "hotelUniqueKey": "", "shoppingid": "", "minPrice": "", "minCurr": ""}],
    "seqid": "028d5d0a7e7b4a20a9a9a874b950d22d",
    "deduplication": [429531, 608516, 375126, 374788, 375265, 16975053, 23932218, 8019672, 47999531, 482534, 63053513,
                      918261, 28642364, 939388, 436894, 430601, 2231618, 30006625, 11305146, 6410223, 431071, 2272090,
                      21785802, 763321],
    "filterCondition": [{"star": [], "rate": "", "rateCount": [], "priceRange": {"lowPrice": 0, "highPrice": -1},
                         "priceType": "", "breakfast": [], "payType": [], "bedType": [], "bookPolicy": [],
                         "bookable": [], "discount": [], "zone": [], "landmark": [], "metro": [],
                         "airportTrainstation": [], "location": [], "cityId": [], "amenty": [], "promotion": [],
                         "category": [], "feature": [], "brand": [], "popularFilters": [], "hotArea": [],
                         "ctripService": [], "priceQuickFilters": [], "applicablePeople": []}],
    "searchCondition": [{"sortType": "1", "adult": 1, "child": 0, "age": "", "pageNo": 3, "optionType": "City",
                         "optionId": "1", "lat": 0, "destination": "", "keyword": "", "cityName": "北京", "lng": 0,
                         "cityId": 1, "checkIn": "2021-03-16", "checkOut": "2021-03-17", "roomNum": 1, "mapType": "gd",
                         "travelPurpose": 0, "countryId": 1,
                         "url": "https://hotels.ctrip.com/hotels/listPage?cityename=beijing&city=1&optionId=1&optionType=City&checkin=2021/03/16&checkout=2021/03/17#ctm_ref=hod_hp_sb_lst",
                         "pageSize": 10, "timeOffset": 28800, "radius": 0, "directSearch": 0, "signInHotelId": 0,
                         "signInType": 0, "hotelIdList": []}], "queryTag": "NORMAL", "genk": 'true',
    "genKeyParam": [{"a": 0, "b": "2021-03-16", "c": "2021-03-17", "d": "zh-cn", "e": 2}], "webpSupport": 'true',
    "platform": "online", "pageID": "102002",
    "head": [{"Version": "", "userRegion": "CN", "Locale": "zh-CN", "LocaleController": "zh-CN", "TimeZone": "8",
              "Currency": "CNY", "PageId": "102002", "webpSupport": 'true', "userIP": "", "P": 27121495033,
              "ticket": "",
              "clientID": "1615519048743.38n59q", "group": "ctrip",
              "Frontend": [{"vid": "1615519048743.38n59q", "sessionID": 3, "pvid": 9}],
              "Union": [{"AllianceID": "", "SID": "", "Ouid": ""}],
              "HotelExtension": [{"group": "CTRIP", "hasAidInUrl": 'false', "Qid": "137846391343", "WebpSupport": 'true',
                                 "hotelUuidKey": "mH8YctRQXeanEXOWfYZtY5UEzYFkedzE01jcUWAYDMR5qIqcvt1j9YaBemBwb9vQ4jaYPFvQSJB5y0ZjtY7fWS6YnqyDcItZvfMe35wDnjSsyGY5typ3v0liMzwn4jf3elZihSYTYAYbOvhGegtYh6ibaYmYHYpAEX1K4BRtdisLRD3jUrQUYsLJB3yQrPQY13WoZvTQxlfem9YX3xGzx95Ybmis3w71jdpE6pJkGWUqjhrP0Jz1i8UwHDv3GR6qjmNYFTjdrlqyLZioXwSORT1ElZj71x3ZxzZEkpEN8E6qWhze0nwkzEzgjtgesAiF7YdSrAkeS7ec1xN8iTqi46x9HW6PjHUeANw5mK8HwgqioXRDSjNcetmEshyqAvUqi7HEcAy3BvQQKd5EFDKoPwp7iODR1AjLrmLYNdJszyFr6Mjoheg4jXcKFQjQzwsGxQBxD8xbNxfbEF7E49EQ8WoMesUwM1EG1jcbeNBis7Yg5r46EmzydkvDdiF8EksyZtvDDKA9WG6EDZjNGefPxgQjSrcBEO8WDgeHcjoAYN0jLDxMGxQpxAhxOLE8UEGPEl0WSNe9nwAmE4TjsXe08il1YZzrone4XeN7YtoEh9wF4WqFiooKBqEpXEodE1LWlXefXwTkENAjmdeAoiQTYZgrhNesmeUoEsLYf4E06waQW8aitYcFYgmiAaiLbikhjpY8swFSETUY0kwqsEAQJnQY0Tw9YLGRzbwpzRBlJ0Tjk3j5AwmzJ6ZWMfWLOWP4RZFWUYlXJHmioNeSZRN7v99xtPJq7rZayUaYt3YSPjh9EMdx5gENFIcY3SRtLwShRHUJGsJUfROhv60WOdEoDjp1yGfELtiaY4ZjlBwFgvc7jlYk3R0SJ8MiBAwqoeLQj3SwLZEAYZsRA0E86yGUEnpem3jgBwqGEpYGbRq4wShRT0JaojgMjFBwksiF1W6HvMSyhdyslJkY0dEmNj9DWXsWOQWs1Y06Y4BY0MR0TYhlWUAYq8Y6BYOzjDHeX1E3FWpUec6wBZehmjbpYB9yHaELcjgkE8nrOmjUNw7N"}]}]
}

response = requests.post(url=url, data=json.dumps(request_payload), headers=headers).text
print(response)
