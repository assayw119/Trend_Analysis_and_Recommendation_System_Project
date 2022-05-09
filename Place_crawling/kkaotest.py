from bs4 import BeautifulSoup as bs
import urllib.request as ur
import numpy as np

url = "http://place.map.kakao.com/8332362"
# url = "https://m.place.naver.com/restaurant/11831738/home"
html = ur.urlopen(url)
soup = bs(html.read(), "html.parser")
print(soup.find("div", {"id": "kakaoWrap"}).text)
