import cloudscraper

url = "https://guavaread.com/novel/i-became-my-sons-first-love/chapter-46/"
scraper = cloudscraper.create_scraper()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

cookies = {
    "PHPSESSID": "0e1fc6361290818444e114e964131979",
    "cf_clearance": "5l1.5C1uJPp3yRHRozXsv7HHnuCKCN1IsFpveFhhuTw-1721841226-1.0.1.1-PMiQUBzRHNvU7IK.rfbtW16kD8Wj3jf5aM7WMRxpaO1rrqqbcJHUB0.t2UTGNX8XaUb7iPqYPjcKX_FR_5sTwg",
    "quads_browser_width": "1920",
    "quads_browser_width": "1920",
    "wpmanga-reading-history": "W3siaWQiOjIwOTYsImMiOiIzNjQ1IiwicCI6MSwiaSI6IiIsInQiOjE3MjE4NDI0Nzl9XQ%3D%3D"
}

response = scraper.get(url, headers=headers, cookies=cookies)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Ошибка: {response.status_code}")
