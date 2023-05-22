import re

link = "https://noveltyreaders.blogspot.com/2022/11/cebf-extra-4.html"

match = re.search(r"/(\w+)-chapter-", link)
if match:
    special_word = match.group(1)
    print(special_word)  # cebf
